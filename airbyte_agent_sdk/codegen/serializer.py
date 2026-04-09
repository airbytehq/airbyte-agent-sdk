"""
Python code serializer for ConnectorModel.

Converts ConnectorModel Pydantic models to Python constructor code for embedding
in generated connectors.
"""

from __future__ import annotations

from enum import Enum
from typing import Any
from uuid import UUID

from airbyte_agent_sdk.types import ConnectorModel


class PythonCodeSerializer:
    """Serialize Pydantic models to Python constructor code."""

    def __init__(self):
        """Initialize serializer with tracking for imports.

        We track actual type objects (not just names) so we can dynamically
        determine their module path using __module__. This eliminates the need
        for manual maintenance of type-to-module mappings.
        """
        # Track type objects (not just names) so we can inspect their modules
        self.type_objects: dict[str, type] = {}
        self.indent_size = 4

    def serialize_connector_model(self, model: ConnectorModel) -> tuple[str, dict[str, list[str]]]:
        """Generate Python code + import list for ConnectorModel.

        Args:
            model: ConnectorModel object to serialize

        Returns:
            Tuple of (python_code, imports_dict) where imports_dict maps module to list of types
        """
        self.type_objects = {}
        self.type_objects["ConnectorModel"] = ConnectorModel
        code = self._serialize_value(model, indent=0, is_top_level=True)

        # Organize imports by module (dynamically determined from __module__)
        imports_by_module: dict[str, list[str]] = {}
        for type_name in sorted(self.type_objects.keys()):
            type_obj = self.type_objects[type_name]
            module = self._get_relative_module(type_obj)

            if module not in imports_by_module:
                imports_by_module[module] = []
            imports_by_module[module].append(type_name)

        return code, imports_by_module

    def _get_relative_module(self, type_obj: type) -> str:
        """Get the relative module path for a type.

        Converts full module paths like 'airbyte_agent_sdk.types' to 'types',
        'airbyte_agent_sdk.schema.security' to 'schema.security', etc.

        For standard library types (like UUID from 'uuid'), returns the module as-is.

        Args:
            type_obj: The type object to get the module for

        Returns:
            Relative module path for imports
        """
        full_module = type_obj.__module__

        # Remove 'airbyte_agent_sdk.' prefix to get relative path
        if full_module.startswith("airbyte_agent_sdk."):
            return full_module[len("airbyte_agent_sdk.") :]

        return full_module

    def _serialize_value(self, value: Any, indent: int, is_top_level: bool = False) -> str:
        """Recursively serialize a value to Python code.

        Args:
            value: Value to serialize
            indent: Current indentation level
            is_top_level: Whether this is the top-level ConnectorModel

        Returns:
            Python code string
        """
        if value is None:
            return "None"

        if isinstance(value, bool):
            return "True" if value else "False"

        # Check for Enum BEFORE str, because string enums are both
        if isinstance(value, Enum):
            return self._serialize_enum(value)

        if isinstance(value, (int, float)):
            return str(value)

        if isinstance(value, str):
            # Escape strings properly
            return repr(value)

        if isinstance(value, UUID):
            # Track UUID type for imports
            self.type_objects["UUID"] = UUID
            # Serialize as UUID constructor call
            return f"UUID('{value}')"

        if isinstance(value, dict):
            return self._serialize_dict(value, indent)

        if isinstance(value, list):
            return self._serialize_list(value, indent)

        if hasattr(value, "model_dump"):
            return self._serialize_pydantic_model(value, indent, is_top_level)

        # Fallback for unknown types
        return repr(value)

    def _serialize_enum(self, value: Enum) -> str:
        """Serialize an enum value.

        Args:
            value: Enum instance

        Returns:
            Python code string
        """
        # Track the enum type for imports
        enum_class = value.__class__
        enum_class_name = enum_class.__name__
        self.type_objects[enum_class_name] = enum_class

        # For string enums, we can use the value directly as a constructor argument
        # This works for Action, AuthType, ContentType which are all str enums
        return f"{enum_class_name}.{value.name}"

    def _serialize_dict(self, value: dict, indent: int) -> str:
        """Serialize a dictionary.

        Args:
            value: Dictionary to serialize
            indent: Current indentation level

        Returns:
            Python code string
        """
        if not value:
            return "{}"

        # Filter out None values and empty collections
        filtered_items = {}
        for k, v in value.items():
            # Skip None values
            if v is None:
                continue
            # Skip empty lists and dicts
            if isinstance(v, (list, dict)) and len(v) == 0:
                continue
            filtered_items[k] = v

        if not filtered_items:
            return "{}"

        # Check if this is a simple one-liner dict
        if len(filtered_items) <= 2 and all(isinstance(v, (str, int, float, bool, type(None))) for v in filtered_items.values()):
            items = [f"{self._serialize_value(k, indent)}: {self._serialize_value(v, indent)}" for k, v in filtered_items.items()]
            return "{" + ", ".join(items) + "}"

        # Multi-line dict
        indent_str = " " * (indent + self.indent_size)
        lines = ["{"]

        for k, v in filtered_items.items():
            serialized_key = self._serialize_value(k, indent)
            serialized_value = self._serialize_value(v, indent + self.indent_size)
            lines.append(f"{indent_str}{serialized_key}: {serialized_value},")

        lines.append(" " * indent + "}")
        return "\n".join(lines)

    def _serialize_list(self, value: list, indent: int) -> str:
        """Serialize a list.

        Args:
            value: List to serialize
            indent: Current indentation level

        Returns:
            Python code string
        """
        if not value:
            return "[]"

        # Check if this is a simple one-liner list
        if len(value) <= 3 and all(isinstance(v, (str, int, float, bool, type(None))) for v in value):
            items = [self._serialize_value(v, indent) for v in value]
            return "[" + ", ".join(items) + "]"

        # Multi-line list
        indent_str = " " * (indent + self.indent_size)
        lines = ["["]

        for item in value:
            serialized_item = self._serialize_value(item, indent + self.indent_size)
            lines.append(f"{indent_str}{serialized_item},")

        lines.append(" " * indent + "]")
        return "\n".join(lines)

    def _serialize_pydantic_model(self, model: Any, indent: int, is_top_level: bool = False) -> str:
        """Serialize a Pydantic model to constructor code.

        Args:
            model: Pydantic model instance
            indent: Current indentation level
            is_top_level: Whether this is the top-level ConnectorModel

        Returns:
            Python code string
        """
        model_class = model.__class__
        model_class_name = model_class.__name__

        # Track this model for imports
        self.type_objects[model_class_name] = model_class

        # Get the fields from the actual model, not dict representation
        # This preserves Pydantic models and enums properly
        fields_to_serialize = {}

        # Fields to exclude from serialization
        excluded_fields = {"openapi_spec"}  # Don't serialize openapi_spec - not needed at runtime

        # Iterate through model fields
        for field_name in model_class.model_fields.keys():
            if field_name in excluded_fields:
                continue

            value = getattr(model, field_name, None)

            # Skip None values
            if value is None:
                continue

            # Skip empty lists and dicts (common default values)
            if isinstance(value, (list, dict)) and len(value) == 0:
                continue

            # Skip fields with default values
            field_info = model_class.model_fields[field_name]
            if field_info.default is not None and value == field_info.default:
                continue
            if field_info.default_factory is not None:
                default_value = field_info.default_factory()
                if value == default_value:
                    continue

            fields_to_serialize[field_name] = value

        if not fields_to_serialize:
            return f"{model_class_name}()"

        # Build constructor call with keyword arguments
        indent_str = " " * (indent + self.indent_size)
        lines = [f"{model_class_name}("]

        for key, value in fields_to_serialize.items():
            serialized_value = self._serialize_value(value, indent + self.indent_size)

            # Handle multi-line values
            if "\n" in serialized_value:
                lines.append(f"{indent_str}{key}={serialized_value},")
            else:
                lines.append(f"{indent_str}{key}={serialized_value},")

        lines.append(" " * indent + ")")

        return "\n".join(lines)

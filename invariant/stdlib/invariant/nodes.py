from dataclasses import dataclass
from typing import Union

@dataclass
class LLM:
    vendor: str
    model: str

@dataclass
class Message:
    content: str
    role: str

@dataclass
class ToolCall:
    id: str
    type: str
    function: list

@dataclass
class Function:
    name: str
    arguments: dict

@dataclass
class ToolOutput:
    role: str
    content: str
    tool_call_id: str

@dataclass
class Trace:
    elements: Message | ToolCall | ToolOutput
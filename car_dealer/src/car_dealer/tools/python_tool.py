from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_experimental.utilities import PythonREPL

class PythonToolInput(BaseModel):
    """Input schema for PythonTool."""
    code: str = Field(..., description="Python code to execute")

class PythonTool(BaseTool):
    name: str = "Python Executor"
    description: str = "Execute Python code and return the results"
    args_schema: Type[BaseModel] = PythonToolInput
    
    def _run(self, code: str) -> str:
        repl = PythonREPL()
        return repl.run(code) 
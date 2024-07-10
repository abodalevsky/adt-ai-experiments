# callbacks for debugging

from typing import Dict, Any, List, Union

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import LLMResult
from langchain_core.agents import AgentAction, AgentFinish, AgentStep


class AgentCallbackHandler(BaseCallbackHandler):
    def __init__(self):
        self.buffer = []

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> Any:
        """Run when LLM starts running."""
        self.buffer.append("\n\n--- on_llm_start ---\n")
        self.buffer.append(prompts[0])

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        """Run when LLM ends running."""
        self.buffer.append("\n\n--- on_llm_end ---\n")
        self.buffer.append(response.generations[0][0].text)

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when LLM errors."""
        self.buffer.append("\n\n--- on_llm_error ---\n")
        self.buffer.append(error)
    
    def on_chain_start(
        self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
    ) -> Any:
        """Run when chain starts running."""
        self.buffer.append(f'\n\n{kwargs.get("run_id")}--- on_chain_start ---')
        self.buffer.append(f'{kwargs.get("run_id")}:{inputs}')

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
        """Run when chain ends running."""
        self.buffer.append(f'\n\n{kwargs.get("run_id")}--- on_chain_end ---')
        self.buffer.append(f'{kwargs.get("run_id")}:{outputs}')

    def on_chain_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when chain errors."""
        self.buffer.append(f'\n\n{kwargs.get("run_id")}--- on_chain_error ---')
        self.buffer.append(f'{kwargs.get("run_id")}:{error}')

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs: Any
    ) -> Any:
        """Run when tool starts running."""
        self.buffer.append(f'\n\n{kwargs.get("run_id")}--- on_tool_start {serialized["name"]} ---')
        self.buffer.append(f'{kwargs.get("run_id")}:{input_str}')

    def on_tool_end(self, output: Any, **kwargs: Any) -> Any:
        """Run when tool ends running."""
        self.buffer.append(f'\n\n{kwargs.get("run_id")}--- on_tool_end ---')
        self.buffer.append(f'{kwargs.get("run_id")}:{output}')

    def on_tool_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> Any:
        """Run when tool errors."""
        self.buffer.append(f'\n\n{kwargs.get("run_id")}--- on_tool_error ---')
        self.buffer.append(f'{kwargs.get("run_id")}:{error}')


    def on_text(self, text: str, **kwargs: Any) -> Any:
        """Run on arbitrary text."""
        self.buffer.append("\n\n--- on_text ---\n")
        self.buffer.append(text)

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        """Run on agent action."""
        self.buffer.append("\n\n--- on_agent_action ---\n")
        self.buffer.append(action)

    def on_agent_finish(self, finish: AgentFinish, **kwargs: Any) -> Any:
        """Run on agent end."""
        self.buffer.append("\n\n--- on_agent_finish ---\n")
        self.buffer.append(finish)

    def print_buffer(self):
        """Print the buffer."""
        for item in self.buffer:
            print(item)
    
    def clear_buffer(self):
        """Clear the buffer."""
        self.buffer = []
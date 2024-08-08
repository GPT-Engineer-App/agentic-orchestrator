from langchain.tools import BaseTool

class WebAPI(BaseTool):
    name = "Web API"
    description = "Fetches additional data from web APIs"

    def _run(self, query: str) -> str:
        # Implement web API call logic here
        return f"Web API result for query: {query}"

    def _arun(self, query: str) -> str:
        # Implement async version if needed
        raise NotImplementedError("WebAPI does not support async")

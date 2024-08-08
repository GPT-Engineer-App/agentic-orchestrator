from langchain.tools import BaseTool

class EmbeddingSheet(BaseTool):
    name = "Embedding Sheet"
    description = "Provides product line and pricing information"

    def _run(self, product_type: str) -> str:
        # Implement embedding sheet logic here
        return f"Embedding sheet info for product type: {product_type}"

    def _arun(self, product_type: str) -> str:
        # Implement async version if needed
        raise NotImplementedError("EmbeddingSheet does not support async")

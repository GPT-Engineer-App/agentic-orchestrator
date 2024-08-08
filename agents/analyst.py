from crewai import Agent
from langchain.llms import OpenAI
from tools.vision_llm import VisionLLM
from tools.data_embedding import DataEmbedding

class Analyst:
    def __init__(self):
        self.agent = Agent(
            role='Multimodal Data Analyst',
            goal='Analyze and extract information from various data sources',
            backstory='You are an expert in image captioning and document analysis.',
            verbose=True,
            llm=OpenAI(temperature=0.2),
            tools=[VisionLLM(), DataEmbedding()]
        )

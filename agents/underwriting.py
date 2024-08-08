from crewai import Agent
from langchain.llms import OpenAI
from tools.embedding_sheet import EmbeddingSheet

class Underwriting:
    def __init__(self):
        self.agent = Agent(
            role='Insurance Underwriter',
            goal='Perform risk assessment and determine coverage and pricing',
            backstory='You are an expert in risk calculation and insurance product design.',
            verbose=True,
            llm=OpenAI(temperature=0.1),
            tools=[EmbeddingSheet()]
        )

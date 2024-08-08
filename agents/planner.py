from crewai import Agent
from langchain.llms import OpenAI
from tools.web_api import WebAPI

class Planner:
    def __init__(self):
        self.agent = Agent(
            role='Additional Data Source Planner',
            goal='Enrich knowledge about objects, items, and locations',
            backstory='You specialize in gathering additional context and information.',
            verbose=True,
            llm=OpenAI(temperature=0.3),
            tools=[WebAPI()]
        )

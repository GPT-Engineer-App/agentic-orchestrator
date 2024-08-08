from crewai import Agent
from langchain.llms import OpenAI

class Checker:
    def __init__(self):
        self.agent = Agent(
            role='Policy Compiler and Checker',
            goal='Compile and verify the final insurance policy',
            backstory='You ensure the accuracy and completeness of insurance policies.',
            verbose=True,
            llm=OpenAI(temperature=0)
        )

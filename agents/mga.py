from crewai import Agent, Task
from langchain.llms import OpenAI

class MGA:
    def __init__(self):
        self.agent = Agent(
            role='Managing General Agent',
            goal='Orchestrate the insurance workflow system',
            backstory='You are the main orchestrator of the AGENTIC workflow system.',
            verbose=True,
            allow_delegation=True,
            llm=OpenAI(temperature=0)
        )

    def create_tasks(self, crew):
        return [
            Task(
                description='Initiate and manage the insurance workflow',
                agent=self.agent,
                expected_output='A complete insurance policy proposal'
            )
        ]

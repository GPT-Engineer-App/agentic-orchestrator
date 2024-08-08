from crewai import Crew
from agents.mga import MGA
from agents.analyst import Analyst
from agents.planner import Planner
from agents.underwriting import Underwriting
from agents.checker import Checker

def main():
    # Initialize agents
    mga = MGA()
    analyst = Analyst()
    planner = Planner()
    underwriting = Underwriting()
    checker = Checker()

    # Create the crew
    crew = Crew(
        agents=[mga.agent, analyst.agent, planner.agent, underwriting.agent, checker.agent],
        tasks=mga.create_tasks(crew),
        verbose=2
    )

    # Start the crew's work
    result = crew.kickoff()

    print("Final Result:", result)

if __name__ == "__main__":
    main()

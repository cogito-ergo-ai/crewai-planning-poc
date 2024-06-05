import os
import sys
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_community.llms import Ollama

model = Ollama(model="mistral")
search_tool = SerperDevTool()
website_tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="ollama",
            config=dict(
                model="llama3",
            ),
        ),
        embedder=dict(
            provider="gpt4all",
            config=dict(
                model="nomic-ai/nomic-embed-text-v1.5-GGUF",
            ),
        ),
    )
)

planning_agent = Agent(
    role="Holiday planner",
    goal="Plan an holiday in Split, Croatia in june 2024",
    backstory=("You are an holiday planner"),
    tools=[search_tool, website_tool],
    allow_delegation=False,
    verbose=True,
    llm=model,
)


planning_task = Task(
    description=(
        "Plan an holiday in Split, Croatia in june 2024. You should look for flights from Milan. Look for hotels"
    ),
    expected_output="A comprehensive plan for the trip to Split, Croatia in june 2024",
    agent=planning_agent,
)

city_expert_agent = Agent(
    role="Expert of the city of Split, Croatia",
    goal="You know everything about the city of Split and want to suggest amazing activities in the city",
    backstory=("You are an expert of Split in Croatia"),
    tools=[search_tool, website_tool],
    allow_delegation=False,
    verbose=True,
    llm=model,
)

city_exploration_task = Task(
    description=("Plan a full exploration of the city of Split in Croatia."),
    expected_output="A comprehensive plan of things to see and activities to do in Split, Croatia",
    agent=city_expert_agent,
)


crew = Crew(
    agents=[planning_agent, city_expert_agent],
    tasks=[planning_task, city_exploration_task],
    process=Process.sequential,
    cache=True,
    max_rpm=100,
    share_crew=True,
)


if __name__ == "__main__":
    if not os.getenv("SERPER_API_KEY"):
        print("SERPER_API_KEY is not defined")
        sys.exit(1)
    result = crew.kickoff()
    print(result)

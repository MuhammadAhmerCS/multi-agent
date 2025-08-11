from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

def run_research(topic: str, api_key: str):
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        temperature=0.5,
        api_key=api_key
    )

    researcher = Agent(
        role=f"{topic} Senior Researcher",
        goal=f"Uncover groundbreaking technologies in {topic} for year 2024",
        backstory="Driven by curiosity, you explore and share the latest innovations.",
        tools=[SerperDevTool()],
        llm=llm
    )

    research_task = Task(
        description=f"Identify the next big trend in {topic} with pros and cons.",
        expected_output=f"A 3-paragraph report on emerging {topic} technologies.",
        agent=researcher
    )

    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff(inputs={'topic': topic})
    return result

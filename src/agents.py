from versionhq.agent.model import Agent

def create_agents(llm: str = None) -> tuple[Agent]:
  # for the info retrival, reasoning tasks
  researcher = Agent(
    role="Researcher",
    goal="Retrieve and summarize relevant information.",
    backstory="You are a researcher studying animal domestication.",
    llm=llm,
    knowledge_sources=[ # knowledge feeded to the agent. you can add/remove file paths or urls.
      "https://pmc.ncbi.nlm.nih.gov/articles/PMC5790555/",
    ]
  )
   
  # for text gent tasks
  content_creator = Agent(
    role="Content Creator",
    goal="Write creative content.",
    llm=llm,
  )
  
  return researcher, content_creator

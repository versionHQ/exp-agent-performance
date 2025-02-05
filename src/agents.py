from versionhq import Agent


def create_agents(llm: str = None) -> tuple[Agent]:
  researcher = Agent(
    role="Researcher",
    goal="Retrieve and summarize relevant information.",
    backstory="You are a researcher studying animal domestication.",
    llm=llm,
    knowledge_sources=[
      "https://pmc.ncbi.nlm.nih.gov/articles/PMC5790555/",
    ]
  )
  
  content_creator = Agent(
    role="Content Creator",
    goal="Write creative content.",
    llm=llm,
  )
  
  return researcher, content_creator

import versionhq as vhq


def create_agents(llm: str = None) -> tuple[vhq.Agent]:
  researcher = vhq.Agent(
    role="Researcher",
    goal="Retrieve and summarize relevant information.",
    backstory="You are a researcher studying animal domestication.",
    llm=llm,
    knowledge_sources=[
      "https://pmc.ncbi.nlm.nih.gov/articles/PMC5790555/",
    ]
  )
  
  content_creator = vhq.Agent(
    role="Content Creator",
    goal="Write creative content.",
    llm=llm,
  )
  
  return researcher, content_creator

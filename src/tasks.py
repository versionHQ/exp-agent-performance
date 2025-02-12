import versionhq as vhq
from pydantic import BaseModel


class Output(BaseModel):
  """A class to store output from the agents"""
  evidences: list[str]
  answer: str
  reasoning: str



task_info_retrieval = vhq.Task(
  description="""
Process the given knowledge sources and answer the following question: 
What specific evidences supported the traditional view of cat domestication centered on Egypt?
List up the evidences.
""",
  pydantic_output=Output,
  should_evaluate=True,
  eval_criteria=[
    "Accuracy of the answers", 
    "Accuracy of the question understanding", 
  ]
)


task_reasoning = vhq.Task(
  description="""
Based on the provided text, answer the following question, explaining your reasoning for the answer.
Question:
The article poses the question of why cats, unlike many other domesticated animals, were not domesticated for their labor or food. 
What is the explanation offered in the text for why cats began living with humans? 
How did the environment of early human settlements play a role?
""",
  pydantic_output=Output,
  should_evaluate=True,
  eval_criteria=[
    "Accuracy of the answers", 
    "Accuracy of the question understanding",
  ]
)

task_text_gen = vhq.Task(
  description="Write me a poem about palm trees in the style of Emily Dickinson.",
  should_evaluate=True,
  eval_criteria=[
    "Creativity", 
    "Accuracy to the given request",
  ]
)
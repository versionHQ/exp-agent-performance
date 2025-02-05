from dotenv import load_dotenv
from typing import Any, Tuple

from versionhq import TaskOutput

from src.tasks import task_info_retrieval, task_reasoning, task_text_gen
from src.agents import create_agents

load_dotenv(override=True)

llms_to_test = [
  "gpt-4o",
  "gemini/gemini-2.0-flash-exp",
  "openrouter/deepseek/deepseek-r1",
  "openrouter/qwen/qwen-2.5-72b-instruct",
]

results = {
  "gpt-4o": [],
  "gemini/gemini-2.0-flash-exp": [],
  "openrouter/deepseek/deepseek-r1": [],
  "openrouter/qwen/qwen-2.5-72b-instruct": [],
}


def execute_task(llm: str, index: int | str) -> Tuple[TaskOutput, dict[str, Any]]:
  researcher, creator = create_agents(llm=llm)
  tasks = [
    (task_info_retrieval, researcher),
    (task_reasoning, researcher),
    (task_text_gen, creator),
  ]
  res = tasks[index][0].execute_sync(agent=tasks[index][1])
  if res.raw:
    results[llm].append(
      {
        index: (
          res.json_dict,
          res.evaluation.aggregate_score,
          res.evaluation.latency,
          res.evaluation.tokens,
          res.evaluation.suggestion_summary
        )
      }
    )

  return res, results



if __name__ == "__main__":
  for llm in llms_to_test:
    for i in range(0, 3):
      res, results = execute_task(llm=llm, index=i)
  
  print(results)

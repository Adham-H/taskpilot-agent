from utils.llm import call_llm

def planner_agent(goal):
    prompt = f"""
Decompose this goal into clear structured steps:

Goal: {goal}
"""

    response = call_llm(prompt)

    steps = response.split("\n")
    return [s for s in steps if s.strip()]
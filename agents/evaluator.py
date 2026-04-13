from utils.llm import call_llm

def evaluator_agent(goal, output):
    prompt = f"""
Evaluate this output:

Goal: {goal}
Output: {output}

Score from 1 to 10 and explain.
"""

    return call_llm(prompt)
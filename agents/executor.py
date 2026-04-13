from utils.llm import call_llm

def executor_agent(step, memory):
    context = memory.get_context()

    prompt = f"""
Execute the following step:

Step: {step}
Context: {context}
"""

    return call_llm(prompt)
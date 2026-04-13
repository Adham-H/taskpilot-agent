from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.evaluator import evaluator_agent
from memory.short_memory import ShortMemory

def run_multi_agent(goal):
    memory = ShortMemory()

    print(f"\n🎯 Goal: {goal}")

    plan = planner_agent(goal)
    print("\n🧠 Plan:", plan)

    results = []

    for step in plan:
        result = executor_agent(step, memory)
        memory.add(step, result)
        results.append(result)

    final_output = "\n".join(results)

    score = evaluator_agent(goal, final_output)

    print("\n📊 Evaluation:", score)
    print("\n✅ Final Output:\n", final_output)

    return score

if __name__ == "__main__":
    goal = input("Enter your goal: ")
    run_multi_agent(goal)
from main import run_multi_agent

tasks = [
    "Plan a trip to Luxor",
    "Compare electric vs gasoline cars",
    "Create a study plan for Python"
]

def run_benchmark():
    results = {}

    for task in tasks:
        print(f"\nRunning: {task}")
        results[task] = run_multi_agent(task)

    return results

if __name__ == "__main__":
    run_benchmark()
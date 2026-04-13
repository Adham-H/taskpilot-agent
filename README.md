# TaskPilot Agent

TaskPilot Agent is a lightweight multi-agent prototype for exploring agentic task execution with planning, memory, execution, and evaluation components.

It takes a user goal, decomposes it into steps, executes those steps sequentially, keeps short-term context, and evaluates the final result. The project is designed as a simple research-style scaffold for experimenting with agent harnesses and evaluation.

## Features

- Planner agent for task decomposition
- Executor agent for step-by-step task handling
- Evaluator agent for output scoring
- Short-term memory for context tracking
- Simulated LLM wrapper for offline testing
- Benchmark script for running multiple sample tasks
- Modular structure for future extension into tool use, long-term memory, and multi-agent experiments

## Project Structure

```text
taskpilot-agent/
+-- agents/
¦   +-- communicator.py
¦   +-- evaluator.py
¦   +-- executor.py
¦   +-- memory.py
¦   +-- planner.py
+-- experiments/
¦   +-- benchmark.py
¦   +-- results.json
+-- memory/
¦   +-- long_memory.py
¦   +-- short_memory.py
+-- tools/
¦   +-- calculator.py
¦   +-- search.py
+-- utils/
¦   +-- llm.py
+-- config.py
+-- main.py
+-- README.md
```

## How It Works

1. The user enters a goal.
2. The planner agent breaks the goal into structured steps.
3. The executor agent processes each step using recent memory as context.
4. The evaluator agent scores the final combined output.
5. The system can be benchmarked across multiple tasks.

## Running the Project

```bash
python main.py
```

Example input:

```text
Plan a trip to Luxor
```

## Running Benchmarks

```bash
python experiments/benchmark.py
```

Example benchmark tasks include:

- Plan a trip to Luxor
- Compare electric vs gasoline cars
- Create a study plan for Python

## Current LLM Mode

The project currently uses a simulated LLM wrapper in `utils/llm.py` for local testing. This allows repeatable development without external API cost.

Planned next steps:

- real model integration
- prompt comparison experiments
- benchmark result logging
- tool use
- multi-agent communication experiments
- long-term memory support

## Why This Project

This project explores core ideas behind agentic AI systems:

- task decomposition
- memory-aware execution
- modular agent roles
- evaluation of multi-step outputs

It serves as a foundation for future work in autonomous agents, prompt experimentation, and benchmark-driven evaluation.

## Author

Adham Hamada

USE_LLM = False

def call_llm(prompt):
    if not USE_LLM:
        # smarter simulation
        if "Decompose" in prompt:
            return """1. Choose destination
2. Book transportation
3. Select accommodation
4. Plan itinerary
5. Estimate budget"""

        if "Execute" in prompt:
            return "Step completed successfully with reasonable assumptions."

        if "Evaluate" in prompt:
            return "Score: 8/10 — Output is structured and relevant."

        return "Processed successfully."

    # real API (later)
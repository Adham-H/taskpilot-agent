class ShortMemory:
    def __init__(self, max_size=5):
        self.history = []
        self.max_size = max_size

    def add(self, step, result):
        self.history.append({"step": step, "result": result})
        self.history = self.history[-self.max_size:]

    def get_context(self):
        return self.history
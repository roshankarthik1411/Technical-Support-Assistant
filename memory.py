class ConversationMemory:
    def __init__(self, max_turns=12):
        self.history = []
        self.max_turns = max_turns

    def add(self, role, content):
        self.history.append({"role": role, "content": content})
        if len(self.history) > self.max_turns:
            self.history = self.history[-self.max_turns:]

    def last_user_message(self):
        for msg in reversed(self.history):
            if msg["role"] == "user":
                return msg["content"].lower()
        return ""

    def reset(self):
        self.history = []

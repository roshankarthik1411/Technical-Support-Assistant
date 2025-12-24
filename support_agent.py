from utils.memory import ConversationMemory
from utils.mock_model import MockSupportModel


class TechnicalSupportAgent:
    def __init__(self, system_prompt):
        self.memory = ConversationMemory()
        self.model = MockSupportModel()
        self.memory.add("system", system_prompt)
        self.attempted_fixes = set()

    def chat(self, user_input):
        self.memory.add("user", user_input)

        response = self.model.generate(
            self.memory.last_user_message(),
            self.attempted_fixes
        )

        self.memory.add("assistant", response)
        return response

    def reset(self):
        system_prompt = self.memory.history[0]
        self.memory.reset()
        self.memory.add("system", system_prompt["content"])

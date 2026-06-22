"""
Memory Skill
Allows Nova to recall stored information.
"""

from nova_voice.core.memory import MemoryManager


class MemorySkill:

    def __init__(self):
        self.memory = MemoryManager()

    def handle(self, command: str) -> str:

        command = command.lower()

        if "last project" in command:
            return self.show_last_project()

        if "framework" in command:
            return self.show_framework()

        if "memory" in command:
            return self.show_all_memory()

        return "I don't have that memory yet."

    def show_last_project(self):

        project = self.memory.recall("last_project")

        if project:
            return f"Last project: {project}"

        return "No project saved yet."

    def show_framework(self):

        framework = self.memory.recall(
            "favorite_framework"
        )

        if framework:
            return f"Favorite framework: {framework}"

        return "No framework saved yet."

    def show_all_memory(self):

        memory = self.memory.load_memory()

        if not memory:
            return "Memory is empty."

        result = ["Nova Memory:"]

        for key, value in memory.items():
            result.append(
                f"{key}: {value}"
            )

        return "\n".join(result)
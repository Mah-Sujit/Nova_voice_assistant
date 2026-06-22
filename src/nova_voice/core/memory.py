"""
Memory Manager
Stores and retrieves Nova memory.
"""

import json
from pathlib import Path


class MemoryManager:
    def __init__(self):
        self.memory_file = Path("src/nova_voice/data/memory.json")

    def load_memory(self):
        if not self.memory_file.exists():
            return {}

        with open(self.memory_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_memory(self, data):
        self.memory_file.parent.mkdir(parents=True, exist_ok=True)

        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def remember(self, key, value):
        memory = self.load_memory()
        memory[key] = value
        self.save_memory(memory)

    def recall(self, key):
        memory = self.load_memory()
        return memory.get(key)
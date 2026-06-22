from nova_voice.core.memory import MemoryManager

memory = MemoryManager()

memory.remember("favorite_framework", "FastAPI")

print(memory.recall("favorite_framework"))
"""
AI Chat Skill
Uses local Ollama model for coding help and explanations.
"""

from ollama import chat


class AIChatSkill:
    def __init__(self, model: str = "llama3.2"):
        self.model = model

    def handle(self, command: str) -> str:
        prompt = command.replace("ask ai", "").replace("ai", "").strip()

        if not prompt:
            return "Please provide a question for AI."

        try:
            response = chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Nova, an AI Workspace Manager. "
                            "Help with programming, debugging, testing, "
                            "Git, deployment, and project automation. "
                            "Give clear, practical answers."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )

            return response.message.content

        except Exception as error:
            return f"Ollama AI error: {error}"
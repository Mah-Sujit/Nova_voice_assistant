"""
Project Skill
Creates project structures.
"""

import os


class ProjectSkill:
    def handle(self, command: str):

        if "python project" in command:

            folders = [
                "src",
                "tests",
                "docs"
            ]

            for folder in folders:
                os.makedirs(folder, exist_ok=True)

            return "Python project structure created."

        return "Unknown project command."
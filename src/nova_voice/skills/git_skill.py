"""
Git Skill
Handles Git operations.
"""

import subprocess


class GitSkill:
    def handle(self, command: str):

        if "status" in command:
            result = subprocess.run(
                ["git", "status"],
                capture_output=True,
                text=True
            )
            return result.stdout

        if "commit" in command:
            return "Git commit feature coming soon."

        if "push" in command:
            return "Git push feature coming soon."

        return "Unknown Git command."
"""
Git Skill
Handles safe Git operations for Nova Workspace Manager.
"""

import subprocess


class GitSkill:
    def handle(self, command: str) -> str:
        command = command.lower().strip()

        if "status" in command:
            return self._run(["git", "status"])

        if "log" in command or "commits" in command:
            return self._run(["git", "log", "--oneline", "-5"])

        if "push" in command:
            return self._run(["git", "push"])

        if "add" in command:
            return self._run(["git", "add", "."])

        if "commit" in command:
            message = self._extract_commit_message(command)
            self._run(["git", "add", "."])
            return self._run(["git", "commit", "-m", message])

        return "Unknown Git command."

    def _run(self, command: list[str]) -> str:
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=30
            )

            output = result.stdout if result.stdout else result.stderr
            return output or "Git command completed successfully."

        except subprocess.TimeoutExpired:
            return "Git command timed out."

        except FileNotFoundError:
            return "Git is not installed or not available in PATH."

    def _extract_commit_message(self, command: str) -> str:
        if "message" in command:
            return command.split("message", 1)[1].strip().strip('"')

        if "commit" in command:
            return command.split("commit", 1)[1].strip().strip('"') or "Update project"

        return "Update project"
"""
Terminal Skill
Safely runs allowed terminal commands for Nova Workspace Manager.
"""

import subprocess


class TerminalSkill:
    def __init__(self):
        self.allowed_commands = {
            "git status": ["git", "status"],
            "git log": ["git", "log", "--oneline"],
            "list files": ["ls"],
            "run tests": ["pytest"],
        }

    def handle(self, command: str):
        command = command.lower().strip()

        for phrase, terminal_command in self.allowed_commands.items():
            if phrase in command:
                return self.run_command(terminal_command)

        return "Command not allowed yet."

    def run_command(self, terminal_command):
        try:
            result = subprocess.run(
                terminal_command,
                capture_output=True,
                text=True,
                timeout=30
            )

            output = result.stdout if result.stdout else result.stderr
            return output or "Command completed successfully."

        except subprocess.TimeoutExpired:
            return "Command timed out."

        except FileNotFoundError:
            return "Command not found. Make sure the required tool is installed."
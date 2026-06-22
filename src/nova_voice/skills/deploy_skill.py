"""
Deploy Skill
Provides safe deployment guidance and basic deployment checks.
"""

from pathlib import Path
import subprocess


class DeploySkill:
    def handle(self, command: str) -> str:
        command = command.lower().strip()

        if "check" in command or "ready" in command:
            return self.check_deploy_readiness()

        if "github" in command or "push" in command:
            return self.deploy_to_github()

        return (
            "Deploy command not recognized. Try: "
            "'deploy check' or 'deploy to github'."
        )

    def check_deploy_readiness(self) -> str:
        checks = []

        checks.append(self._check_file("README.md"))
        checks.append(self._check_file("requirements.txt"))
        checks.append(self._check_file(".gitignore"))

        git_status = self._run(["git", "status", "--short"])

        if git_status.strip():
            checks.append("Git: uncommitted changes found.")
        else:
            checks.append("Git: working tree is clean.")

        return "Deployment readiness report:\n" + "\n".join(checks)

    def deploy_to_github(self) -> str:
        status = self._run(["git", "status", "--short"])

        if status.strip():
            return (
                "Cannot deploy yet. You have uncommitted changes.\n"
                "Commit changes before pushing to GitHub."
            )

        return self._run(["git", "push"])

    def _check_file(self, file_name: str) -> str:
        if Path(file_name).exists():
            return f"{file_name}: found."
        return f"{file_name}: missing."

    def _run(self, command: list[str]) -> str:
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.stdout or result.stderr or "Command completed."
        except subprocess.TimeoutExpired:
            return "Command timed out."
        except FileNotFoundError:
            return f"Command not found: {command[0]}"
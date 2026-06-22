"""
Test Runner Skill
Runs project tests and reports results.
"""

import subprocess


class TestRunnerSkill:
    def handle(self, command: str) -> str:
        command = command.lower().strip()

        if "pytest" in command or "test" in command:
            return self.run_pytest()

        return "Unknown test command."

    def run_pytest(self) -> str:
        try:
            result = subprocess.run(
                ["pytest", "-q"],
                capture_output=True,
                text=True,
                timeout=60
            )

            output = result.stdout + result.stderr

            if result.returncode == 0:
                return "All tests passed.\n\n" + output

            return "Tests failed.\n\n" + output

        except subprocess.TimeoutExpired:
            return "Tests timed out."

        except FileNotFoundError:
            return "pytest is not installed. Run: pip install pytest"
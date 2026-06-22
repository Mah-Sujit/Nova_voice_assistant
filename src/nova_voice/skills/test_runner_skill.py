"""
Test Runner Skill
Runs project tests.
"""

import subprocess


class TestRunnerSkill:
    def handle(self, command: str):

        result = subprocess.run(
            ["pytest"],
            capture_output=True,
            text=True
        )

        return result.stdout
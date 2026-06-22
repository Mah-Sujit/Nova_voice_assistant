"""
Intent Router
Routes user commands to the correct skill.
"""

from nova_voice.skills.git_skill import GitSkill
from nova_voice.skills.project_skill import ProjectSkill
from nova_voice.skills.test_runner_skill import TestRunnerSkill
from nova_voice.skills.debug_skill import DebugSkill


class IntentRouter:
    def __init__(self):
        self.git_skill = GitSkill()
        self.project_skill = ProjectSkill()
        self.test_skill = TestRunnerSkill()
        self.debug_skill = DebugSkill()

    def route(self, command: str):
        command = command.lower()

        if "git" in command or "commit" in command or "push" in command or "status" in command:
            return self.git_skill.handle(command)

        elif "create project" in command:
            return self.project_skill.handle(command)

        elif "run tests" in command:
            return self.test_skill.handle(command)

        elif "debug" in command or "error" in command:
            return self.debug_skill.handle(command)

        return "Sorry, I don't understand that command yet."
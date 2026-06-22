"""
Intent Router
Routes user commands to the correct skill.
"""

from nova_voice.skills.git_skill import GitSkill
from nova_voice.skills.project_skill import ProjectSkill
from nova_voice.skills.test_runner_skill import TestRunnerSkill
from nova_voice.skills.debug_skill import DebugSkill
from nova_voice.skills.terminal_skill import TerminalSkill
from nova_voice.skills.code_review_skill import CodeReviewSkill

class IntentRouter:
    def __init__(self):
        self.git_skill = GitSkill()
        self.project_skill = ProjectSkill()
        self.test_skill = TestRunnerSkill()
        self.debug_skill = DebugSkill()
        self.terminal_skill = TerminalSkill()
        self.code_review_skill = CodeReviewSkill()

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
        
        elif "run command" in command or "terminal" in command or "list files" in command:
            return self.terminal_skill.handle(command)
        
        elif "review" in command or "check code" in command or "find bugs" in command:
             return self.code_review_skill.handle(command)
        
        return "Sorry, I don't understand that command yet."
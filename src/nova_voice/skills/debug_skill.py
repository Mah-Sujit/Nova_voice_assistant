"""
Debug Skill
Analyzes common Python errors.
"""


class DebugSkill:
    def handle(self, error_text: str):

        error_text = error_text.lower()

        if "modulenotfounderror" in error_text:
            return "Missing package. Install it with pip."

        if "syntaxerror" in error_text:
            return "Check brackets, quotes, and indentation."

        if "filenotfounderror" in error_text:
            return "The file path does not exist."

        if "permission denied" in error_text:
            return "The process lacks required permissions."
        
        if "syntaxerror" in error_text or "syntax error" in error_text:
            return "Check brackets, quotes, and indentation."

        return f"Unknown error:\n{error_text}"
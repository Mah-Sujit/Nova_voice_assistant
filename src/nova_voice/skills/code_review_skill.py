"""
Code Review Skill
Reviews Python files for basic issues.
"""

from pathlib import Path
import ast


class CodeReviewSkill:
    def handle(self, command: str) -> str:
        file_path = self._extract_file_path(command)

        if not file_path:
            return "Please provide a Python file to review. Example: review src/nova_voice/main.py"

        path = Path(file_path)

        if not path.exists():
            return f"File not found: {file_path}"

        if path.suffix != ".py":
            return "I can currently review only Python .py files."

        code = path.read_text(encoding="utf-8")

        issues = []

        syntax_issue = self._check_syntax(code)
        if syntax_issue:
            issues.append(syntax_issue)

        long_lines = self._check_long_lines(code)
        issues.extend(long_lines)

        todo_comments = self._check_todos(code)
        issues.extend(todo_comments)

        if not issues:
            return f"Code review passed for {file_path}. No basic issues found."

        report = [f"Code review report for {file_path}:"]
        for index, issue in enumerate(issues, start=1):
            report.append(f"{index}. {issue}")

        return "\n".join(report)

    def _extract_file_path(self, command: str) -> str | None:
        words = command.strip().split()

        for word in words:
            if word.endswith(".py"):
                return word

        return None

    def _check_syntax(self, code: str) -> str | None:
        try:
            ast.parse(code)
            return None
        except SyntaxError as error:
            return f"SyntaxError on line {error.lineno}: {error.msg}"

    def _check_long_lines(self, code: str) -> list[str]:
        issues = []

        for line_number, line in enumerate(code.splitlines(), start=1):
            if len(line) > 100:
                issues.append(
                    f"Line {line_number} is too long ({len(line)} characters)."
                )

        return issues

    def _check_todos(self, code: str) -> list[str]:
        issues = []

        for line_number, line in enumerate(code.splitlines(), start=1):
            if "todo" in line.lower():
                issues.append(f"TODO found on line {line_number}.")

        return issues
"""
Debug Skill
Analyzes common Python and terminal errors.
"""


class DebugSkill:

    def handle(self, error_text: str):

        error_text = error_text.lower()

        # Python Errors

        if "modulenotfounderror" in error_text:
            return (
                "ModuleNotFoundError detected.\n"
                "A required package is missing.\n"
                "Try: pip install <package_name>"
            )

        if "filenotfounderror" in error_text:
            return (
                "FileNotFoundError detected.\n"
                "The file path does not exist.\n"
                "Check the path and filename."
            )

        if "permissionerror" in error_text:
            return (
                "PermissionError detected.\n"
                "The program does not have permission "
                "to access the file or folder."
            )

        if "syntaxerror" in error_text or "syntax error" in error_text:
            return (
                "SyntaxError detected.\n"
                "Check brackets, quotes, commas, "
                "and indentation."
            )

        if "importerror" in error_text:
            return (
                "ImportError detected.\n"
                "Verify the module exists and "
                "the import statement is correct."
            )

        if "keyerror" in error_text:
            return (
                "KeyError detected.\n"
                "The dictionary key does not exist."
            )

        if "indexerror" in error_text:
            return (
                "IndexError detected.\n"
                "The list index is out of range."
            )

        if "typeerror" in error_text:
            return (
                "TypeError detected.\n"
                "An operation received an invalid type."
            )

        if "valueerror" in error_text:
            return (
                "ValueError detected.\n"
                "A function received an invalid value."
            )

        return (
            "Unknown error.\n"
            "Future AI analysis module will inspect "
            "the full traceback."
        )
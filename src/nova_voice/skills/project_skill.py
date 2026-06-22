"""
Project Skill
Creates starter project structures.
"""

from pathlib import Path


class ProjectSkill:

    def handle(self, command: str) -> str:

        command = command.lower()

        if "fastapi" in command:
            return self.create_fastapi_project()

        if "python project" in command:
            return self.create_python_project()

        return "Unknown project command."

    def create_python_project(self) -> str:

        project_name = "python_project"

        structure = [
            f"{project_name}/src",
            f"{project_name}/tests",
            f"{project_name}/docs",
        ]

        for folder in structure:
            Path(folder).mkdir(parents=True, exist_ok=True)

        Path(f"{project_name}/README.md").touch()
        Path(f"{project_name}/requirements.txt").touch()
        Path(f"{project_name}/.gitignore").touch()

        return f"Python project '{project_name}' created successfully."

    def create_fastapi_project(self) -> str:

        project_name = "fastapi_project"

        structure = [
            f"{project_name}/app",
            f"{project_name}/tests",
        ]

        for folder in structure:
            Path(folder).mkdir(parents=True, exist_ok=True)

        main_file = Path(f"{project_name}/app/main.py")

        main_file.write_text(
            """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Nova FastAPI Project"}
"""
        )

        Path(f"{project_name}/requirements.txt").write_text(
            "fastapi\nuvicorn\n"
        )

        Path(f"{project_name}/README.md").touch()

        return f"FastAPI project '{project_name}' created successfully."
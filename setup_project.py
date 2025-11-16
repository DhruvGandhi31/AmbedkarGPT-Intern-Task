# Just a normal script to set up the project structure.
import os

folders = [
    "src",
    "src/rag",
    "src/utils"
]

files = {
    "src": ["main.py", "config.py"],
    "src/rag": ["__init__.py", "loader.py", "splitter.py", "vectorstore.py", "qa.py"]
}

def create_folders():
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

def create_files():
    for folder, filenames in files.items():
        for filename in filenames:
            filepath = os.path.join(folder, filename)
            if not os.path.exists(filepath):
                with open(filepath, 'w') as f:
                    f.write("# Initial file: " + filename)

def setup_project_structure():
    create_folders()
    create_files()
    print("Project structure created successfully!")

setup_project_structure()

from src.flask_gen.generator import Generator
from src.flask_gen.structs import base
from pathlib import Path

def main():
    PROJECT_NAME = "example_project"
    PROJECT_DIR = Path(__file__).parent.resolve().joinpath(PROJECT_NAME)
    
    generator = Generator()
    generator.root_dir = PROJECT_DIR
    generator.load(base.struct)
    generator.generate()

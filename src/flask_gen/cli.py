from src.flask_gen.generator import Generator
from src.flask_gen.structs import base
from pathlib import Path
import argparse
from . logger import logger
from . config import VERSION


def main():
    logger.debug(f'flask-gen v{VERSION} - generates a producation ready microservice')
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name', type=str, help='the project name which will be generated')

    args = parser.parse_args()

    project_name = args.project_name
    project_dir = Path(__file__).parent.resolve().joinpath(project_name)

    generator = Generator()
    generator.root_dir = project_dir
    generator.load(base.struct)
    generator.generate()

from setuptools import setup, find_packages

from clean_folder.clean_folder.clean_folder import get_main_path, around_dir 
setup(
    name="clean_folder",
    version='1.0',
    entry_points = {
        "console_scripts" : ["clean_folder = clean_folder.clean_folder:main"],
    },
    packages=find_packages(),
    description="Clean folder script",
)

def main():
    main_path = get_main_path()
    around_dir(main_path)  
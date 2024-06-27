from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."  # in requirements.txt used to activate\run setup.py
def get_requirements(file_path:str)->List[str]:
    '''
    this function return the list of requirements without remove "-e ."
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()

__version__ = "1.0"

REPO_NAME = "TextSummarizerProject"
AUTHOR_USER_NAME = "BharatSingh Rajpurohit"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "bsraigur@gmail.com"

setup(
    name=SRC_REPO,   # project_name in template should be same 
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    #long_description=long_description,
    long_description_content="text/markdown",
    install_requires=get_requirements("requirements.txt"),
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
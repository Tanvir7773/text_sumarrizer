import setuptools
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0" 
REPO_NAME = "text_summarizer"
AUTHOR_NAME = "TANVIR SHEKHAWAT"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "tanushekhawat0801@gmail.com"
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
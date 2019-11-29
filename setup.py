from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    name="clicker",
    version="0.0.1",
    author="James Fitzgerald",
    author_email="mail@james.wf",
    description="Simple GUI automation tool to send clicks if a specified pixel matches a specified color.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Jawfish/clicker",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: Unlicense",
    ],
)
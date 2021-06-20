import setuptools
import re

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirement_list = [r.strip() for r in open("requirements.txt", "r").readlines() if r]
project_dir = "lico_main"


def get_attribute(attr, project):
    result = re.search(
        r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(attr),
        open(project + "/__version.py").read(),
    )
    return result.group(1)


setuptools.setup(
    name="lico_main",
    version=get_attribute("__version__", project_dir),
    install_requires=requirement_list,
    author="Deepanshu Dhruw",
    author_email="dhruwxl@gmail.com",
    description="A cli to get lines-of-code for every language of a repo.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["lico=lico_main:main"]},
    url="https://github.com/devblin/lico",
    classifiers=[
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    packages=[project_dir],
)

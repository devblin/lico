import setuptools
import re
from lico_main import __version__, __original_name__, __test_name__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirement_list = [r.strip() for r in open("requirements.txt", "r").readlines() if r]
project_dir = "lico_main"

setuptools.setup(
    name=__test_name__,
    version=__version__,
    install_requires=requirement_list,
    author="Deepanshu Dhruw",
    author_email="dhruwxl@gmail.com",
    description="A cli to get lines-of-code for every language of your github repo.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["lico=lico_main.__main__:main"]},
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

from __future__ import absolute_import
import os
import sys
import argparse as ap
from . import progress
from . import __description__
import aiohttp
import asyncio

GITHUB_REPO_URL = "https://api.github.com/users/devblin/repos"
LOC_API = "https://api.codetabs.com/v1/loc/?github=username/reponame"


def main():
    print(__description__)

#! /bin/bash
rm -rf lico_main/__pycache__
rm -rf build
rm -rf lico_devblin.egg-info
rm -rf dist
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --user --upgrade twine
python3 -m twine upload --repository testpypi dist/*
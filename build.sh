#! /bin/bash
rm -rf lico_main/__pycache__
rm -rf build
rm -rf lico.egg-info
rm -rf dist
echo "UPGRADING BUILD..."
python3 -m pip install --upgrade build
echo "RUNNING BUILD..."
python3 -m build
echo "INSTALLING AND UPGRADING TWINE..."
python3 -m pip install --user --upgrade twine
echo "UPLOADING IN PYPI..."
python3 -m twine upload dist/*
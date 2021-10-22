py -m pip install --upgrade pip setuptools wheel
py -m build --wheel
py -m pip install --force-reinstall .\dist\cd4db-1.0.0-py3-none-any.whl

# J's LS

This repo contains my custom implementation of the UNIX system command *ls*
done in python

### How to build

```shell script
python3 setup.py sdist bdist_wheel

python3 -m twine upload --repository testpypi dist/*

```

### How to install

```
python3 -m pip install --upgrade --index-url https://test.pypi.org/simple/ --no-deps jls
```
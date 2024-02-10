# Hackalytics 2024 Project

## Quickstart
This repo uses `poetry` to manage dependences, so you have to install it:
```bash
curl -sSL https://install.python-poetry.org | python3 - 
```
And add this to your Path: `/Users/<user>/.local/bin/poetry`, where <user> should be replaced with the output of `whoami`
This line should be added to `.zshrc` for ZSH (default for Apple silicon MacOs) or `.bashrc`,
which is located in the home directory. 

For example, do
```bash
echo 'export PATH="/Users/bricey/.local/bin/poetry"' >> ~/.zshrc
```

And then run `poetry install`.
To test, run `poetry run python clickbuzz/__init__.py`

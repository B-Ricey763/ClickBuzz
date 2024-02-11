# ClickBUZZ – Hackalytics 2024 Project

## About 
##Say goodbye to guesswork and hello to precision with ClickBuzz!
Introducing our cutting-edge AI machine learning model designed to revolutionize content optimization: harness the power of data-driven decision-making with our innovative platform.
Our AI model analyzes user engagement metrics and provides insights into the effectiveness of your content.
For the perfectly tailored video title that ensures every piece of content resonates with your audience, our AI empowers you to change the way you A|B test, leaving more time to create exciting content and connect with your audience.

## Technologies Used
Frontend - Taipy
TODO

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

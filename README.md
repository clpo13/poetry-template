# poetry-template

Template for Python CLI projects built with [Poetry](https://python-poetry.org).

Included dependencies:

* [Click](https://click.palletsprojects.com/en/7.x/)
* [Black](https://black.readthedocs.io/en/stable/)
* [isort](https://pycqa.github.io/isort/)
* [Flake8](https://flake8.pycqa.org/en/latest/)
* [pytest](https://docs.pytest.org/en/stable/)

## Usage

Install Poetry with
`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
(recommended), `pipx install poetry` (using [pipx](https://pipxproject.github.io/pipx/)),
or `pip install --user poetry`.

Then fork this repository (or [generate a new one](https://github.com/clpo13/poetry-template/generate)
from it) and:

```bash
git clone https://github.com/<username>/poetry-template
cd poetry-template
poetry install
```

Dependencies can be added and removed with `poetry add [--dev] <name>` / `poetry remove [--dev] <name>`
and updated with `poetry update`.

Now you can:

* format code with Black: `poetry run black .`
* sort imports with isort: `poetry run isort .`
* check for style and code errors with Flake8: `poetry run flake8`
* run tests with pytest: `poetry run pytest`
* run an example script: `poetry run hello --help`

A Python sdist and wheel can be built with `poetry build` and published with `poetry publish`
(though be sure to update `pyproject.toml` first).

## License

This template is released into the public domain according to the terms of The Unlicense. Do
whatever you like with it.

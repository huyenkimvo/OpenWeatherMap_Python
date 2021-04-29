# Search Tests
# Using Selenium Pytest-bdd

## Installation

- **Programming language**: This project requires an up-to-date version of [Python 3](https://www.python.org/downloads/). Currently: Python 3.9.4
- **IDE**: [Visual Studio Code](https://code.visualstudio.com/download)
- **Extensions**: Python, Cucumber (Gherkin) Full Support, Pytest IntelliSense

## VS Code configuration

- Add 2 files ***launch.json*** and ***settings.json*** to ***.vscode***

   ```json
    // launch.json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "pytest-bdd",
                "type": "python",
                "request": "launch",
                "stopOnEntry": false,
                "module": "pytest",
                "args": [
                    "-sv"
                ],
                "cwd": "${workspaceRoot}"
            }
        ]
    }
   ```

   ```json
    // settings.json
    {
        "cucumberautocomplete.steps": [
            "weather/tests/steps/*.py"
        ],
        "cucumberautocomplete.syncfeatures": "weather/tests/features/*feature",
        "cucumberautocomplete.strictGherkinCompletion": true,
        "cucumberautocomplete.strictGherkinValidation": true,
        "cucumberautocomplete.smartSnippets": true,
        "cucumberautocomplete.stepsInvariants": true,
        "cucumberautocomplete.customParameters": [
            {
                "parameter": "{ab}",
                "value": "(a|b)"
            }
        ],
        "cucumberautocomplete.skipDocStringsFormat": true,
        "cucumberautocomplete.onTypeFormat": true,
        "cucumberautocomplete.gherkinDefinitionPart": "(Given|When|Then)\\(parsers.parse\\(",
        "cucumberautocomplete.stepRegExSymbol": "'",
        "editor.quickSuggestions": {
            "comments": false,
            "strings": true,
            "other": true
        },
        "pytest.command": "pipenv run pytest",
        "python.testing.pytestArgs": [
            "weather/tests/steps"
        ],
        "python.testing.unittestEnabled": false,
        "python.testing.nosetestsEnabled": false,
        "python.testing.pytestEnabled": true,
        "python.pythonPath": "${workspaceFolder}/.venv", // Path to the Python interpreter
        "python.linting.enabled": true
    }
   ```

## Setup

1. Make sure existing python the same as version in Pipfile file.
2. Use [Pipenv](https://pipenv.pypa.io) to set up a virtual environment to manage packages
   - Run ***py -m pip install pipenv*** from the command line in the project's root directory
   - At the left corner: select virtual env that created. Example: Python 3.9.4 64-bit ('WeatherMap-dEG8rr8W).
   - Run ***py -m pipenv install*** from the command line

## Running Tests

- Run ***py -m pipenv run python -m pytest*** from the command line
- To run tests in parallel, use the ***-n*** option with a number of processes
- To run tests by tags, use the ***-m*** option with the tag's names
- To generate HTML reports, add the ***--html=report.html*** option
- Example combined options: ***py -m pipenv run python -m pytest -n 1 -m search --html=report.html***

# conversation-assistant

Generates message suggestions for a user to respond with based upon their conversation history, and some context parameters.

Can generate suggestions in any language, within any context.

## How it works (high level)

1. GenerateSuggestionsRequest comes in, includes conversation history and context parameters

2. Detects language of the conversation

3. Uses the context parameters to generate a 'prompt' in English

4. Prompt is translated to the detected language. This ensures that GPT3's message suggestion will be in the detected language.

5. Conversation is appended to the prompt

6. [GPT3 Completion response](https://beta.openai.com/docs/guides/completion) returns a 'completion' that includes the probable next message for the conversation. This is the 'suggestion'.

7. The suggestion is extracted and returned in the GenerateSuggestionsResponse

## Environment setup

Install [pipenv](https://pypi.org/project/pipenv/) to manage your virtual environment and dependencies

```
pip3 install pipenv
```

Add a `.env` file to the root of this project and paste in the following contents:

```
# For access to GPT3
OPENAI_API_KEY=<your API key>

# For access to Google Translate API
GOOGLE_APPLICATION_CREDENTIALS=<path to credentials file>

# Keep virtual environment inside the project folder
PIPENV_VENV_IN_PROJECT=true
PIPENV_IGNORE_VIRTUALENVS=1
```

## Install

Install dependencies:

```
pipenv run install-dev
```

# Test

Run unit tests:

```
pipenv run test
```

Run E2E tests:

```
pipenv run teste2e
```

## Checks

Format files:

```
pipenv run format
```

Lint files:

```
pipenv run lint
```

Perform type-checking on files:

```
pipenv run check-types
```

## Deploy locally

You can deploy the function locally with `flask` by running:

```
pipenv run start
```

Then use `Postman` to make a POST request to `http://localhost:8081/`. Your request body must be JSON that matches the schema in `schemas/generate_suggestions_request.json`. Sample request bodies can be found in `e2e/mock_requests`.

To enable debug mode, use this `launch.json` config:

```
    {
      "name": "Python: Flask",
      "type": "python",
      "request": "launch",
      "module": "flask",
      "env": {
        "FLASK_APP": "app.py",
        "FLASK_ENV": "development",
        "FLASK_DEBUG": "0"
      },
      "args": ["run", "--port", "8081", "--no-debugger", "--no-reload"],
      "jinja": true
    }
```

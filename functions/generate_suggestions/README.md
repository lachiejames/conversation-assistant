# Function: generate_suggestions

Generates message suggestions for a user to respond with based upon their conversation history, and some context parameters.

Can generate suggestions in any language, within any context.

## How it works (high level)

1. GenerateSuggestionsRequest comes in, includes conversation history and context parameters

2. Detects language of the conversation

3. Uses the context parameters to generate a 'prompt' in English

4. Prompt is translated to the detected language. This ensures that GPT3's message suggestion will also be in the detected language.

5. Conversation history is appended to the prompt

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

## VSCode settings

To debug the function locally, use this `launch.json` config:

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

To debug tests locally with [Test Explorer](littlefoxteam.vscode-python-test-adapter), use this `settings.json` config:

```
{
  "python.testing.pytestArgs": ["generate_suggestions", "e2e"],
  "python.testing.pytestEnabled": true,
  "python.formatting.provider": "black",
}
```

# AaAaAa

I'm thinking of 2 different things.

1. An extra fine-tune option for saying what key points need to be addressed in the message

2. An extra panel for rephrasing a message, which doesn't involve adding previous messages

But do I need 2 different screens for this?

Things to consider:

- How likely are each of these things to be used?

  - A fine-tune option seems important because the suggestions don't know what the answer is going to be.  E.g. if the messages say "hey bro, wanna come out?" the suggestions will randomly say yes/no/other, which is annoying because you have to just cycle through them until you get something remotely similar to what you want.  So yes this seems important.

  - A panel seems useful too because you don't always want to add a bunch of messages to get a suggestion for what to say.  E.g. 'hey what's up' along with 'friends', 'flirty' could be rephrased as 'hey gorgeous'

So it seems like both of these things are useful.  But should they exist as 2 separate things?

I'm thinking they shouldn't because it's just an extra fine-tuning step when generating a suggestion really.  It's useful to be able to rephrase something without adding messages though, and you often won't have to if it's like that example before.

So what's the outcome?

These 2 things should be combined as 1

But how should it be implemented?

# solution 1 - Extra fine-tuning input

Same number of panels, fine-tuning panel has an extra input called 'message to rephrase'

You still generate a suggestion as normal

This seems like the easiest way to implement, but it's going to be a bit confusing.  How do people understand that there is an extra rephrase capability for this app?

Should there be a button next to this text box so that it can generate a rephrase using the inputs on the fine-tuning page?

Should I have an extra set of tutorials for rephrasing?

# solution 2 - Extra panel

Rephrase panel has a 'message to rephrase' input.  But shouldn't the fine-tuning inputs be here as well?  I don't want to have to duplicate them.

# Solution 3 - Extra suggestion button

There could be a rephrase button in addition to the generate suggestions button

Should there be a CTA on one of these pages that enables rephrase capabilities?  argh, I need a coffee and a cone.

## I'm thinking option 1

Message to rephrase is another input on the fine-tune window

There are no extra buttons

When message to rephrase is populated, it shows up as the last 'my message' on the message list

It has to look different somehow, so that it's obvious that it's going to be rephrased.


# Askky Python Client

[![PyPI Version](https://img.shields.io/pypi/v/askky.svg)](https://pypi.org/project/askky/) [![PyPI](https://img.shields.io/pypi/pyversions/askky.svg)]() [![License](https://img.shields.io/:license-mit-blue.svg)](https://opensource.org/licenses/MIT)

Python bindings for interacting with Askky API

This is primarily meant for clients who wish to perform interactions with the Askky API programatically.

## Installation

```sh
$ pip install askky
```

## Usage
Get your Private Api key from <http://app.askky.co/account/>.

```py
from askky.client import Client
client = askky.Client("<YOUR_API_KEY>")
```
## Trigger Form

After setting up client, you need to trigger your concerned survey/campaign/form :

```py
client.trigger_survey(survey_id="<YOUR_SURVEY_ID>",user_id=[<"List of userIds you want to trigger the survey for">])
```

Example:

```py
client.trigger_survey(survey_id="abc",user_id=["123","1234"])
```



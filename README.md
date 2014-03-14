Hellosign Python SDK
-------------------
[![Build Status](https://travis-ci.org/minhdanh/hellosign-python-sdk.png?branch=master)](https://travis-ci.org/minhdanh/hellosign-python-sdk)
[![Coverage Status](https://coveralls.io/repos/minhdanh/hellosign-python-sdk/badge.png)](https://coveralls.io/r/minhdanh/hellosign-python-sdk)
[![Code Health](http://landscape.io/github/minhdanh/hellosign-python-sdk/master/landscape.png)](http://landscape.io/github/minhdanh/hellosign-python-sdk/master)
[![Latest Version](https://pypip.in/v/hellosign-python-sdk/badge.png)](https://pypi.python.org/pypi/hellosign-python-sdk/)
[![Downloads](https://pypip.in/d/hellosign-python-sdk/badge.png)](https://pypi.python.org/pypi/hellosign-python-sdk/)
[![Dependency Status](https://gemnasium.com/minhdanh/hellosign-python-sdk.png)](https://gemnasium.com/minhdanh/hellosign-python-sdk)



An API wrapper written in Python to interact with HelloSign's API (http://www.hellosign.com)

Note: This is not the final Readme, and the package is not ready yet. It will be ready when it's ready (of course).

## Installation

Install using `easy_install`:

````sh
easy_install hellosign-python-sdk
````

Install using `pip`:

````sh
pip install hellosign-python-sdk
````

## Configuration

In your application, import `HSClient`:

````python
from hsclient import HSClient
````

Then create a HSClient object and pass authentication information to initialize it:

````python
# Initialize HSClient using email and password
client = HSClient(api_email="api_user@example.com", api_password="your_password")

# Initialize HSClient using api key
client = HSClient(api_key="your_api_key")

# Initialize HSClient using api token

client = HSClient(api_accesstoken="your_api_access_token", api_accesstokentype="your_api_access_token_type")
````
Note: In case you initialize the HSClient with all the above credentials, the priority order is as follow: api_accesstoken & api_accesstokentype, api_key, then api_email and api_password

## Usage

### Account

#### Get current account information

````python
client.get_account_info()
````
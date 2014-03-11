Hellosign Python SDK
-------------------
[![Build Status](https://travis-ci.org/minhdanh/hellosign-python-sdk.png?branch=master)](https://travis-ci.org/minhdanh/hellosign-python-sdk)

An API wrapper written in Python to interact with HelloSign's API (http://www.hellosign.com)

Note: This is not the final Readme, and the package is not ready.

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
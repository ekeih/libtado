# Tado python library

A library to control your Tado Smart Thermostat. This repository contains an actual library in `libtado/api.py` and a proof of concept command line client in `libtado/__main__.py`.

**The tested version of APIs is Tado v2.**

## Installation

You can download officiel library with `pip install libtado`.

But ifyou want to benefits with improvements for API v2 you will need to download this library.

```sh
git clone https://github.com/germainlefebvre4/libtado.git
```

Please check out https://libtado.readthedocs.io for more documentation.

## Preparation

Retrieve your `CLIENT_SECRET` before running the script otherwise you will get a `401 Unauthorized Access`.

To get your `CLIENT_SECRET` enable the Developper Mode when logging in and catch the Headers. You will find the form data like this :
```
client_id: tado-web-app
client_secret: fndskjnjzkefjNFRNkfKJRNFKRENkjnrek
grant_type: password
password: MyBeautifulPassword
scope: home.user
username: email@example.com
```

Then you just have to get the value in the attribute `client_secret`. You will need it to connect to your account through Tado APIs. The `client_secret` never dies so you can base your script on it.

*Your `CLIENT_SECRET` must keep secret.*

## Usage

Download the repository. You can work inside it. Beware the examples considere they can acces to the file `./libtado/api.py`.

Now you can call it in your Pyhton script !

```python
import libtado.api

t = api.Tado('my@email.com', 'myPassword', 'client_secret')

print(t.get_me())
print(t.get_home())
print(t.get_zones())
print(t.get_state(1))
```

## Examples

An script example is provided in the repository as `example.py`.
It show you haw to use the library and expose some structured responses.


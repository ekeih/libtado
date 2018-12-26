# libtado

A library to control your Tado Smart Thermostat. This repository contains an actual library in `libtado/api.py` and a proof of concept command line client in `libtado/__main__.py`.


## Installation

This will install the official library and the command line client:

```
$ pip install libtado
```

and this will install THIS library for local usage

```sh
$ git clone https://github.com/germainlefebvre4/libtado.git
```

Please check out https://libtado.readthedocs.io for more documentation.

## Usage

Copy the library directory in your workdir.

Now you can call it in your Pyhton script !

```python
import api

t = api.Tado('my@email.com', 'myPassword')
print(t.get_me())
print(t.get_home())
print(t.get_zones())
print(t.get_state(1))
```

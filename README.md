# libtado

A library to control your Tado Smart Thermostat. This repository contains an actual library in `libtado/api.py` and a proof of concept command line client in `libtado/__main__.py`.

## Installation

This will install the library and the command line client:

```
$ git clone git@github.com:ekeih/libtado.git
$ pip install .
$ tado -u 'USERNAME' -p 'PASSWORD' whoami
```

## Features

### Command Line Client

```
Usage: tado [OPTIONS] COMMAND [ARGS]...

  This script provides a command line client for the Tado API.

  You can use the environment variables TADO_USERNAME and TADO_PASSWORD
  instead of the command line options.

  Call 'tado COMMAND --help' to see available options for subcommands.

Options:
  -u, --username TEXT  Tado username  [required]
  -p, --password TEXT  Tado password  [required]
  -h, --help           Show this message and exit.

Commands:
  capabilities        Display the capabilities of a zone.
  devices             Display all devices.
  early_start         Display or change the early start feature of a zone.
  end_manual_control  End manual control of a zone.
  home                Display information about your home.
  mobile              Display all mobile devices.
  set_temperature     Set the desired temperature of a zone.
  users               Display all users of your home.
  whoami              Tell me who the Tado API thinks I am.
  zone                Get the current state of a zone.
  zones               Get configuration information about all zones.
```

### API

ToDo: Replace with feature list.

# libtado

A library to control your Tado Smart Thermostat. This repository contains an actual library in `libtado/api.py` and a proof of concept command line client in `libtado/__main__.py`.

## Installation

This will install the library and the command line client:

```
$ git clone git@github.com:ekeih/libtado.git
$ pip install .
$ tado -u 'USERNAME' -p 'PASSWORD' whoami
```

## Usage

### Command Line Client

Just run `tado` in your terminal and read the help output or take a look at the feature section of this README.

#### Credentials

If you do not want to use `--username` and `--password` everytime you can define some environment variables.

```
export TADO_USERNAME='USERNAME'
export TADO_PASSWORD='PASSWORD'
tado whoami
```

### API

```
import tado.api
t = tado.api('Username', 'Password')
print(t.get_me())
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

## License

```
Copyright (C) 2017  Max Rosin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```

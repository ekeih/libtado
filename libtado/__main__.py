#! /usr/bin/env python

import click
import libtado.api

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--username', '-u', required=True, envvar='TADO_USERNAME', help='Tado username')
@click.option('--password', '-p', required=True, envvar='TADO_PASSWORD', help='Tado password')
@click.pass_context
def main(ctx, username, password):
  """
  This script provides a command line client for the Tado API.

  You can use the environment variables TADO_USERNAME and TADO_PASSWORD
  instead of the command line options.

  Call 'tado COMMAND --help' to see available options for subcommands.
  """
  ctx.obj = libtado.api.Tado(username, password)

@main.command(help='Tell me who the Tado API thinks I am.')
@click.pass_obj
def whoami(tado):
  click.echo(tado.get_me())

@main.command(help='Get all zones.')
@click.pass_obj
def zones(tado):
  zones = tado.get_zones()
  for zone in zones:
    click.secho('%s (ID: %s)' % (zone['name'], zone['id']), fg='green', bg='black')
    click.echo('Created: %s' % zone['dateCreated'])
    click.echo('Type: %s' % zone['type'])
    click.echo('Device Types: %s' % ', '.join(zone['deviceTypes']))
    click.echo('Devices: %i' % len(zone['devices']))
    click.echo('Dazzle: %s' % zone['dazzleEnabled'])

@main.command(help='Get all devices.')
@click.pass_obj
def devices(tado):
  devices = tado.get_devices()
  for d in devices:
    if d['deviceType'] == 'GW03':
      click.echo('Serial: %s' % d['serialNo'])
      click.echo('Type: %s' % d['deviceType'])
      click.echo('Firmware: %s' % d['currentFwVersion'])
      click.echo('Operation: %s' % d['gatewayOperation'])
      click.echo('Connection: %s (%s)' % (d['connectionState']['value'], d['connectionState']['timestamp']))
    elif d['deviceType'] == 'VA01':
      click.echo('Serial: %s' % d['serialNo'])
      click.echo('Type: %s' % d['deviceType'])
      click.echo('Firmware: %s' % d['currentFwVersion'])
      click.echo('Connection: %s (%s)' % (d['connectionState']['value'], d['connectionState']['timestamp']))
      click.echo('Mounted: %s (%s)' % (d['mountingState']['value'], d['mountingState']['timestamp']))
    else:
      click.secho('Device type %s not supported. Please report a bug with the following output.' % d['deviceType'], fg='black', bg='red')
      d['serialNo'] = 'XXX'
      d['shortSerialNo'] = 'XXX'
      click.echo(d)
    click.echo('')

@main.command(help='Set the temperature for a zone')
@click.option('--zone', '-z', required=True, type=int, help='Zone ID')
@click.option('--temperature', '-t', required=True, type=int, help='Temperature')
@click.option('--termination', '-x', default='MANUAL', help='Termination settings')
@click.pass_obj
def set_temperature(tado, zone, temperature, termination):
  tado.set_temperature(zone, temperature, termination=termination)

@main.command(help='End manual control.')
@click.option('--zone', '-z', required=True, type=int, help='Zone ID')
@click.pass_obj
def end_manual_control(tado, zone):
  tado.end_manual_control(zone)

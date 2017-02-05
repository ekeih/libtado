import json
import requests

class Tado:
  headers        = { 'Referer' : 'https://my.tado.com/' }
  access_headers = headers
  api            = 'https://my.tado.com/api/v2'

  def __init__(self, username, password):
    self.username = username
    self.password = password
    self._login()
    self.id = self.getMe()['homes'][0]['id']

  def _login(self):
    url='https://my.tado.com/oauth/token'
    data = { 'client_id'  : 'tado-webapp',
             'grant_type' : 'password',
             'password'   : self.password,
             'scope'      : 'home.user',
             'username'   : self.username }
    request = requests.post(url, data=data, headers=self.access_headers)
    response = request.json()
    self.access_token = response['access_token']
    self.refresh_token = response['refresh_token']
    self.access_headers['Authorization'] = 'Bearer ' + response['access_token']

  def _apiCall(self, cmd):
    url = '%s/%s' % (self.api, cmd)
    request = requests.get(url, headers=self.access_headers)
    response = request.json()
    return response

  def refreshAuth(self):
    url='https://my.tado.com/oauth/token'
    data = { 'client_id'     : 'tado-webapp',
             'grant_type'    : 'refresh_token',
             'refresh_token' : self.refresh_token,
             'scope'         : 'home.user'
           }
    request = requests.post(url, data=data, headers=self.headers)
    response = request.json()
    self.access_token = response['access_token']
    self.refresh_token = response['refresh_token']
    self.access_headers['Authorization'] = 'Bearer ' + self.access_token

  def getCapabilities(self, zone):
    data = self._apiCall('homes/%i/zones/%i/capabilities' % (self.id, zone))
    return data

  def getDevices(self):
    data = self._apiCall('homes/%i/devices' % self.id)
    return data

  def getHome(self):
    data = self._apiCall('homes/%i' % self.id)
    return data

  def getInstallations(self):
    data = self._apiCall('homes/%i/installations' % self.id)
    return data

  def getMe(self):
    data = self._apiCall('me')
    return data

  def getMobileDevices(self):
    data = self._apiCall('homes/%i/mobileDevices' % self.id)
    return data

  def getSchedule(self, zone):
    data = self._apiCall('homes/%i/zones/%i/schedule/activeTimetable' % (self.id, zone))
    return data

  def getState(self, zone):
    data = self._apiCall('homes/%i/zones/%i/state' % (self.id, zone))
    return data

  def getWeather(self):
    data = self._apiCall('homes/%i/weather' % self.id)
    return data

  def getZones(self):
    data = self._apiCall('homes/%i/zones' % self.id)
    return data

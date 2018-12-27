from libtado.api import Tado

t = Tado('my@email.com', 'myPassword', 'client_secret')

print(t.get_me())

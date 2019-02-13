from libtado.api import Tado

t = Tado('my@email.com', 'myPassword', 'client_secret')

print(t.get_me())
print(t.get_home())
print(t.get_zones())
print(t.get_state(1))

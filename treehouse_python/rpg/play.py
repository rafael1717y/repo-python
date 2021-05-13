from thieves import Thief
from characters import Character
kenneth = Thief(name="Kenneth", sneaky=False)
print(kenneth.sneaky)
print(kenneth.agile)
print(kenneth.hide(8))

print(issubclass(Thief, Character))

kenneth2 = Thief(name="Kenneth2")
print(kenneth2)
print(type(kenneth2))
print(kenneth.__class__)
print(kenneth.__class__.__name__)
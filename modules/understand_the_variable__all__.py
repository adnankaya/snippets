from foo import *

print(bar)
print(baz)
print(waz)

"""output
<function bar at 0x7fb5fba07940>
46
Traceback (most recent call last):
  File "understand_the_variable__all__.py", line 5, in <module>
    print(waz)
NameError: name 'waz' is not defined
"""
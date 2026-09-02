'''
Q) Why do we need raise <Exception Name>
--> In order to catch the Business logic kind of error.

Raise se code flow break hoga.

but  agar try ke andar likha to handle hoga.

'''


try:
    age = -10
    raise ValueError("Hello")
except ValueError:
    print("Age can't be negative")


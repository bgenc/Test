__author__ = 'bgenc'

plain = raw_input("Enter plain text: ")

a = ord("a")
z = ord("z")
A = ord("A")
Z = ord("Z")

for shift in range(z - a):
    cipher = ""

    for letter in plain:
        code = ord(letter)
        if code >= a and code <= z:
            code = a + (code - a + shift) % (z - a + 1)
        elif code >= A and code <= Z:
            code = A + (code - A + shift) % (Z - A + 1)
        cipher += chr(code)

    print shift, ":", cipher
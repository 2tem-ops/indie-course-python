from string import ascii_lowercase
print(alphabet := {letter: num for num, letter in enumerate(ascii_lowercase, start=1)})
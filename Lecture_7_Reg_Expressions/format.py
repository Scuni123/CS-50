import re

name = input("What's your name? ").strip()
matches = re.search(r"^([a-zA-Z]+), ?([a-zA-Z]+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
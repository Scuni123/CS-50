#List have [] while dict have {}
students = [
    {"name": "Hermione", "House" : "Gryff", "Patronus" : "Otter"},
    {"name": "Harry", "House": "Gryff", "Patronus" : "Stag"},
    {"name": "Ron", "House": "Gryff", "Patronus": "Jack Russell"},
    {"name": "Draco", "House": "Slytherin", "Patronus": None}
]
for s in students:
    print(s["name"], s["House"], s["Patronus"], sep=" : ")
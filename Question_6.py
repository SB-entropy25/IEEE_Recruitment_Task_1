#Cutoff List (Tuple Format), tupples are immutable whereas dictonary and lists are mutable and LISTS can conatin tupples
a=[
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 247),
    ("Pilani", "Eco", 271),
    ("Pilani", "Bio", 236),
    ("Goa", "CS", 301),
    ("Goa", "Chemical", 239),
    ("Goa", "Eco", 263),
    ("Goa", "Bio", 234),
    ("Hyderabad", "CS", 298),
    ("Hyderabad", "Chemical", 238),
    ("Hyderabad", "Eco", 261),
    ("Hyderabad", "Bio", 234),
]
#Cutoff List (Dictionary Format)
b={
    "Pilani": {
        "CS": 327,
        "Chemical": 247,
        "Eco": 271,
        "Bio": 236
    },
    "Goa": {
        "CS": 301,
        "Chemical": 239,
        "Eco": 263,
        "Bio": 234
    },
    "Hyderabad": {
        "CS": 298,
        "Chemical": 238,
        "Eco": 261,
        "Bio": 234
    }
}
print(a)

print(b)

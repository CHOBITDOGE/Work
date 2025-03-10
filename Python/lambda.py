people = [
    {"name":"Harry","mentor": "Tyloo"},
    {"name":"Zywoo","mentor": "Fish"},
    {"name":"Ana","mentor":"Venture"}
]

def f(person):
    return person["mentor"]
people.sort(key=f)  

print(people)

people.sort(key=lambda person: person["mentor"])

print(people)
       
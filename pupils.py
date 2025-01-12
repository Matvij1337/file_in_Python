class Pupil():
    def __init__(self, lastname, name, mark):
        self.lastname = lastname
        self.name = name
        self.mark = mark
with open("pupils.txt", "r", encoding="utf-8") as file:
    pupils = []
    for line in file:
        p = line.split()
        pupils.append(Pupil(p[0], p[1], p[2]))
for pup in pupils:
    if pup.mark == "5":
        print(pup.lastname)
sum = 0
for pup in pupils:
    sum += int(pup.mark)
print(round(sum / len(pupils), 2))
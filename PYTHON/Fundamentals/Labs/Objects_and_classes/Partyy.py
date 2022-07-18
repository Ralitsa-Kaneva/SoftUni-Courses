class Party:
    def __init__(self):
        self.people = list()


party = Party()
command = input()

while command != "End":
    party.people.append(command)
    command = input()

people_going = ", ".join(party.people)

print(f"Going: {people_going}")
print(f"Total: {len(party.people)}")


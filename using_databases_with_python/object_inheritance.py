class PartyAnimal:
    x = 0

    def __init__(self, nam):
        self.nam = nam
        print(self.nam, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.nam, "party count", self.x)

class FootBallFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.nam, "point", self.points)

s = PartyAnimal("Sally")
s.party()

j = FootBallFan("Jim")
j.party()
j.touchdown()

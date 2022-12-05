class Kutya:
    def __init__(self, nev, kor):
        self.name = nev
        self._kor = kor
        dogs.append(self.name)

    @property
    def kor(self):
        return self._kor

    @property
    def nev(self):
        return self.name

    @kor.setter
    def koru(self, kor):
        self._kor = kor

    def __str__(self):
        return self.name + " egy kutya aki " + str(self._kor*7) + " éves!"

    def __eq__(self, other):
        return self.name == other.name and self._kor == other.kor


def koru(dog):
    if dog1.kor <= 2:
        print(dog.nev + "fiatal kutya")
    else:
        dog1.kor = 10
    if dog2.kor <= 2:
        print(dog.nev + "fiatal kutya")
    else:
        dog2.kor = 10
    if dog3.kor <= 2:
        print(dog.nev + "fiatal kutya")
    else:
        dog3.kor = 10
    if dog4.kor <= 2:
        print(dog.nev + "fiatal kutya")
    else:
        dog4.kor = 10


def ugat(dog):
    print(dog + ":VAÚ")


if __name__ == "__main__":
    dogs = []
    dog1 = Kutya("Blöki", 2)
    dog2 = Kutya("Fifi", 4)
    dog3 = Kutya("Csibész", 3)
    dog4 = Kutya("Csibész", 3)
    print(dog1)
    print(dog3 == dog4)
    for i in range(0, len(dogs)):
        ugat(dogs[i])
        koru(dogs[i])

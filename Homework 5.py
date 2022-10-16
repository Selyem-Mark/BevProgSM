class Team:
    def __init__(self, nev, project, szerep):
        self._nev = nev
        self._project = project
        self._szerep = szerep
        print("-- Developer létrehozva --")
        print(self._nev + " a " + self._project + "-en dolgozik " + self._szerep + " szerepkörben")

    @property
    def project(self):
        return self._project

    @property
    def nev(self):
        return self._nev


if __name__ == '__main__':
    dolg1 = Team("Ricsi", "SolArch", "Fronted")
    dolg2 = Team("Angéla", "ZerTeng", "Tesztelő")
    dolg3 = Team("Peti", "KefERP", "Backend")
    dolg4 = Team("Éva", "KefERP", "Fronted")
    if dolg1.project == dolg2.project:
        print(dolg1.nev + " és " + dolg2.nev + " egy projecten dolgoznak")
    if dolg1.project == dolg3.project:
        print(dolg1.nev + " és " + dolg2.nev + " egy projecten dolgoznak")
    if dolg1.project == dolg4.project:
        print(dolg1.nev + " és " + dolg2.nev + " egy projecten dolgoznak")
    if dolg2.project == dolg3.project:
        print(dolg2.nev + " és " + dolg3.nev + " egy projecten dolgoznak")
    if dolg2.project == dolg4.project:
        print(dolg2.nev + " és " + dolg4.nev + " egy projecten dolgoznak")
    if dolg3.project == dolg4.project:
        print(dolg3.nev + " és " + dolg4.nev + " egy projecten dolgoznak")

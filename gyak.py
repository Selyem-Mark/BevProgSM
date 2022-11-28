def h():
    with open("playlist.csv", "r") as file:
        sorok = file.readlines()
        ho = len(sorok)
    return ho

def beolvas():
    playlist = []
    with open("playlist.csv", "r") as file:
        sorok = file.readlines()
        for sor in sorok:
            zene = {
                "eloado": "",
                "cim": "",
                "mufaj": "",
                "hossz": 0
            }
            darab = sor.split(";")
            zene["eloado"] = darab[0]
            zene["cim"] = darab[1]
            zene["mufaj"] = darab[2]
            zene["hossz"] = int(darab[3])
            playlist.append(zene)
    return playlist


def teljes_hossz(str):
    hosz = 0
    #print(str[1]["hossz"])
    for i in range(0, h()):
        hosz = hosz + str[i]["hossz"]
    if hosz % 60 > 30:
        perc = round((hosz / 60) - 1)
    else:
        perc = round((hosz / 60) - 1)
    mp = hosz % 60
    #print(perc)
    ido = "{}:{}"
    with open("02_hossz.txt", "w") as file:
        file.write(ido.format(perc, mp))


def leghosszabb_rockzene(str):
    lh = 0
    index = 0
    for i in range(h(), 0):
        if str[i]["mufaj"] == "rock":
            if str[i]["hossz"] >= lh:
                lh = str[i]["hossz"]
                index = i
    with open("03_leghosszabb_rock.txt", "w") as file:
        file.write(str[index]["cim"])


def leggyakoribb_mufaj(str):
    szo = []
    count = 0
    gyak = 0
    gyaksz = ""
    for i in range(0, h()):
        szo.append(str[i]["mufaj"])
    for i in range(0, len(szo)):
        for j in range(i + 1, len(szo)):
            if szo[i] == szo[j]:
                count += 1

        if gyak < count:
            gyak = count
            gyaksz = szo[i]

        with open("04_kedvenc_mufaj.txt", "w") as file:
            file.write(gyaksz.upper())


def zeneket_csoportosit(str):
    szo = []
    eload = []
    hosz = []
    for i in range(0, h()):
        szo.append(str[i]["eloado"])
        #print(szo[i])
    szo.sort()
    for i in range(0, len(szo)):
        hossz = 0 + str[i]["hossz"]
        for j in range(i + 1, len(szo)):
            if szo[i] == szo[j] and szo[i] != " ":
                if hossz == str[i]["hossz"] and str[j] not in eload:
                    eload.append(szo[i])
                    #print(szo[i])
                hossz += str[j]["hossz"]
                szo[j] = " "
        if szo[i] not in eload and szo[i] != " ":
            eload.append(szo[i])
        hosz.append(hossz)
        #print(eload)
    eloadoh = "{}: {}\n"
    with open("05_osszegzes.txt", "w") as file:
        for i in range(0, len(eload)):
            file.write(eloadoh.format(eload[i], hosz[i]))


def zeneket_listaz(eload, str):
    nev = "06_{}_dalok.txt"
    kiir = "{};{};{};\n"
    tal = 0
    with open(nev.format(eload.replace(' ', '_')), "w") as file:
        for i in range(0, h()):
            if eload == str[i]["eloado"].lower():
                    file.write(kiir.format(str[i]["cim"], str[i]["mufaj"], str[i]["hossz"]))
                    tal = 1

    if tal == 0:
        with open(nev.format(eload.replace(' ', '_')), "w") as file:
            file.write("Nincs ilyen eloado a lejatszasi listaban!")


def zeneket_torol(eload, str):
    kiir = "{};{};{};{};\n"
    with open("07_torolt.txt", 'w') as file:
        for i in range(0, h()):
            if eload != str[i]["eloado"].lower():
                file.write(kiir.format(str[i]["eloado"], str[i]["cim"], str[i]["mufaj"], str[i]["hossz"]))


if __name__ == "__main__":
    teljes_hossz(beolvas())
    leghosszabb_rockzene(beolvas())
    leggyakoribb_mufaj(beolvas())
    zeneket_csoportosit(beolvas())
    #eloado = input("Melyik előadó zenéi?")
    #zeneket_listaz(eloado.lower(), beolvas())
    eloado2 = input("Melyik előadó zenéit szeretnéd törölni?")
    zeneket_torol(eloado2.lower(), beolvas())

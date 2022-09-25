def exchange(int,string):
    if string == "cm":
        int = int/2.54
        string = "inch"
    else:
        int = int * 2.54
        string = "cm"
    exc = "{} {}"
    print(exc.format(int, string))


if __name__ == '__main__':
    print("Adjon meg egy számot és egy mértékegységet (cm/inch)")
    szam = float(input())
    mert = input()
    exchange(szam, mert)

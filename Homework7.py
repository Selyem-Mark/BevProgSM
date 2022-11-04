import string


def delet_spec_char(s):
    cha = {"y", " "}
    s = s.replace("cs", " ")
    s = s.replace("dz", " ")
    s = s.replace("dzs", " ")
    s = s.replace("sz", " ")
    s = s.replace("zs", " ")
    s = s.replace("ő", "ö")
    s = s.replace("ú", "u")
    s = s.replace("ű", "ü")
    s = s.replace("á", "a")
    s = s.replace("é", "e")
    s = s.replace("í", "i")
    s = s.replace("ó", "o")
    s = s.replace("ly", "j")
    blank = ""
    for k in s:
        if k not in cha:
            if k not in string.punctuation:
                blank += k

    return blank


def palindrom(s):
    blank = delet_spec_char(s)

    # print(blank)
    # print(blank[::-1])
    p = "Ez nem palindron"
    if blank == blank[::-1]:
        p = "Ez egy palindron"
    return p


if __name__ == "__main__":
    szov = input("Írja be a szöveget hogy leelenőrizzük hogy palindrom-e:").lower()
    print(palindrom(szov))

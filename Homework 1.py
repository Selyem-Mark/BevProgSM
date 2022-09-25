def characters(string):
    char = {}
    for i in string:
        char[i] = string.count(i)
    return char


def words(string):
    string_split = string.split(' ')
    return string_split


if __name__ == '__main__':
    print("Adjon meg egy egy mondatot:")
    s = input()
    print("Betűk gyakorisága: ", characters(s))
    print("Fordítva: ", s[::-1])
    print("Listába rendezve szavanként: ", words(s))

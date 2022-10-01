def triangle(int_a, int_b, int_c):
    if int_a + int_b >= int_c and int_b + int_c >= int_a and int_a + int_c >= int_b:
        s = "A {}, {} és {} oldalú háromszög szerkeszthető"
        print(s.format(int_a, int_b, int_c))
    else:
        s = "A {}, {} és {} oldalú háromszög NEM szerkeszthető"
        print(s.format(int_a, int_b, int_c))


if __name__ == '__main__':
    print("Adja meg a háromszög három oldalát cm-ben")
    a = int(input("a oldal (cm):"))
    b = int(input("b oldal (cm):"))
    c = int(input("c oldal (cm):"))
    triangle(a, b, c)

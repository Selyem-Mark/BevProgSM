def szor():
    elr = "{0:>2}{1:>1}{2:>6}{3:>6}{4:>6}{5:>6}{6:>6}{7:>6}{8:>6}{9:>6}{10:>6}{11:>6}{12:>6}{13:>6}"
    print(elr.format(" ", " ", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    print("  :------------------------------------------------------------------------")
    for k in range(1, 13):
        print(elr.format(k, ":", k, k * 2, k * 3, k * 4, k * 5, k * 6, k * 7, k * 8, k * 9, k * 10, k * 11, k * 12))


if __name__ == "__main__":
    szor()
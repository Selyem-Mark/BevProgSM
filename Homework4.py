def oszt(int_a, int_b):
    return int_a/int_b


if __name__ == '__main__':
    tr = 1
    while(tr == 1):
        a = int(input("Enter 'a' value"))
        b = int(input("Enter 'b' value"))
        try:

            print(oszt(a, b))

        except ZeroDivisionError:

            tr = 0
            print("Division by zero not allowed")
            print("Out of try except blocks")

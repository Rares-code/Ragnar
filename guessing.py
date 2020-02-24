import random


def player1():
    a = []
    a.append(random.randint(1, 99))
    a.append(random.randint(1, 99))
    a.append(random.randint(1, 99))
    a.append(random.randint(1, 99))
    a.append(random.randint(1, 99))
    a.append(random.randint(1, 99))
    a.append(random.randint(1, 99))
    a.append(random.randint(1, 99))
    a.append(random.randint(1, 99))
    a.append(random.randint(1, 99))
    for i in range(10):
        g = int(input("Enter an integer from 1 to 99: "))
        while a[i] != g:
            if g < a[i]:
                print("guess is low")
                g = int(input("Enter an integer from 1 to 99: "))
            elif g > a[i]:
                print("guess is high")
                g = int(input("Enter an integer from 1 to 99: "))
            else:
                continue
    print("you guessed it!")


def player2():
    b = []
    b.append(random.randint(1, 49))
    b.append(random.randint(1, 49))
    b.append(random.randint(1, 49))
    b.append(random.randint(1, 49))
    b.append(random.randint(1, 49))
    b.append(random.randint(1, 49))
    b.append(random.randint(1, 49))
    b.append(random.randint(1, 49))
    b.append(random.randint(1, 49))
    b.append(random.randint(1, 49))
    for i in range(10):
        g = int(input("Enter an integer from 1 to 49: "))
    while b[i] != g:
        if g < b[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    return ("you guessed it!")


def main():

    print("Welcome")
    x = player1()
    print(x)

    print("Player 2 turn:")
    y = player2()
    print(y)


main()

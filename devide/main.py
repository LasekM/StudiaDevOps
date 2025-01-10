def podziel(x, y):
    if y == 0:
        return "Nie można dzielić przez 0!"
    return x / y

if __name__ == "__main__":
    import sys
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(podziel(x, y))

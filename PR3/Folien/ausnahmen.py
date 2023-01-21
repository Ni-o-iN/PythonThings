a = 3
b = 0

try:
    print(a/b)
except ZeroDivisionError as dussel:
    print("Du kannst nicht durch 0 teilen.".format(dussel))
finally:
    print("Am Ende.")


def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Oh da wurde wohl durch 0 geteilt.")
    else:
        print("du darfst nicht durch 0 teilen.")
    finally:
        print("probiere es nochmal")
div(2,0)


def div2(x,y):
    if y == 0:
        raise ZeroDivisionError("Wert zum teilen ist ungültig.")
div2(3,0)
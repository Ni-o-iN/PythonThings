zahl1 = 5
zahl2 = 0

try:
    zahl1/zahl2
except ZeroDivisionError as ZDE:
    print("Man kann nicht durch 0 teilen, das gibt einen Fehler {0}, {1}.".format(zahl1, zahl2))    #muss {0}, {1} sein?
except Exception as E:
    print("Irgendein Fehler.")


def divideByTwo(a, b):
    try:
        a/b
        if b == 0:
            raise ZeroDivisionError("Man kann nicht durch 0 teilen im try.")
    except ZeroDivisionError as ZDE:
        print("Man kann nicht durch 0 teilen.")
    else:
        print("HI")
    finally:
        print("Tschau")
divideByTwo(3, 0)
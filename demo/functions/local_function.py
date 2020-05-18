gv = 30   # Global variable


def outer():  # Enclosing
    global gv
    ev = 10
    gv = 200

    def inner():  # Local
        nonlocal ev
        ev = 100
        lv = 20
        print("Inside local function -> ", gv, ev, lv)

    inner()
    print("Outer function -->", ev, gv)


outer()

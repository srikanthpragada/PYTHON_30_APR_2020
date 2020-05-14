def outer():  # Enclosing
    def inner():  # Local
        print("Inner function")

    print("Outer function")
    inner()


outer()

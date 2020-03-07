from defKey import defKey


def hello():
    print("hello")


def goodbye():
    print("goodbye")


def actualGoodbye():
    defKey.stop()


defKey.bind("h", hello)
defKey.bind("g", goodbye)
defKey.bind("q", actualGoodbye)

defKey.start()

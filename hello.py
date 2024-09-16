import sys

def hello_world(name):
    print("Hello 2, " + name + "!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"

    hello_world(name)


import sys

print('Hey, Hello222!!')
if __name__ == "__main__":
    print("Printing Args")
    for arg in sys.argv:
        print("type: {0}, value: {1}".format(type(arg), arg))
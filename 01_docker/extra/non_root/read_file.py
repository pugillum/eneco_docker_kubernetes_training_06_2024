# loads a file and outputs its content
import os

if __name__ == "__main__":
    with open("file.txt", "r") as f:
        print(f.read())

import sys


def main():
    sys.stdout.write("$ ")
    users_input = input()
    print(f"{users_input}: command not found")
    
    pass


if __name__ == "__main__":
    main()

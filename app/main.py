import sys
import shutil as sh

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        builtin_commands = ["exit", "echo", "type"]
        
        if command == 'exit':
            break
        elif command.startswith("echo"):
            print(command[5:])
        elif command.startswith("type"):    # Komenda *type* i rozpoznanie innych wbudowanych funkcji
            if command[5:] in builtin_commands:
                print(f"{command[5:]} is a shell builtin")
            elif path:= sh.which(command[5:]):  # przypisujemy zmiennej path = sh.which(command[5:]),
                print(f"{command[5:]} is {path}")   # jeśli jest to Prawdziwe, czyli jeśli jest taki plik w PATH to zwraca pełną nazwę
            else:
                print(f"{command[5:]}: not found")
        else:
            print(f"{command}: command not found")
        


if __name__ == "__main__":
    main()

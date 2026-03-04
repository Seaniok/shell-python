import sys
import shutil as sh
import subprocess as sp
import os

def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        builtin_commands = ["exit", "echo", "type", "pwd", "cd"]
        
        parts = command.split() 
        if not parts:   # Czyli jeśli lista jest pusta przerwij działanie i skocz do $
            continue
        
        if command == 'exit':
            break
        elif command.startswith("echo"):
            print(command[5:])
        elif command.startswith("type"):    # Komenda *type* i rozpoznanie innych wbudowanych funkcji
            if command[5:] in builtin_commands:
                print(f"{command[5:]} is a shell builtin")
            elif path := sh.which(command[5:]):  # przypisujemy zmiennej path = sh.which(command[5:]),
                print(f"{command[5:]} is {path}")   # jeśli jest to Prawdziwe, czyli jeśli jest taki plik w PATH to zwraca pełną lokalizację
            else:
                print(f"{command[5:]}: not found")
        elif command.startswith("cd"): # zmiana folderu pracy
            path = command[3:]
            try: 
                os.chdir(path)
            except FileNotFoundError:
                print(f"cd: <{path}>: No such file or directory")
        elif command == 'pwd':
            print(os.getcwd())
        elif path := sh.which(parts[0]):    # obsługa komand zewnętrznych
            sp.run(parts)
        else:
            print(f"{command}: command not found")
        


if __name__ == "__main__":
    main()

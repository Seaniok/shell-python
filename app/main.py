import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        builtin_commands = ["exit", "echo", "type"]
        
        if command == 'exit':
            break
        elif command.startswith("echo"):
            print(command[5:])
        elif command.startswith("type"):    #rozpoznanie komendy type 
            if command[5:] in builtin_commands:
                print(f"{command[5:]} is a shell builtin")
            else:
                print(f"{command[5:]}: not found")
        else:
            print(f"{command}: command not found")
        


if __name__ == "__main__":
    main()

# question 1 task 1

import os

def list_directory_contents(path):
    try: 
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f"Directory: {entry.name}")
                elif entry.is_file():
                    print(f"File: {entry.name}")
                else:
                    print(f"Other: {entry.name}")
    except FileNotFoundError:
        print("Error: Directory does not exist.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as unexpected:
        print(f"An unexpected error occurred: {unexpected}")

def main():
    path = input("Enter directory path: ")
    list_directory_contents(path)

if __name__ == "__main__":
    main()
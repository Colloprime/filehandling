# file_handling_assignment.py

# Task 1: File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("Second line with a number: 42\n")
        file.write("Third line with a float: 3.14\n")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")

# Task 2: File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("File Contents:")
        print(contents)
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Task 3: File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Fourth line appended.\n")
        file.write("Fifth line appended with a value: 3.67\n")
        file.write("Sixth line appended.\n")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
finally:
    print("File appending operation completed.")

# Task 4: Error Handling
try:
    with open("nonexistent_file.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("The file 'nonexistent_file.txt' does not exist.")
except PermissionError:
    print("You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
#TASK1
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for line_number, line in enumerate(file, start=1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Call the function with the file name
read_file('sample.txt')
 #task 2
 # Step 1: Take input and write to a file
text1 = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text1 + "\n")
print("Data successfully written to output.txt.")

# Step 2: Take more input and append to the same file
text2 = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text2 + "\n")
print("Data successfully appended.")

# Step 3: Read and show final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())

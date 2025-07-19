# 1. Read a Text File and Print Its Content
filename = "file.txt"
print("1. Read and print file content:")
with open(filename, 'r') as file:
    for line in file:
        print(line, end='')


# 2. Write User Input to a Text File
print("2. Write user input to file:")
text = input("Enter some text to save in file.txt: ")
with open(filename, 'w') as file:
    file.write(text)


# 3. Append Data to an Existing File
print("3. Append data to existing file:")
text = input("Enter text to append: ")
with open(filename, 'a') as file:
    file.write('\n' + text)


# 4. Read a File and Count the Number of Lines
print("4. Count number of lines in file:")
with open(filename, 'r') as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")


# 5. Count Words and Characters in a File
print("5. Count words and characters in file:")
with open(filename, 'r') as file:
    content = file.read()
    words = content.split()
    characters = len(content)
    print(f"Words: {len(words)}")
    print(f"Characters: {characters}")


# 6. Search for a Word in a File
print("6. Search for a word in file:")
search_word = input("Enter word to search for: ")
with open(filename, 'r') as file:
    found = False
    for line in file:
        if search_word in line:
            print(line, end='')


# 7. Remove Blank Lines from a File
print("7. Remove blank lines from file and save to file_no_blanks.txt")
input_file = filename
output_file = "file_no_blanks.txt"
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        if line.strip() != '':
            outfile.write(line)


# 8. Copy One File's Content into Another
print("8. Copy file content from file.txt to copy_of_file.txt")
source = filename
destination = "copy_of_file.txt"
with open(source, 'r') as src, open(destination, 'w') as dst:
    content = src.read()
    dst.write(content)


# 9. Read a File in Reverse Order
print("9. Print file content in reverse order:")
with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines[::-1]:
        print(line, end='')


# 10. Check if a File Exists and Handle Error
print("10. Check if a file exists and print content:")
check_file = input("Enter filename to check: ")
with open(check_file, 'r') as file:
    print(file.read())


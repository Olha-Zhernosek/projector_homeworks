# Вміст для першого файлу
content = '''
Create a file with some content. As example, you can
take this one:

“Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum”.

Create a second file and copy the content of the first file
to the second file in upper case.
'''

file_name_1 = 'text_1.txt'
with open(file_name_1, "w") as file:
    file.write(content)

print(f"File '{file_name_1}' with content created.")

with open(file_name_1, "r") as source_file:
    content = source_file.read()

file_name_2 = 'text_2.txt'
with open(file_name_2, "w") as target_file:
    target_file.write(content.upper())

print(f"File '{file_name_2}' with upper case content created.")

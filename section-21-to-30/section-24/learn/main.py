import os 
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
# print(os.getcwd())

with open("my_file.txt", "r+") as file:
    # file.seek(0)
    content = file.read()
    print(content)
    file.seek(0)
    file.write("Hello World")
    file.truncate()
    file.seek(0)
    updated_content = file.read()
    print("Updated content:")
    print(updated_content)

import os 
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
# print(os.getcwd())

with open("my_file.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    print(content)
    file.write("\nHello World")

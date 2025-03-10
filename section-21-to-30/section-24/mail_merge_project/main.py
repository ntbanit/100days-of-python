import os 
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

letter = ""
with open("./input/letters/starting_letter.txt") as file:
    letter = file.read()

def create_letters():
    if not letter: 
        print("No letter found")
        return

    with open("./input/names/invited_names.txt") as file:
        names = file.readlines()
        for name in names:
            name = name.strip()
            with open(f"./output/ready_to_send/letter_for_{name}.txt", "w") as output_file:
                output_file.write(letter.replace("[name]", name))
    print("Letters created successfully")
create_letters()
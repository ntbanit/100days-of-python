# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import os

stop = False
auction_dict = {}

while not stop :
    os.system('cls')
    name = input("What's your name?: ")
    bid = float(input("What's your bid?: $"))
    auction_dict[name] = bid

    confirm = input("Any other bid? (yes/no) ")
    if confirm == "no" :
        stop = True

# max_auction = 0
winner = max(auction_dict, key=auction_dict.get)
# for key in auction_dict :
#     if max_auction < auction_dict[key] :
#         winner = key
#         max_auction = auction_dict[key]

os.system('cls')
print(f"Winner is {winner}")
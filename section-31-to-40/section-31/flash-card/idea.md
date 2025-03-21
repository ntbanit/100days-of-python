When I will flipping the card 

- 3 seconds after the word appear 
- when the word is refresh (tick event or cross event), 3 seconds after that 

others : # dev my own app  # target to learn 10000 (wiki) + 10000 (github resources) English Frequency
when the word is cross, 
- save it to temp_remembered.csv then remove from dictionary 
   mark to repeat it after 3 -> 5 -> 8 -> 13 times
Example : 
original list
1 - apple 
2 - banana
3 - mango
4 - orange
5 - strawberry
6 - pineapple
7 - grape
8 - watermelon
9 - kiwi
10 - peach
11 - pear
12 - cherry
13 - durian
14 - raspberry
15 - lemon
16 - lime
17 - coconut
18 - papaya
19 - pomegranate
20 - apricot

First time learn tick 1 2 8 18
len = M
tick = [1 2 8 18 ] -> repeat after 3 times 
len = N
cross = [3 4 5 10 19 20] -> repeat gain (1 time)

# tỷ lệ random ra cross là (N * 3 + M) / (N + M)
~~~python 
import random

def weighted_random_selection(tick, cross):
    M = len(tick)
    N = len(cross)
    
    # Create a combined list with weights
    combined = [(item, 1) for item in tick] + [(item, 3) for item in cross]
    
    # Unpack the items and weights
    items, weights = zip(*combined)
    
    # Use random.choices for weighted random selection
    selected = random.choices(items, weights=weights, k=1)[0]
    
    return selected

# Example usage
tick = [1, 2, 8, 18]
cross = [3, 4, 5, 10, 19, 20]

# Test the function
for _ in range(20):  # Let's run it 20 times as an example
    result = weighted_random_selection(tick, cross)
    print(f"Selected: {result}")

# Calculate and print the theoretical probability
M = len(tick)
N = len(cross)
prob_cross = (N * 3) / (N * 3 + M)
print(f"\nTheoretical probability of selecting from cross: {prob_cross:.2f}")
~~~ python 


lưu vào file space_1 , space_3, space_5, space_8, space_13

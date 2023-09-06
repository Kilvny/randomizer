import random 
import time

bucket_of_items = []
selected_items = []

number_of_items: int = int(input("Please enter the number of items to select from"))
for i in range(number_of_items):
    cur_item = input(f"Enter item {i+1}: ")
    bucket_of_items.append(cur_item)

print("\n.\n.\n.\nKindly wait for the selection to get done... \n \n \n")
for i in range(1):
    item = random.choice(bucket_of_items)
    selected_items.append(item)
time.sleep(3)

print(f"\n Selected Items after 3 iterations are {selected_items}")






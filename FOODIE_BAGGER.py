

observed_data = {
    "loaf of bread": [1, "dry_food"],
    "eggs": [2,"dry_food", "fragile"], 
    "bag of onions": [9,"dry_food"], 
    "chips": [0.5,"dry_food", "fragile"],
    "meat": [7,"leaky_food"],
    "gallon of milk": [8.6,"leaky_food"],
    "gallon of water": [8.3,"leaky_food"],
    "watermelon": [9,"dry_food"],
    "pasta": [1.1,"dry_food"],
    "pint of ice cream": [1.04,"frozen_food"],

}

#the items in the order have to be in observed_data list.
order = [ ["gallon of water", 2] , ["pint of ice cream", 1], ["meat", 1],  ["loaf of bread",1], ["chips", 1]]


working_memory = []
current_bag = 0

def rules():
    global working_memory
    #bag frozen items
    for item in order:
        if "frozen_food" in observed_data[item[0]]:
            print(f"Rule 1 says: bag {item[0]} in the freezer bag")
            order.remove(item)
    #need to bag large items first
    for item in order:
        if observed_data[item[0]][0] > 8:
            #print(item[0], "is a large item")
            working_memory = working_memory + [item[0]] + observed_data[item[0]]
            working_memory.append("large")


if __name__ == "__main__":
    rules()
    pass

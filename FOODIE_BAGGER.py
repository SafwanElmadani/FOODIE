

observed_data = {
    "loaf of bread": [1],
    "eggs": [2, "fragile"], 
    "bag of onions": [9], 
    "chips": [0.5,"fragile"],
    "meat": [7],
    "gallon of milk": [8.6],
    "gallon of water": [8.3],
    "watermelon": [9],
    "pasta": [1.1],
    "pint of ice cream": [1.04,"frozen_food"],

}

#the items in the order have to be in observed_data list.
order = [ ["gallon of water", 2] , ["pint of ice cream", 1], ["meat", 1],  ["loaf of bread",1], ["chips", 1]]


working_memory = []
current_bag_items = 0
bags_count = 0

def rules():
    global working_memory
    global current_bag_items
    global bags_count
    print(f"*** start bagging ***")
    while True:
        #bag frozen items R1
        for item in order:
            if "frozen_food" in observed_data[item[0]]:
                print(f"Rule 1 applies: bag {item[0]} in the freezer bag")
                order.remove(item)
        #need to bag large items first
        for item in order:

            #check for large items R2
            if observed_data[item[0]][0] > 8:
                #print(item[0], "is a large item")
                working_memory = working_memory + [item[0]] + observed_data[item[0]]
                working_memory.append("large")
                print(f"Rule 2 applies: bagging a large item")

            #check for medioum items R3
            if 5 <= observed_data[item[0]][0] <= 8:
                working_memory = working_memory + [item[0]] + observed_data[item[0]]
                working_memory.append("medioum")
                print(f"Rule 3 applies: bagging a medioum item")

            #check for small items R4
            if observed_data[item[0]][0] < 5:
                working_memory = working_memory + [item[0]] + observed_data[item[0]]
                working_memory.append("small")
                print(f"Rule 4 applies: bagging a small item")

            #check if we need a new bag for large item R5
            if "large" in working_memory and current_bag_items == 1:
                working_memory.append("need_new_bag")

            #check if we need a new bag for medioum item R6
            if "medioum" in working_memory and current_bag_items == 5:
                working_memory.append("need_new_bag")

            #check if we need a new bag for small items R7
            if "small" in working_memory and current_bag_items == 10:
                working_memory.append("need_new_bag")

            #check if a new paper bag is needed R8
            if "need_new_bag" in working_memory:
                print(f"Rule R8 applies: starting a new bag")
                bags_count = bags_count + 1

            #bag large item R9
            if "large" in working_memory and current_bag_items < 1:
                print(f"Rule R9 applies: put {item[0]} in bag_{bags_count}")
                current_bag_items = current_bag_items + 1
                
            #bag medioum item R10
            if "medioum" in working_memory and current_bag_items < 5:
                print(f"Rule R10 applies: put {item[0]} in bag_{bags_count}")

            #bag medioum item R11
            if "small" in working_memory and current_bag_items < 10:
                print(f"Rule R11 applies: put {item[0]} in bag_{bags_count}")

            #bag fragile items last R12
            if "fragile" in working_memory:
                print(f"Rule R12 applies: put {item[0]} in a separete bag and place it on top of other bags")

        if not order:
            print(f"*** bagging is finished ***")
            break

if __name__ == "__main__":
    rules()
    pass

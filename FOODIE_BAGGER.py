

observed_data = {
    "loaf of bread": [1],
    "eggs": [2, "fragile"], 
    "bag of onions": [9], 
    "chips": [0.5,"fragile"],
    "meat": [7],
    "1-gallon of milk": [8.6],
    "1-gallon of water": [8.3],
    "watermelon": [9],
    "pasta": [1.1],
    "pint of ice cream": [1.04,"frozen_food"],

}

#the items in the order have to be in observed_data list.
order = [ ["1-gallon of water", 2] , ["pint of ice cream", 1], ["meat", 1],  ["loaf of bread",1], ["chips", 1]]

def expnad_list():
    for i in order:
        if i[1] > 1:
            pass



working_memory = []
current_bag_items = 0
bags_count = 1

def find_item(size):
    if not order:
        return None
    for i in order:
        if observed_data[i[0]][0] > 8 and size == 'L':
            return i

        if 5 <= observed_data[i[0]][0] <= 8 and size == 'M':
            return i
        
        if observed_data[i[0]][0] < 5 and size == 'S':
            return i

def rules():
    global working_memory
    global current_bag_items
    global bags_count
    print(f"*** start bagging ***")
    while True:
        #bag frozen items R1
        for item in order:
            if "frozen_food" in observed_data[item[0]]:
                print(f"Rule {1:02} applies: bag {item[0]} in the freezer bag")
                order.remove(item)
        #need to bag large items first
        item = find_item("L")
        if item is None:
            #then medioum items
            item = find_item("M")
            if item is None:
                #then small items
                item = find_item("S")
            
            #check for large items R2
        if observed_data[item[0]][0] > 8:
            #print(item[0], "is a large item")
            working_memory = working_memory + [item[0]] + observed_data[item[0]]
            working_memory.append("large")
            print(f"Rule {2:02} applies: bagging a large item")

        #check for medioum items R3
        if 5 <= observed_data[item[0]][0] <= 8:
            working_memory = working_memory + [item[0]] + observed_data[item[0]]
            working_memory.append("medioum")
            print(f"Rule {3:02} applies: bagging a medioum item")

        #check for small items R4
        if observed_data[item[0]][0] < 5:
            working_memory = working_memory + [item[0]] + observed_data[item[0]]
            working_memory.append("small")
            print(f"Rule {4:02} applies: bagging a small item")

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
            print(f"Rule {8:02} applies: starting a new bag")
            bags_count = bags_count + 1

        #bag large item R9
        if "large" in working_memory and current_bag_items < 1 and "fragile" not in working_memory:
            print(f"Rule {9:02} applies: put {item[0]} in bag_{bags_count}")
            current_bag_items = current_bag_items + 1
            order.remove(item)
            if not find_item("L"):
                bags_count = bags_count + 1
            working_memory.clear()
            
        #bag medioum item R10
        if "medioum" in working_memory and current_bag_items < 5 and "fragile" not in working_memory:
            print(f"Rule 10 applies: put {item[0]} in bag_{bags_count}")
            order.remove(item)
            if not find_item("M"):
                bags_count = bags_count + 1
            working_memory.clear()

        #bag medioum item R11
        if "small" in working_memory and current_bag_items < 10 and "fragile" not in working_memory:
            print(f"Rule 11 applies: put {item[0]} in bag_{bags_count}")
            order.remove(item)
            if not find_item("S"):
                bags_count = bags_count + 1
            working_memory.clear()

        #bag fragile items last R12
        if "fragile" in working_memory:
            print(f"Rule 12 applies: put {item[0]} in a separete bag labeled \"Fragile\" and place it on top of the other bags to avoid being crushed.")
            order.remove(item)

        if not order:
            print(f"*** bagging is finished ***")
            break

if __name__ == "__main__":
    rules()
    pass

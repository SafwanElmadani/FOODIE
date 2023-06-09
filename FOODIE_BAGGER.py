
import sys

observed_data = {
    "loaf of bread": [1],
    "dozen eggs carton": [2, "fragile"], 
    "bag of onions": [9], 
    "bag of chips": [0.5,"fragile"],
    "gallon of milk": [8.6],
    "gallon of water": [8.3],
    "watermelon": [9],
    "pasta": [1.1],
    "pint of ice cream": [1.04,"frozen_food"],
    "jar of peanut butter": [2.5],
    "bag of potatoes": [9],
    "ground beef": [2],
    "sliced smoked turkey": [4],
    "12 pack of soda": [10],
    "bag of apples": [6],
    "bag of flour": [5],
    "bag of sugar": [5]
}

#the items in the order have to be in observed_data list.
order = []

def set_order(args):
    print(args[1])
    global order
    if args[1] == "order1":
        order = [ ["gallon of milk", 2], ["dozen eggs carton", 1], ["bag of chips",1], ["loaf of bread", 2], ["pint of ice cream", 1], ["jar of peanut butter", 1], ["12 pack of soda", 1]]
    if args[1] == "order2":
        order = [ ["gallon of water", 3] , ["pint of ice cream", 1], ["ground beef", 3], ["loaf of bread",1], ["dozen eggs carton", 1], ["bag of flour", 2], ["bag of sugar", 4], ["watermelon", 1] , ["bag of potatoes", 1]]
    else:
        print("no such order!")
        sys.exit()

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
            #return non-fragile items fist
            for j in order:
                if "fragile" not in observed_data[j[0]]:
                    return j
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
                print(f"Rule {1:02} applies: bag 1 {item[0]} in the freezer bag")
                if item[1] == 1:
                    order.remove(item)
                else:
                    item[1] = item[1] - 1
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
            current_bag_items = 0

        #bag large item R9
        if "large" in working_memory and current_bag_items < 1 and "fragile" not in working_memory:
            print(f"Rule {9:02} applies: put 1 {item[0]} in bag_{bags_count}")
            current_bag_items = current_bag_items + 1
            #order.remove(item)
            if item[1] == 1:
                order.remove(item)
            else:
                item[1] = item[1] - 1
            if not find_item("L"):
                bags_count = bags_count + 1
                current_bag_items = 0
            working_memory.clear()
            
        #bag medioum item R10
        if "medioum" in working_memory and current_bag_items < 5 and "fragile" not in working_memory:
            print(f"Rule 10 applies: put 1 {item[0]} in bag_{bags_count}")
            current_bag_items = current_bag_items + 1
            #order.remove(item)
            if item[1] == 1:
                order.remove(item)
            else:
                item[1] = item[1] - 1
            if not find_item("M"):
                bags_count = bags_count + 1
                current_bag_items = 0
            working_memory.clear()

        #bag medioum item R11
        if "small" in working_memory and current_bag_items < 10 and "fragile" not in working_memory:
            print(f"Rule 11 applies: put 1 {item[0]} in bag_{bags_count}")
            current_bag_items = current_bag_items + 1
            #order.remove(item)
            if item[1] == 1:
                order.remove(item)
            else:
                item[1] = item[1] - 1
            if not find_item("S"):
                bags_count = bags_count + 1
                current_bag_items = 0
            working_memory.clear()

        #bag fragile items last R12
        if "fragile" in working_memory:
            print(f"Rule 12 applies: put 1 {item[0]} in a separete bag labeled \"Fragile\" and place it on top of the other bags to avoid being crushed.")
            #order.remove(item)
            if item[1] == 1:
                order.remove(item)
            else:
                item[1] = item[1] - 1
            working_memory.clear()

        if not order:
            print(f"*** bagging is finished ***")
            break

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("usage:\nFOODIE_BAGGER.py order#")
        sys.exit()
    set_order(sys.argv)
    # set_order([0 , "order2"])
    rules()

    pass

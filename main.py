"""
Final project ECE579
This file has methods to read graph nodes from file and create a graph
"""
from tree_search import Node
import csv

graph = {}

def read_node_fron_file(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header row
        next(csv_reader)

        for row in csv_reader:
            #print(row[0])
            add_to_graph(row)

def add_to_graph(row):
    parent_name = row[0]
    parent_g_n = row[1]
    parent_coords = row[2],row[3]

    child_name = row[4]
    child_g_n = row[5]
    child_coords = row[6], row[7]

    #check if the parent is alreay exist
    if (parent_name in graph):
        parent_node = graph[parent_name]
    else:
        parent_node = Node(parent_name, parent_coords, None, parent_g_n, [])
        graph[parent_node.name] = parent_node
        
    child_node = Node(child_name, child_coords, parent_node, child_g_n,[])
    parent_node.children.append(child_node)

    graph[child_node.name] = child_node

def main(file_name):
    read_node_fron_file(file_name)
    start_node = 'SU'
    goal_node = 'SofI'

    #start_node = 'SU'

    parent_list = graph[goal_node].get_parents()
    if not parent_list:
        print("this node has no parents")
        return
    else:
        parent_list.insert(0,graph[goal_node])
        parent_list.reverse()
    print(len(parent_list), "size")
    for i in parent_list:
        print(i.name, end='')
        if i.name != goal_node:
            print(' ----> ', end='')
        if i.name == goal_node:
            print("")
            break
    
if __name__ == "__main__":
    main("graph_data")


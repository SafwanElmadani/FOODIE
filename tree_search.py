"""
pynpuzzle - Solve n-puzzle with Python
License : MIT License
"""
#from copy import deepcopy
import csv
import heapq
import numpy as np

class Node:
    def __init__(self, name=None, coords=None, parent=None, cost=0, children=[]):
        self.name = name
        self.coords = coords
        self.parent = parent
        self.g_n = cost
        self.children = children

    def is_goal_state(self, name, goal_state_name):
        if name == goal_state_name:
            return True
        else:
            return False

    def is_goal(self, goal_state_name):
        return self.is_goal_state(self.name, goal_state_name)

    def parents(self):
        current_node = self
        while current_node.parent:
            yield current_node.parent
            current_node = current_node.parent

   # def gn(self):
   #     costs = self.cost
   #     for parent in self.parents():
   #         costs += parent.cost

   #     return costs
    def get_parents(self):
        parent_list = []
        for parent in self.parents():
            parent_list.append(parent)
        return parent_list

    def gn(self):
        return self.g_n

    def check_if_state_exists(self, new_state):
        for parent in self.parents():
            if (new_state == parent.state):
                return True
        return False
    

class Map_Constructor:
    
    def __init__(self):
        self.graph = {}

    def read_node_from_file(self, file_name):

        self.graph = {}

        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            # Skip the header row
            next(csv_reader)

            for row in csv_reader:
                #print(row[0])
                self.add_to_graph(row)
            
        return self.graph

    def add_to_graph(self, row):

        parent_name = row[0]
        parent_g_n = float(row[1])
        parent_coords = float(row[2]),float(row[3])

        child_name = row[4]
        child_g_n = float(row[5])
        child_coords = float(row[6]), float(row[7])

        #check if the parent is alreay exist
        if (parent_name in self.graph):
            parent_node = self.graph[parent_name]
        else:
            parent_node = Node(parent_name, parent_coords, None, parent_g_n, [])
            self.graph[parent_node.name] = parent_node
            

        if child_name in self.graph:
            parent_node.children.append(self.graph[child_name])
            self.graph[child_name].children.append(parent_node)
        else:
            child_node = Node(child_name, child_coords, parent_node, child_g_n,[])
            parent_node.children.append(child_node)
            
            self.graph[child_name] = child_node
            self.graph[child_name].children.append(parent_node)

        # if child_name in self.graph:
        #     self.graph[child_name].children.append(parent_node)
        # else:
        #     self.graph[child_name] = child_node


class astar:

    def __init__(self):
        None

    def heuristic(self, node, goal_state):
        
        # distance to energy

        distance = np.linalg.norm(np.array(node.coords) - np.array(goal_state.coords))
        energy = distance * 10000000

        return energy


    def astar(self, start_state, goal_state, search_tree):
        # Open and closed sets
        open_set = [(0, start_state)]
        closed_set = set()
        
        # Keep track of the path traveled and the cost with the following datatypes
        path = {}
        cost = {}
        path[start_state] = None
        cost[start_state] = 0
        
        # Continue the search while the open set is not empty
        while len(open_set) > 0:
            # Choose the node with the lowest f value to continue with, and take it out of the open set
            current_node = heapq.heappop(open_set)[1]
            #print(current_node)
            current_node = search_tree[current_node].name
            
            # First check if the current node is already the goal state
            if current_node == goal_state:
                # Add the cost of the node to the total cost
                total_cost = cost[current_node]
                current_path = []
                # Backtrack to determine the path, and then flip the result to show the proper sequence
                while current_node is not None:
                    current_path.append(current_node)
                    current_node = path[current_node]
                current_path.reverse() 
                # conclude search and return the path and total cost
                return current_path, total_cost
            
            # Whether goal state or not, add the current node to the closed set
            closed_set.add(current_node)
            
            # Search through the children/neighbors of the current node and get their cost and names
            for neighbor in search_tree[current_node].children:
                edge_cost = neighbor.g_n
                neighbor = neighbor.name

                # Avoid a loop by not visiting neighbors already in our closed set
                if neighbor in closed_set:
                    continue
                
                # Calculate the g and f values for the nodes based on ege costs and heuristics.
                tentative_g = cost[current_node] + edge_cost
                tentative_f = tentative_g + self.heuristic(search_tree[neighbor], search_tree[goal_state])
                
                # Add the neighbors to the open set so they can be explored on next iteration
                if ((tentative_f, neighbor) not in open_set) and (neighbor not in closed_set):
                    heapq.heappush(open_set, (tentative_f, neighbor))
                    
                # Update the path with the path that has the best g/f values
                if tentative_g < cost.get(neighbor, float('inf')):
                    path[neighbor] = current_node
                    cost[neighbor] = tentative_g
                    
        # No path is found if this return condition is met
        return None, None



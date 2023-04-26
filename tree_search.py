"""
pynpuzzle - Solve n-puzzle with Python
License : MIT License
"""
#from copy import deepcopy


def is_goal_state(name, goal_state_name):
    if name == goal_state_name:
        return True
    else:
        return False
    

class Node:
    def __init__(self, name=None, coords=None, parent=None, cost=0, children=[]):
        self.name = name
        self.coords = coords
        self.parent = parent
        self.g_n = cost
        self.children = children

    def is_goal(self, goal_state_name):
        return is_goal_state(self.name, goal_state_name)

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


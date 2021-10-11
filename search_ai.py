#
# Author: Rakan AlZagha
# Date: 3/15/2021
#
# Assignment: Project #1
# Comments: BFS Linear Search is rather slow for more complicated problems (as expected), however, it fully works.
#


from queue import Queue
from time import time
from queue import PriorityQueue
import random
import sys
import numpy as np

#
# Class: Eight_Puzzle
# Purpose: create an instance of the 8-Puzzle
# and provide necessary elements to solve it
# (heuristic, path, eval, state, goal)
#

class Eight_Puzzle:
    state_count=0
    goal_state=[0,0,0,0,0,0,0,0,0]
    astar_eval=None
    heuristic_function = None
    heuristic_needed = False
    heuristic_type = None
    def __init__(self, state, root_origin, move, path_cost, goal_state, heuristic_type = None, heuristic_needed=False):
        self.root_origin=root_origin
        self.state=state
        self.move=move
        self.goal_state=goal_state
        if (self.root_origin == True):
            self.path_cost = root_origin.path_cost + path_cost
        else:
            self.path_cost = path_cost
        if (heuristic_needed == True):
            self.heuristic_needed=True
            self.heuristic_type=heuristic_type
            if(self.heuristic_type == 1):
                self.first_heuristic()
                self.astar_eval=self.heuristic_function+self.path_cost
            elif(self.heuristic_type == 2):
                self.second_heuristic()
                self.astar_eval=self.heuristic_function+self.path_cost
        else:
            heuristic_needed = False
        Eight_Puzzle.state_count = Eight_Puzzle.state_count + 1

    #
    # Function: first_heuristic
    # Purpose: calculate the number of misplaced tiles
    # and then report heuristic back to class
    # Parameters: self
    #

    def first_heuristic(self):
        self.heuristic_function=0
        for curr_node in range(1,9):
            if (self.is_goal_node(self,curr_node) == False):
                self.heuristic_function=self.heuristic_function+1
    #
    # Function: second_heuristic
    # Purpose: calculate the Manhattan distance of tiles
    # and then report heuristic back to class
    # Parameters: self
    #

    def second_heuristic(self):
        self.heuristic_function=0
        for curr_node in range(1,9):
            distance=abs(self.state.index(curr_node) - self.goal_state.index(curr_node))
            row=int(distance/3)
            column=int(distance%3)
            self.heuristic_function=self.heuristic_function+row+column

    #
    # Function: is_goal_node (static)
    # Purpose: checks if the current node is in the goal nodes place
    # Parameters: self, curr_node
    #

    @staticmethod
    def is_goal_node(self, curr_node):
        if (self.goal_state[curr_node] == self.state[curr_node]):
            return True
        else:
            return False
    
    #
    # Function: is_goal
    # Purpose: checks to see if current state is goal state
    # Parameters: self
    #

    def is_goal(self):
        if self.state == self.goal_state:
            return True
        else:
            return False

    #
    # Function: is_legal
    # Purpose: check if a move is legal/limit actions
    # Parameters: row,column
    #

    @staticmethod
    def is_legal(row,column):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        if row == 0:  
            possible_actions.remove('UP')
        if row == 2: 
            possible_actions.remove('DOWN')
        if column == 0:
            possible_actions.remove('LEFT')
        if column == 2:
            possible_actions.remove('RIGHT')
        return possible_actions

    #
    # Function: explore_children
    # Purpose: expand current child node and generate children
    # Parameters: self
    #

    def explore_children(self):
        children=[]
        curr_pos = self.state.index(0)
        row = int(curr_pos / 3)
        column = int(curr_pos % 3)
        legal_actions=self.is_legal(row,column)
        for move in legal_actions:
            new_state = self.state.copy()
            if move == 'UP':
                temp_state = new_state[curr_pos]
                new_state[curr_pos] = new_state[curr_pos-3]
                new_state[curr_pos-3] = temp_state
            if move == 'DOWN':
                temp_state = new_state[curr_pos]
                new_state[curr_pos] = new_state[curr_pos+3]
                new_state[curr_pos+3] = temp_state
            if move == 'LEFT':
                temp_state = new_state[curr_pos]
                new_state[curr_pos] = new_state[curr_pos-1]
                new_state[curr_pos-1] = temp_state
            if move == 'RIGHT':
                temp_state = new_state[curr_pos]
                new_state[curr_pos] = new_state[curr_pos+1]
                new_state[curr_pos+1] = temp_state
            children.append(Eight_Puzzle(new_state, self, move, 1, self.goal_state, self.heuristic_type, self.heuristic_needed))
        return children

    #
    # Function: solution_path
    # Purpose: keep track of path/moves taken
    # Parameters: self
    #

    def solution_path(self):
        final_solution = []
        final_solution.append(self.move)
        final_path = self
        while final_path.root_origin != None:
            final_path = final_path.root_origin
            final_solution.append(final_path.move)
        final_solution = final_solution[:-1]
        final_solution.reverse()
        return final_solution
#
# Function: input_configuration
# Purpose: Take in initial state as random or custom
# Parameters: initial_state_decision
#

def input_configuration(initial_state_decision):
    if(initial_state_decision == 1):
        initial_state = custom_config()
        print()
        print("Initial State:")
        print_puzzle(initial_state)
        print()
    elif(initial_state_decision == 2):
        initial_state = random_config()
        print("Initial State:")
        print_puzzle(initial_state)
    return initial_state

#
# Function: random_config
# Purpose: generate a random configuration
# Parameters: N/A
#

def random_config():
    print("You chose random configuration\n.\n.\n.\n")
    initial_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(initial_state)
    return initial_state

#
# Function: custom_config
# Purpose: take in a custom tile configuration
# Parameters: N/A
#

def custom_config():
    print("You chose custom configuration\n.\n.\n.\n")
    print("Enter 9 values from '0:8', seperate each with a space: ")
    digit_input = input()
    initial_state = digit_input.split(' ')
    char_to_int(initial_state)
    return initial_state

#
# Function: char_to_int
# Purpose: convert char array into int array
# Parameters: array
#

def char_to_int(array):
    for i in range(0, len(array)):
        array[i] = int(array[i])
    return array

#
# Function: print_puzzle
# Purpose: print the whole matrix (if needed)
# Parameters: array
#

def print_puzzle(array):
    two_dimension = np.reshape(array, (-1,3))
    for i in two_dimension:
        for j in i:
            print(j, end=" ")
        print()

#
# Function: parity_check
# Purpose: identify the parity needed for goal state calculation
# Parameters: array
#

def parity_check(array):
    parity_array = array[:]
    count = 0
    for i in range(0, len(parity_array) - 1):
        if(parity_array[i] == 0):
            del parity_array[i]
    for i in range(0, len(parity_array)):
        value = parity_array[i]
        for j in range(i+1, len(parity_array)):
            if(parity_array[j] < value):
                count = count + 1
    if(count % 2 == 0):
        parity = 0
    elif(count % 2 != 0):
        parity = 1
    return parity

#
# Function: goal_state_func
# Purpose: identify correct goal based on parity
# Parameters: self
#

def goal_state_func(parity):
    if (parity == 0):
        goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    elif (parity == 1):
        goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    print("\nGoal State:")
    print_puzzle(goal_state)
    return goal_state

#
# Function: breadth_first_search
# Purpose: search algorithm implementation for BFS
# returns the solution to the puzzle
# Parameters: initial_state, goal_state
# Comments: struggles for more complex problems,
# works, but takes a long time
# Solutions: attempted to use binary search over linear search for reached states, 
# results were not as promising as I thought they would be
#

def breadth_first_search(initial_state, goal_state):
    initial_root_node = Eight_Puzzle(initial_state, None, None, 0, goal_state,None, False)
    if initial_root_node.is_goal():
        return initial_root_node.solution_path()
    frontier = Queue()
    frontier.put(initial_root_node)
    reached=[]
    while (frontier.empty() != True):
        child_node=frontier.get()
        reached.append(child_node.state)
        expand_children=child_node.explore_children()
        for child in expand_children:
            if child.state not in reached:
                if child.is_goal():
                    return child.solution_path()
                frontier.put(child)
#
# Function: a_star_misplaced (heuristic one)
# Purpose: search algorithm for astar
# returns the path to the solution
# Parameters: initial_state, goal_state
#

def a_star_misplaced(initial_state, goal_state):
    count=0
    reached=[]
    initial_root_node=Eight_Puzzle(initial_state,None,None,0,goal_state,1,True)
    frontier = PriorityQueue()
    frontier.put((initial_root_node.astar_eval,count,initial_root_node))
    while (frontier.empty() != True):
        child_node=frontier.get()
        child_node=child_node[2]
        reached.append(child_node.state)
        if child_node.is_goal():
            return child_node.solution_path()
        expand_children=child_node.explore_children()
        for child in expand_children:
            if child.state not in reached:
                count = count + 1
                frontier.put((child.astar_eval,count,child))

#
# Function: a_star_manhattan (heuristic two)
# Purpose: search algorithm for astar
# returns the path to the solution
# Parameters: initial_state, goal_state
#

def a_star_manhattan(initial_state, goal_state):
    count=0
    reached=[]
    initial_root_node=Eight_Puzzle(initial_state,None,None,0,goal_state,2,True)
    frontier = PriorityQueue()
    frontier.put((initial_root_node.astar_eval,count,initial_root_node))
    while (frontier.empty() != True):
        child_node=frontier.get()
        child_node=child_node[2]
        reached.append(child_node.state)
        if child_node.is_goal():
            return child_node.solution_path()
        expand_children=child_node.explore_children()
        for child in expand_children:
            if child.state not in reached:
                count = count + 1
                frontier.put((child.astar_eval,count,child))

#
# Function: main
# Purpose: compile the 3 search algorithms and display results
# Parameters: N/A
#

def main():
    print("------------------------------------")
    print("Welcome to the Eight_Puzzle Game!")
    print("------------------------------------")
    print()
    print("Please input decision (1 or 2) of initial state:\n\t1. Custom Configuration\n\t2. Random Configuration")
    initial_state_decision = int(input("--> "))
    initial_state = input_configuration(initial_state_decision)
    parity = parity_check(initial_state)
    goal_state = goal_state_func(parity)

    Eight_Puzzle.state_count=0
    initial_time=time()
    bfs=breadth_first_search(initial_state, goal_state)
    final_time=time()-initial_time
    print()
    print('Breadth First Search:', bfs)
    print('Total Number of Moves Required:', len(bfs))
    print('Total Number of Search Tree Nodes Explored:', Eight_Puzzle.state_count)
    print('Time until Completion:', final_time)
    print()

    Eight_Puzzle.state_count = 0
    initial_time = time()
    astar_misplaced = a_star_misplaced(initial_state, goal_state)
    final_time = time() - initial_time
    print()
    print('A* Misplaced Heuristic:',astar_misplaced)
    print('Total Number of Moves Required:', len(astar_misplaced))
    print('Total Number of Search Tree Nodes Explored:', Eight_Puzzle.state_count)
    print('Time until Completion:', final_time)
    print()


    Eight_Puzzle.state_count = 0
    initial_time = time()
    astar_manhattan = a_star_manhattan(initial_state, goal_state)
    final_time = time() - initial_time
    print()
    print('A* Manhattan Heuristic:',astar_manhattan)
    print('Total Number of Moves Required:', len(astar_manhattan))
    print('Total Number of Search Tree Nodes Explored:', Eight_Puzzle.state_count)
    print('Time until Completion:', final_time)
    print()

if __name__ == "__main__":
    main()

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # A stack to store the nodes and paths (open list)
    frontier = util.Stack() 
    # A set to keep the explored nodes
    explored_nodes = set() 
    # This pushes the node to the fringe
    frontier.push((problem.getStartState(), [])) 
    while True:
        removed_element = frontier.pop()
        node = removed_element[0]
        path_found = removed_element[1]
        # Check if it is the goal state, if yes break
        if problem.isGoalState(node):  
            break
        else:
            if node not in explored_nodes:
                explored_nodes.add(node)
                successors = problem.getSuccessors(node)
                for successor in successors:
                    child_node = successor[0]
                    child_path = successor[1]
                    path_cost = path_found + [child_path]
                    frontier.push((child_node, path_cost))
    return path_cost
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # A queue to store the nodes (open list)
    frontier = util.Queue() 
    # A set to store all the explored nodes
    explored_nodes = set() 
    frontier.push((problem.getStartState(), []))
    while True:
        removed_element = frontier.pop()
        node = removed_element[0]
        path_found = removed_element[1]
        if problem.isGoalState(node):
            break
        else:
            if node not in explored_nodes:
                explored_nodes.add(node)
                successors = problem.getSuccessors(node)
                for successor in successors:
                    child_node = successor[0]
                    child_path = successor[1]
                    path_cost = path_found + [child_path]
                    frontier.push((child_node, path_cost))
    return path_found


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # Initialize a priority queue to store nodes with priorities
    frontier = util.PriorityQueue() 
    # A set to keep track of explored nodes
    explored_nodes = set()
    # Push the starting state onto the priority queue with a priority based on cost
    frontier.push((problem.getStartState(), [], 0),0)
    while True:
        # Remove and get the element with the highest priority from the priority queue
        removed_element = frontier.pop()
         # Extract node, path, and cost information from the removed element
        node = removed_element[0]
        path_found = removed_element[1]
        cost_found = removed_element[2]
        # Check if the current node is the goal state, break loop if it is
        if problem.isGoalState(node):
            break
        else:
            # If the node is not in the set of explored nodes, add it
            if node not in explored_nodes:
                explored_nodes.add(node)
                 # Get successors of the current node
                successors = problem.getSuccessors(node)
                # Iterate through the successors
                for successor in successors:
                    # Extract information about the successor
                    child_node = successor[0]
                    child_path = successor[1]
                    child_cost = successor[2]
                    # Create the full path by appending the child path to the current path
                    full_path = path_found + [child_path]
                     # Calculate the total cost of the path to the child node
                    path_cost = cost_found + child_cost
                    # Push the child node, full path, and total cost onto the priority queue with the calculated cost as priority
                    frontier.push((child_node, full_path, path_cost),path_cost)
    # Return the path found as the solution
    return path_found



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.

    Parameters:
    problem: The search problem to solve.
    heuristic: A function that estimates the cost from a given state to the goal.

    Returns:
    A list of actions that leads from the start state to a goal state.
    """

    # Initialize a priority queue for the frontier with nodes prioritized by their total cost (path cost + heuristic).
    frontier = util.PriorityQueue()

    # A set to keep track of explored (visited) nodes to avoid revisiting them.
    explored = set()

    # A dictionary to store the lowest cost found so far to reach each node.
    best_costs = {}

    # Get the start state of the problem and push it onto the frontier with its initial priority based on the heuristic.
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0), heuristic(start_state, problem))

    # Initialize the best cost to reach the start state as 0.
    best_costs[start_state] = 0

    # Loop until there are no more nodes in the frontier.
    while not frontier.isEmpty():
        # Pop the node with the lowest priority (total cost) from the frontier.
        node, path, cost = frontier.pop()

        # If the popped node is a goal state, return the path leading to it.
        if problem.isGoalState(node):
            return path

        # If the node hasn't been explored yet, mark it as explored.
        if node not in explored:
            explored.add(node)

            # Generate all successors of the node and iterate through them.
            for child_node, action, step_cost in problem.getSuccessors(node):
                # Calculate the new cost to reach the child node.
                new_cost = cost + step_cost

                # If the child node hasn't been visited or a lower cost path to it is found, update its cost.
                if child_node not in best_costs or new_cost < best_costs[child_node]:
                    best_costs[child_node] = new_cost  # Update the best cost to reach the child node.

                    # Calculate the priority of the child node by adding the new cost to its heuristic estimate.
                    priority = new_cost + heuristic(child_node, problem)

                    # Push the child node onto the frontier with its calculated priority and the path to reach it.
                    frontier.push((child_node, path + [action], new_cost), priority)

    # Return an empty list if no path to a goal state is found.
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

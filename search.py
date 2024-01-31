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
    "*** YOUR CODE HERE ***"
    frontier = util.Stack() # A stack to store the nodes and paths (open list)
    explored_nodes = set() # A set to keep the explored nodes
    frontier.push((problem.getStartState(), [])) # This pushes the node to the fringe
    while True:
        removed_element = frontier.pop()
        node = removed_element[0]
        path_found = removed_element[1]
        if problem.isGoalState(node):  # Check if it is the goal state, if yes break
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
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #print ("Start:" , problem.getStartState())
    
    "*** YOUR CODE HERE ***"
    frontier = util.Queue() # A queue to store the nodes (open list)
    explored_nodes = set() # A set to store all the explored nodes
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
    "*** YOUR CODE HERE ***"
    frontier = util.PriorityQueue() 
    explored_nodes = set()
    frontier.push((problem.getStartState(), [], 0),0)
    while True:
        removed_element = frontier.pop()
        node = removed_element[0]
        path_found = removed_element[1]
        cost_found = removed_element[2]
        if problem.isGoalState(node):
            break
        else:
            if node not in explored_nodes:
                explored_nodes.add(node)
                successors = problem.getSuccessors(node)
                for successor in successors:
                    child_node = successor[0]
                    child_path = successor[1]
                    child_cost = successor[2]
                    full_path = path_found + [child_path]
                    path_cost = cost_found + child_cost
                    frontier.push((child_node, full_path, path_cost),path_cost)
    return path_found



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

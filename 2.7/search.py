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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    # State = (x, y)
    # Action = 'North' | 'South' | 'East' | 'West'
    # Successor = (State, Action, Cost)
    # Successors = [Successor1, Successor2,...]
    
    # print(problem.getStartState())
    # print(problem.isGoalState(problem.getStartState()))
    # print(problem.getSuccessors(problem.getStartState()))
    
    # Start state
    first_state = problem.getStartState()
    first_node = {'state' : first_state, 
                  'path' : []}
    
    stack = util.Stack()
    stack.push(first_node)
    
    # DFS
    visited = []
    while not stack.isEmpty():
        current_node = stack.pop()
        if current_node['state'] not in visited:
            visited += [current_node['state']]
        else:
            continue
        if problem.isGoalState(current_node['state']):
            actions = current_node['path']
            break
        successor_nodes = problem.getSuccessors(current_node['state'])
        neighbor_nodes = [{'state' : ele[0],
                            'path' : current_node['path'] + [ele[1]]} for ele in successor_nodes]
        [stack.push(ele) for ele in neighbor_nodes]

    # print(actions)
    # print(problem.getCostOfActions(actions))
    return actions
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # State = (x, y)
    # Action = 'North' | 'South' | 'East' | 'West'
    # Successor = (State, Action, Cost)
    # Successors = [Successor1, Successor2,...]
    
    # print(problem.getStartState())
    # print(problem.isGoalState(problem.getStartState()))
    # print(problem.getSuccessors(problem.getStartState()))
    
    # Start state
    first_state = problem.getStartState()
    first_node = {'state' : first_state, 
                  'path' : []}
    
    queue = util.Queue()
    queue.push(first_node)
    
    # BFS
    visited = []
    while not queue.isEmpty():
        current_node = queue.pop()
        if current_node['state'] not in visited:
            visited += [current_node['state']]
        else:
            continue
        if problem.isGoalState(current_node['state']):
            actions = current_node['path']
            break
        successor_nodes = problem.getSuccessors(current_node['state'])
        neighbor_nodes = [{'state' : ele[0],
                            'path' : current_node['path'] + [ele[1]]} for ele in successor_nodes]
        [queue.push(ele) for ele in neighbor_nodes]
                    
    # print(actions)
    # print(problem.getCostOfActions(actions))
    return actions
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    # State = (x, y)
    # Action = 'North' | 'South' | 'East' | 'West'
    # Successor = (State, Action, Cost)
    # Successors = [Successor1, Successor2,...]
    
    # Start state
    first_state = problem.getStartState()
    first_node = {'state' : first_state, 
                  'path' : []}
    
    heap = util.PriorityQueue() # Min-Heap
    heap.push(first_node, problem.getCostOfActions(first_node['path']))

    # UCS
    visited = []
    while not heap.isEmpty():
        current_node = heap.pop()
        if current_node['state'] not in visited:
            visited += [current_node['state']]
        else:
            continue
        if problem.isGoalState(current_node['state']):
            actions = current_node['path']
            break
        successor_nodes = problem.getSuccessors(current_node['state'])
        neighbor_nodes = [{'state' : ele[0],
                            'path' : current_node['path'] + [ele[1]]} for ele in successor_nodes]
        [heap.push(ele, problem.getCostOfActions(ele['path'])) for ele in neighbor_nodes]
                    
    # print(actions)
    # print(problem.getCostOfActions(actions))
    return actions
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # State = (x, y)
    # Action = 'North' | 'South' | 'East' | 'West'
    # Successor = (State, Action, Cost)
    # Successors = [Successor1, Successor2,...]
    
    # Start state
    first_state = problem.getStartState()
    first_node = {'state' : first_state, 
                  'path' : [],
                  'g' : 0,
                  'h' : heuristic(first_state, problem)}
    
    heap = util.PriorityQueue() # Min-Heap
    heap.push(first_node, first_node['g'] + first_node['h']) # f = g + h
        
    # A*
    visited = []
    while heap.isEmpty() == False:
        current_node = heap.pop()
        if current_node['state'] not in visited:
            visited += [current_node['state']]
        else:
            continue
        if problem.isGoalState(current_node['state']):
            actions = current_node['path']
            break
        successor_nodes = problem.getSuccessors(current_node['state'])
        neighbor_nodes = [{'state' : ele[0],
                           'path' : current_node['path'] + [ele[1]],
                           'g' : current_node['g'] + ele[2],
                           'h' : heuristic(ele[0], problem)} for ele in successor_nodes]
        [heap.push(ele, ele['g'] + ele['h']) for ele in neighbor_nodes]
                    
    # print(actions)
    # print(problem.getCostOfActions(actions))
    return actions
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
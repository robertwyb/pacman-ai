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
    
    stack = util.Stack()
    explored = []
    start = problem.getStartState()
    stack.push((start, []))    
    while not stack.isEmpty():
        cur = stack.pop()
        cur_pos = cur[0]
        cur_path = cur[1]
        # print cur
        # print cur[0]
        # print cur[1]
        # print "----"
        if cur_pos not in explored:
            explored.append(cur_pos)
            if problem.isGoalState(cur_pos):
                return cur_path
            succ = list(problem.getSuccessors(cur_pos))
            for i in succ:
                pos_i = i[0]
                dir_i = i[1]
                if pos_i not in explored:
                    path_i = cur_path + [dir_i]
                    stack.push((pos_i, path_i))
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    explored = []
    start = problem.getStartState()
    queue.push((start, []))
    while not queue.isEmpty():
        cur = queue.pop()
        cur_pos = cur[0]
        cur_path = cur[1]
        if cur_pos not in explored:
            explored.append(cur_pos)
            if problem.isGoalState(cur_pos):
                return cur_path
            succ = list(problem.getSuccessors(cur_pos))
            for i in succ:
                pos_i = i[0]
                dir_i = i[1]
                if pos_i not in explored:
                    path_i = cur_path + [dir_i]
                    queue.push((pos_i, path_i))
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pqueue = util.PriorityQueue()
    explored = []
    start = (problem.getStartState(), [], 0)
    pqueue.push(start, 0)

    while not pqueue.isEmpty():
        cur = pqueue.pop()
        # print cur
        cur_pos = cur[0]
        cur_path = cur[1]
        cur_cost = cur[2]
        if cur_pos not in explored:
            explored.append(cur_pos)
            if problem.isGoalState(cur_pos):
                return cur_path
            succ = list(problem.getSuccessors(cur_pos))
            for i in succ:
                pos_i = i[0]
                dir_i = i[1]
                if i[0] not in explored:
                    path_i = cur_path + [dir_i]
                    cost_i = cur_cost + i[2]
                    start_i = (pos_i, path_i, cost_i)
                    pqueue.push(start_i, cost_i)
                    
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pqueue = util.PriorityQueue()
    explored = []
    start = (problem.getStartState(), [], 0)
    pqueue.push(start, 0)
    while not pqueue.isEmpty():
        cur = pqueue.pop()
        cur_pos = cur[0]
        cur_path = cur[1]
        cur_cost = cur[2]
        if cur_pos not in explored:
            explored.append(cur_pos)
            if problem.isGoalState(cur_pos):
                return cur_path
            succ = list(problem.getSuccessors(cur_pos))
            for i in succ:
            	# get heuristic cost and step cost
                pos_i = i[0]
                dir_i = i[1]
                h = heuristic(pos_i, problem)
                cost_i = cur_cost + i[2]
                total_cost = h + cost_i
                if i[0] not in explored:
                    path_i = cur_path + [dir_i]
                    # store position, path and cost without heuristic cost as new state
                    start_i = (pos_i, path_i, cost_i)
                    pqueue.push(start_i, total_cost)
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

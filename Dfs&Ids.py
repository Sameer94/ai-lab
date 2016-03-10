# 0 represent blank tile in puzzle
final = [0,3,6,1,4,7,2,5,8]

#displaying state in matrix form
def display( state ): 
    print " "
    print "| %d  %d  %d |" % (state[0], state[3], state[6])
    print "| %d  %d  %d |" % (state[1], state[4], state[7])
    print "| %d  %d  %d |" % (state[2], state[5], state[8])
    

#up movement in matrix
def up( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [0, 3, 6]: # checking if it is not first row
         #swaping with blank tile
         temp = new_state[index - 1]
         new_state[index - 1] = new_state[index]
         new_state[index] = temp
         display( state )
         return new_state
    else:
        return None

#down movement in matrix
def down( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [2, 5, 8]: # checking if it is not last row
         #swaping with blank tile
         temp = new_state[index + 1]
         new_state[index + 1] = new_state[index]
         new_state[index] = temp
         display( new_state )
         return new_state
    else:
        return None

#left movement in matrix
def left( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [0, 1, 2]: #checking if it is not first column
             #swaping with blank tile
             temp = new_state[index - 3]
             new_state[index - 3] = new_state[index]
             new_state[index] = temp
             display( new_state )
             return new_state
    else:
        return None

#right movement in matrix
def right( state ):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [6, 7, 8]: #checking if for last column in matrix
         #swaping with blank tile
         temp = new_state[index + 3]
         new_state[index + 3] = new_state[index]
         new_state[index] = temp
         display( new_state )
         return new_state
    else:
        return None

def create_node( state, parent, operator, depth, cost ):
    return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
    expanded_nodes = []
    expanded_nodes.append( create_node( up( node.state ), node, "u", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( down( node.state ), node, "d", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( left( node.state ), node, "l", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( right( node.state), node, "r", node.depth + 1, 0 ) )
    expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
    return expanded_nodes

def dfs( start, goal, depth=10 ):
    
    depth_limit = depth
    nodes = []
    
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        if len( nodes ) == 0: return None
        node = nodes.pop(0)
        if node.state == goal:
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.operator)
                if temp.depth <= 1: break
                temp = temp.parent
            return moves				
        if node.depth < depth_limit:
            expanded_nodes = expand_node( node, nodes )
            expanded_nodes.extend( nodes )
            nodes = expanded_nodes

def ids( start, goal, depth=50 ):
    for i in range( depth ):
        result = dfs( start, goal, i )
        if result != None:
            return result


class Node:
    def __init__( N, state, parent, operator, depth, cost ):
        N.state = state
        N.parent = parent
        N.operator = operator
        N.depth = depth
        N.cost = cost


start = [3,4,0,2,7,6,5,1,8]
result = dfs( start,final ) # for ids replace ids with dfs
if result == None:
    print "Soultion Not Found"
elif result == [None]:
    print "Start node was the final goal"
else:
    print result
    print len(result), " no of moves"
    
display(final)


'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    
    This function describes the relationship that two users have with each other.
    
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data 
        
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed_by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    
    This function evaluates a tic tac toe board and returns the winner.
    
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
        
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    hw = 0
    vw = 0
    dw = 0
    
    #horizontal wins
    for i in range(len(board)):
        h = board[i][0]
        for j in range(len(board)):
            if h == board[i][j]:
                hw +=1
        if hw == len(board):
            return h
        else:
            hw = 0
        
    #vertical wins
    for i in range(len(board)):
        v = board[0][i]
        for j in range(len(board)):
            if v == board[j][i]:
                vw +=1
        if vw == len(board):
            return v
        else:
            vw = 0
               
    #diagonal wins
    for i in range(len(board)):
        d = board [0][0]
        if d == board [i][i]:
            dw +=1
    if dw == len(board):
        return d
    else:
        dw = 0
        
    k = len(board)
    for i in range(len(board)):   
        d = board [0][len(board)-1]
        k -= 1
        if d == board [i][k]:
            dw +=1
        
    if dw == len(board):
        return d
    else:
        dw = 0        
    
        return print("NO WINNER")

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
        
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    total_time = 0
    routes = []
    
    #between proper pair in the same subset dictionary
    route = [i for i in route_map.keys() if i[0] == first_stop]
    if route[0][0] == first_stop and route[0][1] == second_stop:
        return route_map[route[0]]['travel_time_mins']
    
    various_routes = [i for i in route_map.keys()]

    #array of needed pairs whether starting from first stop or second stop
    for i in range(len(route_map)):
        if first_stop == various_routes[i][0]:
            for j in range(i, len(route_map)):
                routes.append(various_routes[j])
                
    #turning the array given ^ to sovle for the time
    for i in range(len(route_map)):
        if second_stop == routes[i][1]:
            for j in range(i,-1,-1):
                total_time += route_map[routes[j]]['travel_time_mins']
            return total_time 

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team No Ls' # Only 10 chars displayed.
strategy_name = 'Fair Game'
strategy_description = 'So if they are down and we are not then we will collude. But if we are down then we will dig ourselves out of a hole and betray.'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if my_score < -500: 
        return 'b'
    elif their_score < -1000: 
        return 'c'
    elif my_score < -500 and their_score < -1000:
        return 'b'
    else:
        return 'b'

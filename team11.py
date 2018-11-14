####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Win' # Only 10 chars displayed.
strategy_name = 'innocent till proven guilty'
strategy_description = 'If our teams score is a negative number then we will betray, if we have a positive number or a zero then we will collude'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    if len(my_score)<0:
        return 'b'
    elif len(my_score)==0:
        return 'c'
    else:
        return 'c'
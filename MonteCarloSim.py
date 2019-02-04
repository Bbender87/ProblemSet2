import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numTrue = 0
    for i in range(numTrials):
        if oneTrial():
            numTrue+=1
    return float(numTrue) /float(numTrials)   
            
def oneTrial():
    
    hand  = []
    bucket = ['G', 'G', 'G', 'R', 'R', 'R',]
    for pick in range(3):
        ball = random.choice(bucket)  
        bucket.remove(ball)
        hand.append(ball)
    if hand[0] == hand[1] and hand[1] == hand[2]:
        return True
    return False
            
             
        

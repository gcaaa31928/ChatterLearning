# ChatterLearning

**ChatterLearning** is automatic reply bot, it's can reply any text if it had data in, and it machine-learning based engine build in **Python** which can generate answers to those unkown questions.



## Installation
    MongoDB needed
    
    


    pip install chatterLearning
    
    from chatter_learning import Chatter
    
    chatter = Chatter()
    
    while True:
        testVar = raw_input()
        print chatter.response_to(testVar)



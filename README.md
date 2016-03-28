# ChatterLearning

**ChatterLearning** is automatic reply bot, it's can reply any text if it had data in, and it machine-learning based engine build in **Python** which can generate answers to those unkown questions.



## Installation
Python 2.7
MongoDB needed
    
    


    pip install chatterLearning
    
    from chatter_learning import Chatter
    
    chatter = Chatter(database_url='mongodb://localhost:27017')
    
    while True:
        testVar = raw_input()
        print chatter.response_to(testVar)



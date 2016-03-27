import os
from chatter_learning import Chatter

chatter = Chatter()

while True:
    testVar = raw_input()
    print chatter.response_to(testVar)
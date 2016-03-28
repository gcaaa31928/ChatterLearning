import sys

import os
from chatter_learning import Chatter

chatter = Chatter()

while True:
    testVar = raw_input().decode(sys.stdin.encoding)
    print chatter.response_to(testVar)
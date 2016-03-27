from chatter_learning import Chatter

chatter = Chatter(dict_path='../chatter_learning/dict.txt.big')

while True:
    testVar = raw_input()
    print chatter.response_to(testVar)
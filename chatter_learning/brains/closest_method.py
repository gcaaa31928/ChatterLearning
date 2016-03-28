import os
from chatter_learning.brains import BaseBrain
import jieba
import jieba.analyse
from chatter_learning.brains.pick_strategy import PickStrategy
from chatter_learning.store_adapters import Mongodb
from fuzzywuzzy import process
import itertools

class ClosestMethod(BaseBrain):

    def __init__(self,  **kwargs):
        dir = "%s/dict.txt.big" % os.path.dirname(__file__)
        dict_path = kwargs.get('dict_path', dir)
        jieba.load_userdict(dict_path)

    def set_store(self, store):
        self.store = store

    def drop_store(self):
        self.store.drop()

    def process(self, input):
        highest_weight = jieba.analyse.extract_tags(input, withWeight=True)
        if len(highest_weight) == 0:
            highest_weight_word = input
        else:
            highest_weight_word = highest_weight[0][0]
        # highest weight word
        available_conversations = self.store.filter(highest_weight_word)

        # can't find any conversations, just return random one
        if len(available_conversations) == 0:
            all_answers_list = self.store.list_answers()
            # none of data
            if len(all_answers_list) == 0:
                return 1, input
            return 1, PickStrategy.get_random(self.store.list_answers())

        ask_list = []
        for conversation in available_conversations:
            ask_list.append(conversation['ask'])

        closest_ask, confidence = process.extract(input, ask_list, limit=2)[0]
        confidence /= 100.0

        result = [s for s in available_conversations if s['ask'] == closest_ask][0]
        return confidence, PickStrategy.get_random(result['answers'])





from chatter_learning.brains import BaseBrain
import jieba
import jieba.analyse
from chatter_learning.store_adapters import Mongodb
import itertools

class ClosestMean(BaseBrain):

    def __init__(self,  **kwargs):
        jieba.load_userdict('../../dicts/dict.txt.big')
        self.set_store(kwargs.get('store_adapter', 'Mongodb'), **kwargs)

    def set_store(self, store_name, **kwargs):
        if store_name == 'Mongodb':
            self.store = Mongodb(**kwargs)

    def drop_store(self):
        self.store.drop()

    def process(self, input):
        highest_weight = jieba.analyse.extract_tags(input, withWeight=True)[0]
        # highest weight word
        available_conversations = self.store.filter(highest_weight[0])
        ask_list = []
        for conversation in available_conversations:
            ask_list.append(conversation['ask'])

        total_similarity = 0
        highest_similarity = 0
        closest_ask = None
        for ask in ask_list:
            similarity =  self.get_similarity(ask, input)
            print similarity
            total_similarity += similarity
            if similarity > highest_similarity:
                highest_similarity = similarity
                closest_ask = ask
        try:
            confidence = highest_similarity * 1.0 / total_similarity
        except:
            confidence = 0
        result = [s for s in available_conversations if s['ask'] == closest_ask]
        return confidence, result[0]

    def get_similarity(self, string1, string2):
        segments_list1 = jieba.cut(string1, cut_all=False)
        segments_list2 = jieba.cut(string2, cut_all=False)
        total = 0
        for combination in itertools.product(*[segments_list1, segments_list2]):
            if combination[0] == combination[1]:
                total += 1
        return total



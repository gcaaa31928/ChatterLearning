from chatter_learning.brains import BaseBrain
import jieba
from chatter_learning.store_adapters import Mongodb


class ClosetMean(BaseBrain):

    def __init__(self,  **kwargs):
        jieba.load_userdict('../dicts/dict.txt.big')
        self.set_store(kwargs.get('store_adapter', 'Mongodb'), **kwargs)

    def set_store(self, store_name, **kwargs):
        if store_name == 'Mongodb':
            self.store = Mongodb(**kwargs)

    def process(self, input):
        segments_list = jieba.cut(input, cut_all=True)

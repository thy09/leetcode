#! encoding=utf-8

# Creation Date: 2017-04-03 13:44:58
# Created By: Heyi Tang

from p460_lfu_cache import LFUCache
from p146_lru_cache import LRUCache
import json

if __name__ == "__main__":
    funcs = json.load(open("funcs.in"))
    vals = json.load(open("vals.in"))
    print len(vals)
    for func, val in zip(funcs, vals):
        if func == "LFUCache":
            cache = LFUCache(val[0])
        elif func == "LRUCache":
            cache = LRUCache(val[0])
        else:
            print getattr(cache, func)(*val)


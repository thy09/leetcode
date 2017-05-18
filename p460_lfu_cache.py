#! encoding=utf-8

# Creation Date: 2017-04-03 12:45:07
# Created By: Heyi Tang

class LinkedListNode(object):
    def __init__(self, value, key = None):
        self.value = value
        self.freq = 0
        self.next = self.prev = None
        self.key = key

    def insert_after(self, node):
        self.remove()

        next_node = node.next
        if next_node is not None:
            next_node.prev = self
        self.next = next_node

        self.prev = node
        node.next = self

    def remove(self):
        next_node = self.next
        prev_node = self.prev

        if next_node is not None:
            next_node.prev = prev_node

        if prev_node is not None:
            prev_node.next = next_node

    def show(self):
        node = self
        vals = []
        while node is not None:
            vals.append((node.key, node.value, node.freq))
            node = node.next
        #print vals

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.size = 0

        self.cache_list = [self.init_list(0)]
        self.max_freq = 0
        self.key2node = {}
    
    def show(self):
        for head, tail in self.cache_list:
            head.show()
    
    def full(self):
        return self.size >= self.cap
    
    def invalidate(self):
        #print "Invalidating"
        idx = 0
        for head, tail in self.cache_list:
            idx += 1
            if head.next == tail:
                continue
            print "Invalidating ", idx
            to_remove = head.next
            to_remove.remove()
            self.key2node.pop(to_remove.key)
            break
        self.size -= 1
    
    def init_list(self, freq):
        head = LinkedListNode("Head%d" % freq)
        tail = LinkedListNode("Tail%d" % freq)
        tail.insert_after(head)
        return (head, tail)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.key2node:
            result = -1
        else:
            node = self.key2node[key]
            result = node.value
            node.freq += 1
            self.insert_to_freq(node.freq, node)
        return result

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0:
            return
        node = self.key2node.get(key)
        if node:
            node.value = value
            self.get(key)
            return
        if self.full():
            self.invalidate()
        node = LinkedListNode(value, key)
        node.insert_after(self.cache_list[0][1].prev)
        self.key2node[key] = node
        self.size += 1
        #self.show() 
    
    def insert_to_freq(self, freq, node):
        max_freq = len(self.cache_list) - 1
        while freq > max_freq:
            max_freq += 1
            self.cache_list.append(self.init_list(max_freq))
        node.insert_after(self.cache_list[freq][1].prev)
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

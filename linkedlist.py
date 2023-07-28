class Linkedlist:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

    def addfirst(self, item):
        self._head = ListNode(item, self._head)
    
    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        
        return item


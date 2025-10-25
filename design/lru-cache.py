class LRUCache:

    class LL:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.contains = 0
        self.dict = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:


        # if key not in list
        if key not in self.dict or self.dict[key] == None:
            return -1

        cur_node = self.dict[key]

        #if alrdy head, do nothing
        if self.head == cur_node:
            # print("ret head")
            return self.dict[key].value

        # #move guy to top, and stitch around him 
        #take my guy from middle and merge his prev & after
        cur_node.prev.next = cur_node.next
        if self.tail != cur_node:
            cur_node.next.prev = cur_node.prev
        else:
            self.tail = cur_node.prev


        # #set my (now out of linked list) guy to head
        cur_node.next = self.head
        cur_node.prev = None
        self.head.prev = cur_node
        self.head = cur_node


        # #I could ALSO just re-use put for this
        # self.contains -= 1
        # self.dict[key] = None
        # self.put(key, cur_node.value)

        # c = self.head
        # while c != None:
        #     print(c.key, end = '->')
        #     c = c.next
        # print("(post fetch updated order)")
        return self.dict[key].value
        

    def put(self, key: int, value: int) -> None:

        #if item alrdy in cache, and just changing value
        if key in self.dict and self.dict[key] != None:
            self.get(key)
            self.dict[key].value = value
            return

        #create node
        new_node = self.LL(key, value)
        self.dict[key] = new_node

        #first item is both tail and head
        if self.contains == 0:
            self.head = new_node
            self.tail = new_node

        #else add it as head only
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        #do we need to remove?
        if self.contains < self.capacity:
            c = self.head
            # while c != None:
            #     print(c.key, end = '->')
            #     c = c.next
            # print("post-insert of", key)

            self.contains += 1
            return

        #removing "LRU" item
        # print("    removing", self.tail.key, "for", key)
        self.tail.prev.next = None
        self.dict[self.tail.key] = None
        self.tail = self.tail.prev #abandon self.tail so it's dealloced

        c = self.head
        # while c != None:
        #     print(c.key, end = '->')
        #     c = c.next
        # print("post-insert of", key)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
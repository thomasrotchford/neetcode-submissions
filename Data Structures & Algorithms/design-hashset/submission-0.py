class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.__mainArr = [ListNode("dummy") for i in range(10000)]
        

    def add(self, key: int) -> None:

        index = key%len(self.__mainArr)

        current = self.__mainArr[index]

        while current.next:

            current = current.next

        if current.val != key:
            current.next = ListNode(key)
            print("added: ",key)


    def remove(self, key: int) -> None:

        index = key%len(self.__mainArr)

        current = self.__mainArr[index]

        while current.next:

            previous = current

            current = current.next

            if (current.val == key):

                previous.next = current.next

                del current
                print("removed: ",key)

                break

    def contains(self, key: int) -> bool:

        index = key%len(self.__mainArr)

        current = self.__mainArr[index]

        while current.next:

            current = current.next

            if (current.val == key):
                print("contains: ",key)
                return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
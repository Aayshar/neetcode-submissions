
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        hashmap = {}

        current = head
        while current:
            hashmap[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copy = hashmap[current]
            copy.next = hashmap.get(current.next)
            copy.random = hashmap.get(current.random)
            current = current.next

        return hashmap[head]


        
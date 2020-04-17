# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_value(l: ListNode):
            numbers = []
            while l !=None:
                numbers.append(l.val)
                l = l.next
            # print(numbers)
            # print(type(numbers[0]))
            reverse = reverse_numbers(numbers)
            return reverse

        def reverse_numbers(l: list) -> list:
            reverse = [l[len(l)-1-i] for i in range(len(l))]
            return reverse

        def calc(l:list) -> int:
            sum = 0
            for i in range(len(l)):
                sum += l[i] * 10**(len(l) - 1 - i)
            return sum

        def reverse_sum(x: int) -> int:
            str_x = str(x)
            reverse = ''
            for i in range(len(str_x)):
                reverse += str_x[len(str_x) - 1 - i]
                
            return reverse

        def numbers_2_nodes(str_x: str) -> ListNode:
            numbers = []
            # str_x = str(x)
            numbers = [int(str_x[i]) for i in range(len(str_x))]
            # print("numbers:", numbers)

            nodes = [ListNode(numbers[i]) for i in range(len(numbers))]

            for i in range(len(nodes)):
                if i < len(nodes) - 1:
                    nodes[i].next = nodes[i+1]
                else:
                    nodes[i].next = None
            return nodes[0]
        
        numlist_1, numlist_2 = get_value(l1), get_value(l2)
        s1, s2 = calc(numlist_1), calc(numlist_2)
        r = reverse_sum(s1+s2)
        node = numbers_2_nodes(r)

        return node
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_value(l: ListNode) -> int:
    value = 0
    tmp = l
    while tmp != None:
        # print("old_value:", value)
        value = value * 10 + tmp.val        
        # print("current digit:", tmp.val)
        # print("updated_value:", value)
        # print("----------------")
        tmp = tmp.next
    # value += value * 10 + tmp.val
    return value

            
def reverse(value: int) -> int:
    reverse = 0
    while value != 0:
        reverse = reverse * 10 + value%10
        value = value // 10
    return reverse

def value_2_reverse_ListNode(value:int) -> ListNode:
    l = [] # list of digits
    nodes = []
    my_list_node = ListNode(0)
    while value != 0:
        l.append(value%10)
        nodes.append(ListNode(value%10))
        value = value // 10
    for i in range(len(nodes)):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i+1]
        else:
            nodes[i].next = None
    return nodes[0]

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0:
            return l2
        elif l2.val == 0:
            return l1
        else:
            value1 = get_value(l1)
            value2 = get_value(l2)
            reverse_sum = reverse(value1) + reverse(value2)
            print(value1, value2)
            
            return value_2_reverse_ListNode(reverse_sum)


if __name__ == "__main__":
    # Input
    # [2,4,3]
    # [5,6,4]
    # Expect Output
    # [7,0,8]
    list_a = [0,4,3]
    list_b = [5,6,4]
    print(list_a, list_b)
    a1, a2, a3 = [ListNode(x) for x in list_a]
    b1, b2, b3 = [ListNode(x) for x in list_b]
    a1.next = a2
    a2.next = a3

    b1.next = b2
    b2.next = b3
    s = Solution()
    result = s.addTwoNumbers(a1,b1)
    print(result.val, result.next.val, result.next.next.val) # , result.next.val, result.next.next.val    

    # print(a1.val, a1.next.val, a1.next.next.val)
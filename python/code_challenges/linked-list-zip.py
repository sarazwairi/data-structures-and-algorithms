# code challenge 8:
def zipLists(list1, list2):
    if list1.head is None and list2.head is None:
        return None
    if list1.head is None:
        return list1
    if list2.head is None:
        return list2
    l1current=list1.head
    l1next=l1current.next
    l2current=list2.head
    l2next=l2current.next

    while l1next and l2next:
        l1current.next=l2current
        l2current.next=l1next
        l1current=l1next
        l2current=l2next
        l1next=l1next.next
        l2next=l2next.next

    if l1next is None and l2next is None:
        l1current.next=l2current
    elif l1next is not None:
        l1current.next=l2current
        l2current.next=l1next
    elif l2next is not None:
        l2current.next=l2current
    return list1

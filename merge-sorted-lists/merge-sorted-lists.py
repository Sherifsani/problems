def merge(list1, list2):
    res = listNode(-1)
    current = res
    
    while list1 != None and list2 != None:
        if list1.val < list2.val :
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1 != None:
        current.next = list1
    elif list2 != None:
        current.next = list2

        return res.next

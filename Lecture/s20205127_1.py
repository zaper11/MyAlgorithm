def sorted_list(lists):
    def merge(list1, list2):
        result = []
        while len(list1) > 0 or len(list2) > 0:
            if len(list1) > 0 and len(list2) > 0:
                if list1[0] <= list2[0]:
                    result.append(list1[0])
                    list1 = list1[1:]
                else:
                    result.append(list2[0])
                    list2 = list2[1:]
            elif len(list1) > 0:
                result.append(list1[0])
                list1 = list1[1:]
            elif len(list2) > 0:
                result.append(list2[0])
                list2 = list2[1:]
        return result

    if len(lists) == 0:
        return []
    if len(lists) == 1:
        return lists[0]

    while lists:
        if len(lists) <= 1:
            return lists[0]
        lists.append(merge(lists.pop(0),lists.pop(0)))

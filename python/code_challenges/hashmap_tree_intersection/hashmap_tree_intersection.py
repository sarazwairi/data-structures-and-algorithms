def tree_intersection(tree1,tree2):
    list1=tree1.in_order()
    list2=tree2.in_order()

    output=[]

    for i in list1:
        if i in list2:
            output.append(i)
    if output:
        return output
    else:
        return None



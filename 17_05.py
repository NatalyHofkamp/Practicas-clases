
def intercalar (l1,l2):
    l_new= []
    while len(l1)>0 and len(l2)>0:
        v_min1 = l1[0] 
        v_min2 = l2[0]
        if v_min1< v_min2:
                l_new.append(v_min1)
                del l1[0]
        elif v_min1 == v_min2 :
                l_new.append(v_min1)
                del l1[0]
                del l2[0]
        elif v_min2< v_min1:
                l_new.append(v_min2)
                del l2[0]
    if len(l1)>0:
        l_new += l1
    elif len(l2)>0:
        l_new+=l2
    print (l_new)
    
intercalar ([1,3,5,7,9,11],[0,2,4,6,8,10])
intercalar ([1,8,10],[0,2,4,6,8,10])

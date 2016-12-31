def time_to_deliver(num_packages, delivery_sequence):
    dict={}
    i =0
    res=1
    while i <num_packages:
        if delivery_sequence[i].split("-")[0] in dict:
            if int(delivery_sequence[i].split("-")[1]) == dict[delivery_sequence[i].split("-")[0]]:
                i+=1
            else: dict[delivery_sequence[i].split("-")[0]]+=1
        else: dict[delivery_sequence[i].split("-")[0]]=1
        res+=1
    return res

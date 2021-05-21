def func(list):
    rep_list = []
    for position in range(0,len(list)-1): 
        if list[position] == list[position + 1]:
            rep_list.append(list[position])
    if rep_list:
        return rep_list[0]
    else:
        print('No repeating element found')






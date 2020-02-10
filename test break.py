





list1 = [4, 6, 45, 87, 35, 17, 63, 654, 987, 63, 321]

list2 = [4, 6, 45, 87, 35, 17, 63, 654, 987, 63, 321]


i = 0
while i < len(list1):
    print("List 1    -  " + str(list1[i]))
    povtor = 0
    g = 0
    while g < len(list2):
        if list1[i] == list2[g]:
            povtor += 1

        g += 1
    if povtor > 1:
        print("есть" + str(povtor))
    i += 1

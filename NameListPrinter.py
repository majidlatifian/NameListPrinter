name_list = []
for i in range(0, 10):
    item = input()
    name_list.append(item)
for i in range( len(name_list) ):
    print( name_list[i].title() )
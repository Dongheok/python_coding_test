temp = input()
temp_list = list(temp)
temp_len = len(temp)

for i, x in enumerate(temp_list):
    num = int(x)
    gob = int(temp_len) - int(i)-1
    print('[', num*10**gob, ']')

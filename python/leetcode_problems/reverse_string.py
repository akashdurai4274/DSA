list = ['a','k','a','s','h']

def reverse_string(list):
    s = 0
    e = len(list) -1
    while(s < e):
        t = list[s]
        list[s] = list[e]
        list[e] = t
        s += 1
        e -= 1

reverse_string(list)    
print(list)


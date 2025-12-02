def square():
    print("Square")
    for i in range(5):
        for j in range(5):
            print("* ", end="")
        print()
    print()


def left_triangle():
    print("Left Triangle")
    for i in range(6):
        for j in range(i):
            print("* ", end="")
        print() 
    print()   

def left_triangle_numbers():
    print("Left Triangle with Numbers")
    for i in range(6):
        for j in range(i):
            print(f'{j + 1} ', end="")
        print() 
    print()   


def left_triangle_same_numbers():
    print("Left Triangle with Same Numbers")
    for i in range(1, 6):
        for j in range(i):
            print(f'{i} ', end="")
        print() 
    print()  

def reversed_right_triangle():
    print("Reversed Right Triangle")
    for i in range(1, 6):
        for j in range(6, i,-1):
            print('* ' , end="")
        print() 
    print()  

def reversed_right_triangle_numbers():
    print("Reversed Right Triangle with Numbers")
    for i in range(6):
        for j in range(1, 6 - i):
            print(f'{j} ' , end="")
        print() 
    print()  

def pyramid():
    n = 5
    print("Pyramid")
    for i in range(n):
        for k in range(n - i - 1):
            print(" ", end="")
        #stars
        for l in range(2 * i + 1):
            print("*", end="")
        print()
    print()


def tilt_pyramid():
    n = 5
    print("Tilt Pyramid")
    for i in range(n):
        #space
        for j in range(i):
            print(" ", end="")
        #star
        for k in range(2*n - (2*i + 1)):
            print("*",end="")
        print()
    print()


def diamond():
    n = 5
    print("Diamond")
    for i in range(2*n):
        if i < 2 * n // 2:
            for j in range(n - i - 1):
                print(" ", end="")
            #stars
            for k in range(2 * i + 1):
                print("*", end="")
            print()
        
        elif i >= 2 * n // 2:
              #space
            for l in range(i - n):
                print(" ", end="")
            #star
            for m in range(2*n - (2*(i - n) + 1)):
                print("*",end="")
            print()
    print()

def right_diamond():
    n = 5
    print("Right Diamond")
    for i in range(2 * n):
        if i < 2 * n // 2:
            for j in range(i):
                print("*", end="")
        elif i >= 2 * n // 2:
            for k in range(2*n - i):
                print("*", end="")
        print()
    print()

def right_triangle_zero_flip():
    start = 1
    print("right_triangle_zero_flip")
    for i in range(6):
        if i % 2 != 0: start = 1
        else: start = 0
        for j in range(i):
            print(start, end="")
            start = 1 - start
        print()
    print()

  


square()
left_triangle()
left_triangle_numbers()
left_triangle_same_numbers()
reversed_right_triangle()
reversed_right_triangle_numbers()
pyramid()
tilt_pyramid()
diamond()
right_diamond()
right_triangle_zero_flip()
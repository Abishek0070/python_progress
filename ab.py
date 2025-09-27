def fibonacci_sequence():
    try:
        N = int(input())
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    
    if N <= 0:
        
    elif N == 1:
        print(0)
        return
    
    
    a, b = 0, 1
    
   
    print(a, b, end=" ")
    
   
    for _ in range(2, N):
       
        c = a + b
       
        print(c, end=" ")
       
        a = b
        b = c


fibonacci_sequence()
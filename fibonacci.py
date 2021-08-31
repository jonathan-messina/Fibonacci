def fibonacci(n): 
    fib = [];
    first = 0;
    sec = 1;
    fib.append(first);
    fib.append(sec);
    if (n <= 0):
        fib = [];
    elif(n <= 1):
        fib = [0];
    else:
        while (len(fib) <= n):
            fib.append(fib[first] + fib[sec]);
            first += 1
            sec += 1
    return fib;
print(fibonacci(5))
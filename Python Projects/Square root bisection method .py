def square_rt_bisection_method(N,tolerance = 10**-7,max_iteration = 100):
    if N == 0:
        print ("The square root of N is 0")
   
    elif N == 1:
        print ("The square root of N is 1")

    elif N < 0:
        raise ValueError("Square root a negative number is not defined")

    else:
        
        low = 0
        high = N
        root = None
        
        for i in range (max_iteration):
            mid = (low + high)/2
            square_mid = mid**2

            if abs(square_mid - N) < tolerance:
                root = mid
                break

            elif square_mid - N < 0:
                low = mid

            elif square_mid - N > 0:
                high = mid        
    
        if root == None:
            print ("Unable to find root ,not within tolerance")
        else:
            print ("Root of N is", root)
            print ("Iterate",i+1, "times before within tolerance")

def main():
    N = int(input("Enter a number: "))
    root = square_rt_bisection_method(N)
main()

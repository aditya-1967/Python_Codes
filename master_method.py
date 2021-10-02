#!/usr/bin/env python3

import math


def master_method(a, b, k, p):
    if a >= 1 and b >= 1:

        if math.log(a,b) > k:
            print("theta(n^", math.log(a,b), ")")

        elif math.log(a,b) == k:
            if p > -1:
                print("theta(n^", k,  "log^",  (p+1), "n)")
            elif p == -1:
                print("theta(n^", k, "log(logn)")
            else:
                print("theta(n^", k)
        
        elif math.log(a,b) < k:
            if p >= 0:
                print("theta(n^", k, "log^", p, "n)")
            else:
                print("O(n^", k, ")")
    else:
        print("Masters Method cannot be applied")



print("Masters Method")
print("General Form: T(n) = aT(n/b) + theta(n^klog^(p)n)")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
k = float(input("Enter the value of k: "))
p = int(input("Enter the value of p: "))

master_method(a, b, k, p)





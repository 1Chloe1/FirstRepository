##################################################################
#
# HX-2025-05-17:
# Chloe and her dad
# tried the following code
# during a programming session
#
##################################################################

def tally(n):
    if (n==0):
        return 0
    else:
        return n + tally(n-1)

res = tally(3)
print("tally(3) =", res)

##################################################################

def factorial(n):
    if (n==0):
        return 1
    else:
        return n*factorial(n-1)

res = factorial(10)
print("factorial(10) =", res)

##################################################################

def power(x,n):
    if (n==0):
        return 1
    else:
        return x*power(x,n-1)

# recursion depth is O(n)
print("power(2,10) =", power(2,10))

##################################################################
#
# HX:
# This one seems to be
# too advanced for Chloe now.
#
def power2(x,n):
    if (n==0):
        return 1
    if (n==1):
        return x
    if (n%2==0):
        return power2(x*x, n//2)
    else:
        return x*power2(x*x, n//2)

# recursion depth is O(log(n))
print("power2(2,10) =", power2(2,1000))

##################################################################

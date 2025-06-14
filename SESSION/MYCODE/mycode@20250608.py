##################################################################
import sys
sys.setrecursionlimit(10000)
##################################################################

def isPrime(x):
    def helper(i):
        if i * i > x:
            return True
        else:
            if x % i > 0:
                return helper(i+1)
            else:
                return False
    if x<2:
      return False
    else:
      return helper(2)

print("isPrime(137) = " + str(isPrime(137)))
print("isPrime(727) = " + str(isPrime(727)))
print("isPrime(1111) = " + str(isPrime(1111)))
  
##################################################################

def hd(xs):
    return xs[0]
def tl(xs):
    return xs[1:]
def cons(x0, xs):
    xs.insert(0, x0); return xs
def nilq(xs):
    return len(xs)==0
def consq(xs):
    return len(xs)>=1

##################################################################

def rappend(xs, ys):
    if nilq(xs):
        return ys
    else:
        return rappend(tl(xs), cons(hd(xs), ys))

def reverse(xs):
    return rappend(xs, [])

xs = [0,1,2,3,4,5]
print("reverse(" + str(xs) + ") = " + str(reverse(xs)))

##################################################################
#
# HX: This one is written by CJX
# HX: The implementation is tail-recursive
# HX: Correct but impractical for a long list
#
def minusend(xs):
  if nilq(xs):
    return []
  else:
    return reverse(tl(reverse(xs)))

xs = [1,2,3,4,5]
print("minusend(" + str(xs) + ") = " + str(minusend(xs)))

#
# HX: The implementation is not tail-recursive
#
def minusend1(xs):
  if nilq(xs):
    return []
  elif len(xs)==1:
      return []
  else: # at least 2 elements in xs!
      return cons(hd(xs), minusend1(tl(xs)))

##################################################################

def last(xs):
    if nilq(xs):
        assert False
    else:
        if len(xs)==1:
            return hd(xs)
        else:
            return last(tl(xs))

xs = [1,2,3]
print("last(" + str(xs) + ") = " + str(last(xs)))

def list_split(xs):
    n2 = len(xs)//2
    def helper(xs, ys):
        if len(ys)==n2:
            return (reverse(ys), xs)
        else:
            return helper(tl(xs), cons(hd(xs), ys))
    return helper(xs, [])

xs = [1,2,3,4,5,6,7,8,9,10,11]
print("list_split(xs, []) = ", str(list_split(xs)))

# def splitlist(xs,ys):
#     if nilq(xs):
#         return ([], [])
#     else:
#         if len(xs)==len(ys):
#             return (xs,ys)
#         else:
#             if len(xs)==len(ys)+1:
#                 return (xs,ys)
#             else:
#                 return splitlist(minusend(xs), cons(last(xs),ys))

# xs = [1,2,3,4,5,6,7,8,9,10,11]
# print("splitlist(xs, []) = ", str(splitlist(xs, [])))

##################################################################

def list_altsplit(xs):
    ln = len(xs)
    if ln==0:
        return ([], [])
    elif ln==1:
        return ([hd(xs)], [])
    else:
        (ys, zs) = list_altsplit(tl(tl(xs)))
        return (cons(hd(xs), ys), cons(hd(tl(xs)), zs))

xs = [1,2,3,4,5,6,7,8,9,10,11]
print("list_altsplit(" + str(xs) + ") = ", str(list_altsplit(xs)))

##################################################################

##################################################################
import sys
sys.setrecursionlimit(10000)
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
# HX: Correct but impractical for a long list
#
def minusend(xs):
  if nilq(xs):
    return[]
  else:
    return reverse(tl(reverse(xs)))

xs = [1,2,3,4,5]
print("minusend(" + str(xs) + ") = " + str(minusend(xs)))

##################################################################

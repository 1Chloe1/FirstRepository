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

def list_map(xs, fopr):
    if nilq(xs):
        return []
    else:
        return cons(fopr(hd(xs)), list_map(tl(xs), fopr))

##################################################################

def list_forall(xs, test):
  if nilq(xs):
    return True
  else:
    return test(hd(xs)) and list_forall(tl(xs), test)

xs = [1,3,5,7,9]
print("odd$forall(", xs, ") = ", list_forall(xs, lambda x: x % 2 != 0))

##################################################################

def list_exists(xs, test):
  if nilq(xs):
    return False
  else:
    return test(hd(xs)) or list_exists(tl(xs), test)

xs = [1,3,5,7,9]
print("even$exists(", xs, ") = ", list_exists(xs, lambda x: x % 2 == 0))

##################################################################

def append(xs, ys):
    if nilq(xs):
        return ys
    else:
        return cons(hd(xs), append(tl(xs), ys))

##################################################################

def rappend(xs, ys):
    if nilq(xs):
        return ys
    else:
        return rappend(tl(xs), cons(hd(xs), ys))

def reverse(xs):
    return rappend(xs, [])

##################################################################

def list_zip(xs,ys):
    if nilq(xs):
        return []
    if nilq(ys):
        return []
    x1 = hd(xs)
    y1 = hd(ys)
    return cons((x1,y1),list_zip(tl(xs),tl(ys)))

xs = [1,2,3]
ys = [4,5,6,7,8]
xys = list_zip(xs, ys)
print("list_zip(", xs, ";", ys, ") = ", "(", xys, ")")

##################################################################

def list_zip_trec(xs,ys):
    def helper(xs,ys,zs):
        if nilq(xs):
            return reverse(zs)
        if nilq(ys):
            return reverse(zs)
        else:
            x1 = hd(xs)
            y1 = hd(ys)
            return helper(tl(xs),tl(ys),cons((x1,y1),zs))

xs = [1,2,3]
ys = [4,5,6,7,8]
xys = list_zip(xs, ys)
print("list_zip_trec(", xs, ";", ys, ") = ", "(", xys, ")")

##################################################################

def list_unzip(xs):
  if nilq(xs):
    return ([], [])
  else:
    (y0,z0) = hd(xs)
    (ys,zs) = list_unzip(tl(xs))
    return (cons(y0,ys), cons(z0,zs))

xs = [(1,2),(3,4),(5,6)]
(ys, zs) = list_unzip(xs)
print("list_unzip(", xs, ") = ", "(", ys, ";", zs, ")")

##################################################################

def list_unzip_trec(xs):
    def helper(xs,ys,zs):
        if nilq(xs):
            return (reverse(ys), reverse(zs))
        else:
            (y1,z1) = hd(xs)
            return helper(tl(xs),cons(y1,ys),cons(z1,zs))
    return helper(xs,[],[])

xs = [(1,2),(3,4),(5,6)]
(ys, zs) = list_unzip_trec(xs)
print("list_unzip_trec(", xs, ") = ", "(", ys, ";", zs, ")")

##################################################################

def list_foldl(xs, r0, fopr):
    if nilq(xs):
        return r0
    else:
        return list_foldl(tl(xs), fopr(r0, hd(xs)), fopr)

def list_cross(xs, ys):
    return list_concat(list_map(xs, lambda x: list_map(ys, lambda y: (x, y))))
def list_reverse(xs):
    return list_rappend(xs, [])
def list_rappend(xs, ys):
    return list_foldl(xs, ys, lambda r0, x1: cons(x1, r0))
def list_concat(xss):
    return list_reverse(list_foldl(xss, [], lambda r0, xs: list_rappend(xs, r0)))

xs = [1, 2, 3]
ys = ["a", "b", "c"]
print("list_cross(", xs, ",", ys, ") = ", list_cross(xs, ys))

##################################################################

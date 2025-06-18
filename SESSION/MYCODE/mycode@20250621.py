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

# def llip(xs,ys):
#   if nilq(xs):
#     return reverse(ys)
#   else:
#     if nilq(tl(xs)):
#       return reverse(ys)
#     else:
#       if hd(xs) <= hd(tl(xs)):
#         return llip(tl(xs), cons(hd(xs),ys))
#       else:
#         return reverse(ys)

def llip_xrec(xs):
    if len(xs) <= 1:
        return xs
    ## len(xs) >= 2
    if hd(xs) <= hd(tl(xs)):
        return cons(hd(xs), llip_xrec(tl(xs)))
    else:
        return [hd(xs)]

xs = [1,2,3,1,3,1,3,1,2,3]
print("llip_xrec(xs) = ", llip_xrec(xs))

def llip_trec(xs):
    def helper(xs, ys):
        if nilq(xs):
            return reverse(ys)
        if nilq(ys):
            return helper(tl(xs), [hd(xs)])
        else:
            if hd(xs) >= hd(ys):
                return helper(tl(xs), cons(hd(xs), ys))
            else:
                return reverse(ys)
    return helper(xs, [])

xs = [1,2,3,1,3,1,3,1,2,3]
print("llip_trec(xs) = ", llip_trec(xs))

##################################################################

def llis(xs):
    if len(xs) <= 1:
        return xs
    else:
        res = llis(tl(xs))
        if len(res)==len(tl(xs)):
            if hd(xs)<=hd(tl(xs)):
                return xs
            else:
                return res
        else:
            return res

xs = [1,2,3,1,3,1,3,1,2,3]
print("llis(xs) = ", llis(xs))

##################################################################

def list_cross(xs,ys):
    if nilq(xs):
        return []
    if nilq(ys):
        return []
    def helper(x0, ys):
        if nilq(ys):
            return []
        else:
            return cons((x0, hd(ys)), helper(x0, tl(ys)))
    return append(helper(hd(xs),ys), list_cross(tl(xs),ys))

xs = [1, 2]
ys = ["a", "b", "c"]
print("list_cross(", xs, ",", ys, ") = ", list_cross(xs, ys))

##################################################################

# Permutation Generator algorithm

def perm(a,k,n):
    if(k==n):
        return a[1:n]
    else:
        for i in range(k,n):
            temp  = a[k]
            a[i] = temp
            perm(a,k+1,n)
            temp = a[k]
            a[k] = a[i]
            a[i] = temp

if __name__ == '__main__':
    a = perm([1,2,3,4,5],5,5)
    print(a)
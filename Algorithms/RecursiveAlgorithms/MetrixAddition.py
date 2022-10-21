def MetrixAddition(metrix1, metrix2,M,N):
    metrix3 =[[0,0,0],[0,0,0],[0,0,0]]
    for i in range (M):
        for j in range(N):
            metrix3[i][j] = metrix1[i][j] + metrix2[i][j]
    return metrix3


if __name__  == '__main__':
    a = [[1,2,3],[2,3,4],[4,5,6]]
    b = [[4,5,6],[1,2,3],[2,3,4]]
    M = 3
    N = 3
    c = MetrixAddition(a,b,3,3)
    for i in range (M):
        print("\t|",end="")
        for j in range (N):
            print("\t"+str(a[i][j]),end="")
        print("\t|\t")
        
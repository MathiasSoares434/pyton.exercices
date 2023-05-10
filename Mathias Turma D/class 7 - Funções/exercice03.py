def numpat(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(j+1, end=" ")
        num+=1

        print("\r")


n = 5
numpat(n)
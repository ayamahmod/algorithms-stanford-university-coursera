def Karatsuba(x, y):
    if(x < 10 or y < 10):
        return x*y;
    xStr = str(x)
    yStr = str(y)
    splitPos = int(max(len(xStr), len(yStr))/2)
    a, b = int(xStr[:-splitPos]), int(xStr[-splitPos:])
    c, d = int(yStr[:-splitPos]), int(yStr[-splitPos:])
    z0 = Karatsuba(b, d)
    z1 = Karatsuba(a + b, c + d)
    z2 = Karatsuba(a, c)
    return (z2 * 10 ** (2 * splitPos)) + ((z1 - z2 - z0) * 10 ** splitPos) + z0

def main():
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    print(Karatsuba(x, y))

if __name__ == "__main__":
    main()

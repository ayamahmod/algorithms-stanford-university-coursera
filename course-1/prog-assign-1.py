# In this programming assignment you will implement one or more of the integer
# multiplication algorithms described in lecture.  To get the most out of this
# assignment, your program should restrict itself to multiplying only pairs of
# single-digit numbers. You can implement the grade-school algorithm if you
# want, but to get the most out of the assignment you'll want to implement
# recursive integer multiplication and/or Karatsuba's algorithm.  So: what's the
# product of the following two 64-digit numbers?
# 3141592653589793238462643383279502884197169399375105820974944592
# 2718281828459045235360287471352662497757247093699959574966967627  [TIP: before
# submitting, first test the correctness of your program on some small test
# cases of your own devising. Then post your best test cases to the discussion
# forums to help your fellow students!]  [Food for thought: the number of digits
# in each input number is a power of 2. Does this make your life easier? Does it
# depend on which algorithm you're implementing?]  The numeric answer should be
# typed in the space below. So if your answer is 1198233847, then just type
# 1198233847 in the space provided without any space / commas / any other
# punctuation marks.  (We do not require you to submit your code, so feel free
# to use any programming language you want --- just type the final numeric
# answer in the following space.)
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

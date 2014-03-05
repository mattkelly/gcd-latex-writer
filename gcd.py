import sys

def print_latex_matrix(A, indent = '    '):
    sys.stdout.write("\n%s\\begin{pmatrix}\n" % indent)
    for i in range(len(A)):
        sys.stdout.write(indent)
        for j in range(len(A[0])):
            if j < len(A[0]) - 1:
                sys.stdout.write("%d & " % A[i][j])
            else:
                sys.stdout.write("%d" % A[i][j])
        if i == 0: sys.stdout.write(' \\\\\n')
    sys.stdout.write("\n%s\\end{pmatrix}" % indent)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = 6424608522503111
b = 3242940221833111 

d = gcd(a, b)

A = [[a, 1, 0],
     [b, 0, 1]]

sys.stdout.write('\\begin{multline*}')
print_latex_matrix(A)

i = 1
while A[0][0] != d and A[1][0] != d:
    if A[0][0] > A[1][0]:
        factor = A[0][0] // A[1][0]
        A[0] = [(A[0][j] - factor*A[1][j]) for j in range(len(A[0]))]
    else:
        factor = A[1][0] // A[0][0]
        A[1] = [(A[1][j] - factor*A[0][j]) for j in range(len(A[0]))]
    if i % 2 == 0:
        sys.stdout.write('\\\\')
    sys.stdout.write("\n    \\rightarrow")
    print_latex_matrix(A)
    i += 1

sys.stdout.write('\n\\end{multline*}\n')

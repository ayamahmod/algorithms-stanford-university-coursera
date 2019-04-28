# In this assignment you will implement one or more algorithms for the 2SAT
# problem. Here are 6 different 2SAT instances:
# 2sat1.txt
# 2sat2.txt
# 2sat3.txt
# 2sat4.txt
# 2sat5.txt
# 2sat6.txt
# The file format is as follows. In each instance, the number of variables and
# the number of clauses is the same, and this number is specified on the first
# line of the file. Each subsequent line specifies a clause via its two
# literals, with a number denoting the variable and a "-" sign denoting logical
# "not". For example, the second line of the first data file is "-16808 75250",
# which indicates the clause -16808∨75250.
# Your task is to determine which of the 6 instances are satisfiable, and which
# are unsatisfiable. In the box below, enter a 6-bit string, where the ith bit
# should be 1 if the ith instance is satisfiable, and 0 otherwise. For example,
# if you think that the first 3 instances are satisfiable and the last 3 are
# not, then you should enter the string 111000 in the box below.
# DISCUSSION: This assignment is deliberately open-ended, and you can implement
# whichever 2SAT algorithm you want. For example, 2SAT reduces to computing the
# strongly connected components of a suitable graph (with two vertices per
# variable and two directed edges per clause, you should think through the
# details). This might be an especially attractive option for those of you who
# coded up an SCC algorithm in Part 2 of this specialization. Alternatively, you
# can use Papadimitriou's randomized local search algorithm. (The algorithm from
# lecture is probably too slow as stated, so you might want to make one or more
# simple modifications to it --- even if this means breaking the analysis given
# in lecture --- to ensure that it runs in a reasonable amount of time.) A third
# approach is via backtracking. In lecture we mentioned this approach only in
# passing; see Chapter 9 of the Dasgupta-Papadimitriou-Vazirani book, for
# example, for more details.

## FIXME
def dfs(graph, s, visited, st):
    st2 = []
    st2.append(s)
    startTimes = set()
    while len(st2):
        v = st2[-1]
        if v not in startTimes: # first time
            visited.add(v)
            if v in graph:
                for v2 in graph[v]:
                    if v2 not in visited:
                        st2.append(v2)
            startTimes.add(v)
        else:
            st.append(v)
            st2.pop()

FILE_NAMES = ["2sat1.txt", "2sat2.txt", "2sat3.txt", "2sat4.txt", "2sat5.txt",
    "2sat6.txt"]

for fName in FILE_NAMES:
    sat = True
    f = open(fName)
    nVar = int(f.readline())
    lines = f.readlines()
    f.close()
    graph = {}
    for line in lines:
        v1, v2 = map(int, line.split()) # A v B
        # ^A => B
        if -v1 in graph:
            graph[-v1].append(v2)
        else:    graph[-v1] = [v2]
        # ^B => A
        if -v2 in graph:
            graph[-v2].append(v1)
        else:    graph[-v2] = [v1]
##################################################
    #1. DFS
    visited = set()
    st = []
    for v in graph:
        if v not in visited:
            dfs(graph, v, visited, st)
    #2. Reverse the graph
    tGraph = {}
    for v1 in graph:
        for v2 in graph[v1]:
            if v2 in tGraph:
                tGraph[v2].append(v1)
            else:    tGraph[v2] = [v1]
    #3. DFS again
    visited = set()
    while len(st):
        v = st.pop()
        if v not in visited:
            scc = []
            dfs(tGraph, v, visited, scc)
            scc = set(scc)
            for v in scc:
                if -v in scc:
                    sat = False
    print(sat)

# In this programming problem and the next you'll code up the greedy algorithms
# from lecture for minimizing the weighted sum of completion times..  This file
# describes a set of jobs with positive and integral weights and lengths. It has
# the format  [number_of_jobs]  [job_1_weight] [job_1_length]  [job_2_weight]
# [job_2_length]  ...  For example, the third line of the file is "74 59",
# indicating that the second job has weight 74 and length 59.  You should NOT
# assume that edge weights or lengths are distinct.  Your task in this problem
# is to run the greedy algorithm that schedules jobs in decreasing order of the
# difference (weight - length). Recall from lecture that this algorithm is not
# always optimal. IMPORTANT: if two jobs have equal difference (weight -
# length), you should schedule the job with higher weight first. Beware: if you
# break ties in a different way, you are likely to get the wrong answer. You
# should report the sum of weighted completion times of the resulting schedule ---
# a positive integer --- in the box below.  ADVICE: If you get the wrong answer,
# try out some small test cases to debug your algorithm (and post your test
# cases to the discussion forum).


# For this problem, use the same data set as in the previous problem.
#
# Your task now is to run the greedy algorithm that schedules jobs (optimally) in
# decreasing order of the ratio (weight/length). In this algorithm, it does not
# matter how you break ties. You should report the sum of weighted completion
# times of the resulting schedule --- a positive integer --- in the box below.

def comprTuple(element):
    return (element[0], element[1][0])

with open("jobs.txt") as f:
    content = f.readlines()
numOfJobs = int(content.pop(0).strip())
arr = []
for l in content:
    w, l = map(int, l.split())
    arr.append((w/l, (w, l))) # w-l
arr.sort(key = comprTuple, reverse = True)
sumWeighComp = 0
time = 0
for elem in arr:
    time += elem[1][1]
    sumWeighComp += elem[1][0] * time
print(sumWeighComp)

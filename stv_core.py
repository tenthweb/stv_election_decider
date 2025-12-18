from random import shuffle

candidates = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']
'''Generate 100 random ballots for 5 candidates'''

ballots = []

for i in range(100):
    preferences = list(range(1, len (candidates) + 1))
    shuffle(preferences)
    ballot = {candidates[j]: preferences[j] for j in range(len(candidates))}
    ballots.append(ballot)

print(ballots)


[{'Alice': 1, 'Bob': 2, 'Carol': 4, 'Dave': 5, 'Eve': 3}
 {'Alice': 4, 'Bob': 1, 'Carol': 2, 'Dave': 5, 'Eve': 3}
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 2, 'Eve': 3}
 {'Alice': 5, 'Bob': 1, 'Carol': 4, 'Dave': 3, 'Eve': 2}
 {'Alice': 1, 'Bob': 5, 'Carol': 2, 'Dave': 4, 'Eve': 3}
 {'Alice': 4, 'Bob': 1, 'Carol': 2, 'Dave': 3, 'Eve': 5}
 {'Alice': 1, 'Bob': 2, 'Carol': 5, 'Dave': 4, 'Eve': 3}
 {'Alice': 3, 'Bob': 5, 'Carol': 2, 'Dave': 4, 'Eve': 1}
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 3, 'Eve': 1}
 {'Alice': 1, 'Bob': 2, 'Carol': 3, 'Dave': 5, 'Eve': 4}
 {'Alice': 3, 'Bob': 4, 'Carol': 1, 'Dave': 5, 'Eve': 2}
 {'Alice': 5, 'Bob': 2, 'Carol': 3, 'Dave': 4, 'Eve': 1}
 {'Alice': 1, 'Bob': 5, 'Carol': 2, 'Dave': 3, 'Eve': 4}
 {'Alice': 5, 'Bob': 3, 'Carol': 1, 'Dave': 2, 'Eve': 4}
 {'Alice': 4, 'Bob': 2, 'Carol': 5, 'Dave': 1, 'Eve': 3}
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 3, 'Eve': 1}
 {'Alice': 3, 'Bob': 5, 'Carol': 2, 'Dave': 1, 'Eve': 4}
 {'Alice': 4, 'Bob': 1, 'Carol': 3, 'Dave': 2, 'Eve': 5}
 {'Alice': 5, 'Bob': 3, 'Carol': 2, 'Dave': 4, 'Eve': 1}
 {'Alice': 3, 'Bob': 5, 'Carol': 1, 'Dave': 2, 'Eve': 4}
 {'Alice': 5, 'Bob': 3, 'Carol': 2, 'Dave': 4, 'Eve': 1}
 {'Alice': 2, 'Bob': 5, 'Carol': 3, 'Dave': 1, 'Eve': 4}
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 2, 'Eve': 3}
 {'Alice': 2, 'Bob': 3, 'Carol': 4, 'Dave': 5, 'Eve': 1}
 {'Alice': 2, 'Bob': 5, 'Carol': 1, 'Dave': 3, 'Eve': 4}
 {'Alice': 1, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 5}
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 3, 'Eve': 1}
 {'Alice': 1, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 5}
 {'Alice': 2, 'Bob': 3, 'Carol': 4, 'Dave': 5, 'Eve': 1}
 {'Alice': 3, 'Bob': 5, 'Carol': 2, 'Dave': 1, 'Eve': 4}
 {'Alice': 2, 'Bob': 4, 'Carol': 1, 'Dave': 3, 'Eve': 5}
 {'Alice': 4, 'Bob': 2, 'Carol': 5, 'Dave': 1, 'Eve': 3}
 {'Alice': 2, 'Bob': 5, 'Carol': 3, 'Dave': 1, 'Eve': 4}
 {'Alice': 1, 'Bob': 2, 'Carol': 5, 'Dave': 4, 'Eve': 3}
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 3, 'Eve': 2}
 {'Alice': 3, 'Bob': 5, 'Carol': 1, 'Dave': 2, 'Eve': 4}
 {'Alice': 4, 'Bob': 1, 'Carol': 2, 'Dave': 3, 'Eve': 5}
 {'Alice': 2, 'Bob': 5, 'Carol': 3, 'Dave': 1, 'Eve': 4}
 {'Alice': 1, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 5}
 {'Alice': 1, 'Bob': 4, 'Carol': 3, 'Dave': 2, 'Eve': 5}
 {'Alice': 4, 'Bob': 5, 'Carol': 1, 'Dave': 3, 'Eve': 2}
 {'Alice': 1, 'Bob': 4, 'Carol': 2, 'Dave': 3, 'Eve': 5}
 {'Alice': 3, 'Bob': 1, 'Carol': 5, 'Dave': 4, 'Eve': 2}
 {'Alice': 5, 'Bob': 1, 'Carol': 4, 'Dave': 2, 'Eve': 3}
 {'Alice': 2, 'Bob': 3, 'Carol': 5, 'Dave': 4, 'Eve': 1}
 {'Alice': 5, 'Bob': 2, 'Carol': 3, 'Dave': 4, 'Eve': 1}
 {'Alice': 5, 'Bob': 1, 'Carol': 3, 'Dave': 4, 'Eve': 2}
 {'Alice': 3, 'Bob': 5, 'Carol': 4, 'Dave': 1, 'Eve': 2}
 {'Alice': 3, 'Bob': 4, 'Carol': 2, 'Dave': 5, 'Eve': 1}
 {'Alice': 2, 'Bob': 5, 'Carol': 3, 'Dave': 4, 'Eve': 1}
 {'Alice': 2, 'Bob': 5, 'Carol': 4, 'Dave': 1, 'Eve': 3}
 {'Alice': 3, 'Bob': 2, 'Carol': 5, 'Dave': 1, 'Eve': 4}
 {'Alice': 1, 'Bob': 3, 'Carol': 5, 'Dave': 4, 'Eve': 2}
 {'Alice': 2, 'Bob': 1, 'Carol': 5, 'Dave': 4, 'Eve': 3}
 {'Alice': 1, 'Bob': 5, 'Carol': 4, 'Dave': 2, 'Eve': 3}
 {'Alice': 2, 'Bob': 4, 'Carol': 1, 'Dave': 3, 'Eve': 5}
 {'Alice': 1, 'Bob': 5, 'Carol': 2, 'Dave': 4, 'Eve': 3}
 {'Alice': 1, 'Bob': 4, 'Carol': 5, 'Dave': 2, 'Eve': 3}
 {'Alice': 4, 'Bob': 3, 'Carol': 5, 'Dave': 2, 'Eve': 1}
 {'Alice': 5, 'Bob': 2, 'Carol': 3, 'Dave': 1, 'Eve': 4}
 {'Alice': 5, 'Bob': 4, 'Carol': 1, 'Dave': 3, 'Eve': 2}
 {'Alice': 1, 'Bob': 2, 'Carol': 3, 'Dave': 5, 'Eve': 4}
 {'Alice': 4, 'Bob': 1, 'Carol': 3, 'Dave': 2, 'Eve': 5}
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 3, 'Eve': 2}
 {'Alice': 2, 'Bob': 4, 'Carol': 3, 'Dave': 1, 'Eve': 5}
 {'Alice': 3, 'Bob': 5, 'Carol': 1, 'Dave': 2, 'Eve': 4}
 {'Alice': 4, 'Bob': 5, 'Carol': 1, 'Dave': 3, 'Eve': 2}
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 1, 'Eve': 3}
 {'Alice': 2, 'Bob': 3, 'Carol': 5, 'Dave': 1, 'Eve': 4}
 {'Alice': 3, 'Bob': 2, 'Carol': 4, 'Dave': 1, 'Eve': 5}
 {'Alice': 1, 'Bob': 2, 'Carol': 5, 'Dave': 3, 'Eve': 4}
 {'Alice': 1, 'Bob': 2, 'Carol': 3, 'Dave': 5, 'Eve': 4}
 {'Alice': 4, 'Bob': 5, 'Carol': 2, 'Dave': 1, 'Eve': 3}
 {'Alice': 5, 'Bob': 2, 'Carol': 3, 'Dave': 4, 'Eve': 1}
 {'Alice': 1, 'Bob': 2, 'Carol': 4, 'Dave': 3, 'Eve': 5}
 {'Alice': 1, 'Bob': 5, 'Carol': 3, 'Dave': 4, 'Eve': 2}
 {'Alice': 4, 'Bob': 3, 'Carol': 1, 'Dave': 5, 'Eve': 2}
 {'Alice': 3, 'Bob': 4, 'Carol': 5, 'Dave': 2, 'Eve': 1}
 {'Alice': 3, 'Bob': 4, 'Carol': 1, 'Dave': 2, 'Eve': 5}
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 1, 'Eve': 3}
 {'Alice': 5, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 1}
 {'Alice': 3, 'Bob': 5, 'Carol': 2, 'Dave': 1, 'Eve': 4}
 {'Alice': 1, 'Bob': 5, 'Carol': 4, 'Dave': 3, 'Eve': 2}
 {'Alice': 5, 'Bob': 2, 'Carol': 4, 'Dave': 3, 'Eve': 1}
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 3, 'Eve': 2}
 {'Alice': 5, 'Bob': 3, 'Carol': 1, 'Dave': 4, 'Eve': 2}
 {'Alice': 3, 'Bob': 2, 'Carol': 5, 'Dave': 1, 'Eve': 4}
 {'Alice': 1, 'Bob': 5, 'Carol': 4, 'Dave': 3, 'Eve': 2}
 {'Alice': 5, 'Bob': 1, 'Carol': 4, 'Dave': 2, 'Eve': 3}
 {'Alice': 1, 'Bob': 4, 'Carol': 2, 'Dave': 3, 'Eve': 5}
 {'Alice': 5, 'Bob': 1, 'Carol': 2, 'Dave': 4, 'Eve': 3}
 {'Alice': 3, 'Bob': 5, 'Carol': 1, 'Dave': 2, 'Eve': 4}
 {'Alice': 1, 'Bob': 3, 'Carol': 4, 'Dave': 5, 'Eve': 2}
 {'Alice': 3, 'Bob': 1, 'Carol': 5, 'Dave': 2, 'Eve': 4}
 {'Alice': 5, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 1}
 {'Alice': 4, 'Bob': 2, 'Carol': 1, 'Dave': 3, 'Eve': 5}
 {'Alice': 3, 'Bob': 4, 'Carol': 1, 'Dave': 5, 'Eve': 2}
 {'Alice': 2, 'Bob': 1, 'Carol': 5, 'Dave': 3, 'Eve': 4}
 {'Alice': 2, 'Bob': 3, 'Carol': 4, 'Dave': 5, 'Eve': 1}
 {'Alice': 2, 'Bob': 3, 'Carol': 1, 'Dave': 4, 'Eve': 5}]


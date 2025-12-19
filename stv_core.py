


from random import shuffle

seat_number = 3

candidates = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']

total_candidates = len(candidates)



'''Generate 100 random ballots for 5 candidates'''

'''
ballots = []

for i in range(100):
    preferences = list(range(1, len (candidates) + 1))
    shuffle(preferences)
    ballot = {candidates[j]: preferences[j] for j in range(len(candidates))}
    ballots.append(ballot)

print(ballots)
'''

ballots = [
{'Alice': 1, 'Bob': 2, 'Carol': 4, 'Dave': 5, 'Eve': 3},
 {'Alice': 4, 'Bob': 1, 'Carol': 2, 'Dave': 5, 'Eve': 3},
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 2, 'Eve': 3},
 {'Alice': 5, 'Bob': 1, 'Carol': 4, 'Dave': 3, 'Eve': 2},
 {'Alice': 1, 'Bob': 5, 'Carol': 2, 'Dave': 4, 'Eve': 3},
 {'Alice': 4, 'Bob': 1, 'Carol': 2, 'Dave': 3, 'Eve': 5},
 {'Alice': 1, 'Bob': 2, 'Carol': 5, 'Dave': 4, 'Eve': 3},
 {'Alice': 3, 'Bob': 5, 'Carol': 2, 'Dave': 4, 'Eve': 1},
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 3, 'Eve': 1},
 {'Alice': 1, 'Bob': 2, 'Carol': 3, 'Dave': 5, 'Eve': 4},
 {'Alice': 3, 'Bob': 4, 'Carol': 1, 'Dave': 5, 'Eve': 2},
 {'Alice': 5, 'Bob': 2, 'Carol': 3, 'Dave': 4, 'Eve': 1},
 {'Alice': 1, 'Bob': 5, 'Carol': 2, 'Dave': 3, 'Eve': 4},
 {'Alice': 5, 'Bob': 3, 'Carol': 1, 'Dave': 2, 'Eve': 4},
 {'Alice': 4, 'Bob': 2, 'Carol': 5, 'Dave': 1, 'Eve': 3},
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 3, 'Eve': 1},
 {'Alice': 3, 'Bob': 5, 'Carol': 2, 'Dave': 1, 'Eve': 4},
 {'Alice': 4, 'Bob': 1, 'Carol': 3, 'Dave': 2, 'Eve': 5},
 {'Alice': 5, 'Bob': 3, 'Carol': 2, 'Dave': 4, 'Eve': 1},
 {'Alice': 3, 'Bob': 5, 'Carol': 1, 'Dave': 2, 'Eve': 4},
 {'Alice': 5, 'Bob': 3, 'Carol': 2, 'Dave': 4, 'Eve': 1},
 {'Alice': 2, 'Bob': 5, 'Carol': 3, 'Dave': 1, 'Eve': 4},
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 2, 'Eve': 3},
 {'Alice': 2, 'Bob': 3, 'Carol': 4, 'Dave': 5, 'Eve': 1},
 {'Alice': 2, 'Bob': 5, 'Carol': 1, 'Dave': 3, 'Eve': 4},
 {'Alice': 1, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 5},
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 3, 'Eve': 1},
 {'Alice': 1, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 5},
 {'Alice': 2, 'Bob': 3, 'Carol': 4, 'Dave': 5, 'Eve': 1},
 {'Alice': 3, 'Bob': 5, 'Carol': 2, 'Dave': 1, 'Eve': 4},
 {'Alice': 2, 'Bob': 4, 'Carol': 1, 'Dave': 3, 'Eve': 5},
 {'Alice': 4, 'Bob': 2, 'Carol': 5, 'Dave': 1, 'Eve': 3},
 {'Alice': 2, 'Bob': 5, 'Carol': 3, 'Dave': 1, 'Eve': 4},
 {'Alice': 1, 'Bob': 2, 'Carol': 5, 'Dave': 4, 'Eve': 3},
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 3, 'Eve': 2},
 {'Alice': 3, 'Bob': 5, 'Carol': 1, 'Dave': 2, 'Eve': 4},
 {'Alice': 4, 'Bob': 1, 'Carol': 2, 'Dave': 3, 'Eve': 5},
 {'Alice': 2, 'Bob': 5, 'Carol': 3, 'Dave': 1, 'Eve': 4},
 {'Alice': 1, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 5},
 {'Alice': 1, 'Bob': 4, 'Carol': 3, 'Dave': 2, 'Eve': 5},
 {'Alice': 4, 'Bob': 5, 'Carol': 1, 'Dave': 3, 'Eve': 2},
 {'Alice': 1, 'Bob': 4, 'Carol': 2, 'Dave': 3, 'Eve': 5},
 {'Alice': 3, 'Bob': 1, 'Carol': 5, 'Dave': 4, 'Eve': 2},
 {'Alice': 5, 'Bob': 1, 'Carol': 4, 'Dave': 2, 'Eve': 3},
 {'Alice': 2, 'Bob': 3, 'Carol': 5, 'Dave': 4, 'Eve': 1},
 {'Alice': 5, 'Bob': 2, 'Carol': 3, 'Dave': 4, 'Eve': 1},
 {'Alice': 5, 'Bob': 1, 'Carol': 3, 'Dave': 4, 'Eve': 2},
 {'Alice': 3, 'Bob': 5, 'Carol': 4, 'Dave': 1, 'Eve': 2},
 {'Alice': 3, 'Bob': 4, 'Carol': 2, 'Dave': 5, 'Eve': 1},
 {'Alice': 2, 'Bob': 5, 'Carol': 3, 'Dave': 4, 'Eve': 1},
 {'Alice': 2, 'Bob': 5, 'Carol': 4, 'Dave': 1, 'Eve': 3},
 {'Alice': 3, 'Bob': 2, 'Carol': 5, 'Dave': 1, 'Eve': 4},
 {'Alice': 1, 'Bob': 3, 'Carol': 5, 'Dave': 4, 'Eve': 2},
 {'Alice': 2, 'Bob': 1, 'Carol': 5, 'Dave': 4, 'Eve': 3},
 {'Alice': 1, 'Bob': 5, 'Carol': 4, 'Dave': 2, 'Eve': 3},
 {'Alice': 2, 'Bob': 4, 'Carol': 1, 'Dave': 3, 'Eve': 5},
 {'Alice': 1, 'Bob': 5, 'Carol': 2, 'Dave': 4, 'Eve': 3},
 {'Alice': 1, 'Bob': 4, 'Carol': 5, 'Dave': 2, 'Eve': 3},
 {'Alice': 4, 'Bob': 3, 'Carol': 5, 'Dave': 2, 'Eve': 1},
 {'Alice': 5, 'Bob': 2, 'Carol': 3, 'Dave': 1, 'Eve': 4},
 {'Alice': 5, 'Bob': 4, 'Carol': 1, 'Dave': 3, 'Eve': 2},
 {'Alice': 1, 'Bob': 2, 'Carol': 3, 'Dave': 5, 'Eve': 4},
 {'Alice': 4, 'Bob': 1, 'Carol': 3, 'Dave': 2, 'Eve': 5},
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 3, 'Eve': 2},
 {'Alice': 2, 'Bob': 4, 'Carol': 3, 'Dave': 1, 'Eve': 5},
 {'Alice': 3, 'Bob': 5, 'Carol': 1, 'Dave': 2, 'Eve': 4},
 {'Alice': 4, 'Bob': 5, 'Carol': 1, 'Dave': 3, 'Eve': 2},
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 1, 'Eve': 3},
 {'Alice': 2, 'Bob': 3, 'Carol': 5, 'Dave': 1, 'Eve': 4},
 {'Alice': 3, 'Bob': 2, 'Carol': 4, 'Dave': 1, 'Eve': 5},
 {'Alice': 1, 'Bob': 2, 'Carol': 5, 'Dave': 3, 'Eve': 4},
 {'Alice': 1, 'Bob': 2, 'Carol': 3, 'Dave': 5, 'Eve': 4},
 {'Alice': 4, 'Bob': 5, 'Carol': 2, 'Dave': 1, 'Eve': 3},
 {'Alice': 5, 'Bob': 2, 'Carol': 3, 'Dave': 4, 'Eve': 1},
 {'Alice': 1, 'Bob': 2, 'Carol': 4, 'Dave': 3, 'Eve': 5},
 {'Alice': 1, 'Bob': 5, 'Carol': 3, 'Dave': 4, 'Eve': 2},
 {'Alice': 4, 'Bob': 3, 'Carol': 1, 'Dave': 5, 'Eve': 2},
 {'Alice': 3, 'Bob': 4, 'Carol': 5, 'Dave': 2, 'Eve': 1},
 {'Alice': 3, 'Bob': 4, 'Carol': 1, 'Dave': 2, 'Eve': 5},
 {'Alice': 2, 'Bob': 4, 'Carol': 5, 'Dave': 1, 'Eve': 3},
 {'Alice': 5, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 1},
 {'Alice': 3, 'Bob': 5, 'Carol': 2, 'Dave': 1, 'Eve': 4},
 {'Alice': 1, 'Bob': 5, 'Carol': 4, 'Dave': 3, 'Eve': 2},
 {'Alice': 5, 'Bob': 2, 'Carol': 4, 'Dave': 3, 'Eve': 1},
 {'Alice': 4, 'Bob': 1, 'Carol': 5, 'Dave': 3, 'Eve': 2},
 {'Alice': 5, 'Bob': 3, 'Carol': 1, 'Dave': 4, 'Eve': 2},
 {'Alice': 3, 'Bob': 2, 'Carol': 5, 'Dave': 1, 'Eve': 4},
 {'Alice': 1, 'Bob': 5, 'Carol': 4, 'Dave': 3, 'Eve': 2},
 {'Alice': 5, 'Bob': 1, 'Carol': 4, 'Dave': 2, 'Eve': 3},
 {'Alice': 1, 'Bob': 4, 'Carol': 2, 'Dave': 3, 'Eve': 5},
 {'Alice': 5, 'Bob': 1, 'Carol': 2, 'Dave': 4, 'Eve': 3},
 {'Alice': 3, 'Bob': 5, 'Carol': 1, 'Dave': 2, 'Eve': 4},
 {'Alice': 1, 'Bob': 3, 'Carol': 4, 'Dave': 5, 'Eve': 2},
 {'Alice': 3, 'Bob': 1, 'Carol': 5, 'Dave': 2, 'Eve': 4},
 {'Alice': 5, 'Bob': 3, 'Carol': 4, 'Dave': 2, 'Eve': 1},
 {'Alice': 4, 'Bob': 2, 'Carol': 1, 'Dave': 3, 'Eve': 5},
 {'Alice': 3, 'Bob': 4, 'Carol': 1, 'Dave': 5, 'Eve': 2},
 {'Alice': 2, 'Bob': 1, 'Carol': 5, 'Dave': 3, 'Eve': 4},
 {'Alice': 2, 'Bob': 3, 'Carol': 4, 'Dave': 5, 'Eve': 1},
 {'Alice': 2, 'Bob': 3, 'Carol': 1, 'Dave': 4, 'Eve': 5}]

def stv(ballots, seats):
    # Convert ballots to (ordered_preferences, weight)
    weighted_ballots = []
    for ballot in ballots:
        prefs = tuple(
            c for c, r in sorted(ballot.items(), key=lambda x: x[1])
        )
        weighted_ballots.append([prefs, 1.0])

    # Collect all candidates
    candidates = set()
    for prefs, _ in weighted_ballots:
        for c in prefs:
            candidates.add(c)

    elected = []
    eliminated = set()

    total_votes = len(weighted_ballots)
    quota = total_votes // (seats + 1) + 1

    round_num = 1

    def tally():
        counts = {}
        for prefs, weight in weighted_ballots:
            for c in prefs:
                if c not in elected and c not in eliminated:
                    counts[c] = counts.get(c, 0.0) + weight
                    break
        return counts

    print(f"Total votes: {total_votes}")
    print(f"Seats: {seats}")
    print(f"Droop quota: {quota}")
    print("-" * 40)

    while len(elected) < seats:
        print(f"\nROUND {round_num}")
        counts = tally()

        if not counts:
            print("\nNo votes remaining to transfer.")
            remaining = candidates - set(elected) - eliminated
            for c in sorted(remaining):
                print(f"ELECTED: {c}")
                elected.append(c)
            break

        # Print tallies
        for c in sorted(counts):
            print(f"{c:>6}: {counts[c]:.3f}")

        # Check for winner
        winner = None
        for c in counts:
            if counts[c] >= quota:
                winner = c
                break

        if winner is not None:
            print(f"\nELECTED: {winner}")
            elected.append(winner)

            total = counts[winner]
            surplus = total - quota
            print(f"Surplus: {surplus:.3f}")

            transfer_fraction = surplus / total if surplus > 0 else 0.0
            print(f"Transfer fraction: {transfer_fraction:.6f}")

            new_ballots = []
            for prefs, weight in weighted_ballots:
                if prefs and prefs[0] == winner:
                    transferred = weight * transfer_fraction
                    remaining = weight - transferred

                    if remaining > 0:
                        new_ballots.append([prefs, remaining])

                    if transferred > 0:
                        new_prefs = tuple(p for p in prefs if p != winner)
                        if new_prefs:
                            new_ballots.append([new_prefs, transferred])
                else:
                    new_ballots.append([prefs, weight])

            weighted_ballots = new_ballots
            round_num += 1
            continue

        # Eliminate lowest candidate
        lowest = None
        lowest_votes = None
        for c, v in counts.items():
            if lowest is None or v < lowest_votes:
                lowest = c
                lowest_votes = v

        print(f"\nELIMINATED: {lowest} ({lowest_votes:.3f} votes)")
        eliminated.add(lowest)

        new_ballots = []
        for prefs, weight in weighted_ballots:
            new_prefs = tuple(p for p in prefs if p != lowest)
            if new_prefs:
                new_ballots.append([new_prefs, weight])

        weighted_ballots = new_ballots

        # Early termination
        remaining = candidates - set(elected) - eliminated
        if len(remaining) + len(elected) <= seats:
            print("\nRemaining candidates equal remaining seats.")
            for c in sorted(remaining):
                print(f"ELECTED: {c}")
                elected.append(c)
            break

        round_num += 1

    print("\nFINAL RESULT")
    print("=" * 40)
    for i, c in enumerate(elected, 1):
        print(f"Seat {i}: {c}")

    return elected


print(stv(ballots, seat_number))





'''test_seats'''
for seats in range(1, total_candidates+2):
    result = stv(ballots, seats)
    print(f'Seats: {seats}, Elected: {result}') 

'''the below code was taken with minor alterations from the 
Love Sandwiches project code'''

from itertools import count
from operator import invert
from bidict import bidict

import gspread
from google.oauth2.service_account import Credentials

'''end of Love Sandwiches code'''

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

ballots_test = [
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



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Election Data')


#Phase 1 (Data Input) Starts Here

candidate_worksheet = SHEET.worksheet('Candidates')
ballots = SHEET.worksheet('Ballots')
# ballots_raw = ballots.get_all_values()

'''We assume candidates have been given an ID by the ballot-setters an
 continue to use that one'''

'''For test ballot sets, we could create a list of candidates and give them an ID by alphabetising them

We don't want the candidate data to be changed, e.g. a user sneaking themselves onto the list!
'''

'''TODO check candidate data for invalid data, e.g. non-natural number for ID, duplicate IDs, duplicate. Skipped numbers ARE valid; candidates may have been disqualified after getting on the list.'''

CANDIDATE_DATA =(candidate_worksheet.get_all_values())

CANDIDATE_NAMES_AND_IDS = bidict(CANDIDATE_DATA)

CANDIDATE_NUMBER = len(CANDIDATE_NAMES_AND_IDS)


'''Ballot area'''

BALLOTS_RAW = ballots.get_all_values()

#print(BALLOTS_RAW)


current_ballot = []

ballots_cleaned = [current_ballot]
#print(BALLOTS_RAW)

for line in BALLOTS_RAW:
    
    if line == ['', ''] or line == []:
        ballots_cleaned.append(current_ballot)

    if line == ['', '']:    
        current_ballot = []

    else:
        current_ballot.append(line)
        
#print(ballots_cleaned)

ballots_dicts = []

for ballot in ballots_cleaned:
    if not ballot:
        continue

    ballot_dict = {}
    for row in ballot:
        if len(row) >= 2 and row[0] and row[1]:
            ballot_dict[row[0]] = int(row[1])

    if ballot_dict:
        ballots_dicts.append(ballot_dict)


print(stv(ballots_dicts, seat_number))

from random import shuffle

def cli_generate_election():
    print("STV Election Setup")
    print("-" * 30)

    # Candidate names
    raw_names = input("Enter candidate names (comma-separated): ").strip()
    candidates = [name.strip() for name in raw_names.split(",") if name.strip()]

    if len(candidates) < 2:
        raise ValueError("You must enter at least two candidates.")

    # Seats
    seats = int(input("Enter number of seats: ").strip())
    if seats < 1 or seats >= len(candidates):
        raise ValueError("Seats must be at least 1 and fewer than candidates.")

    # Ballots
    ballot_count = int(input("Enter number of ballots to generate: ").strip())
    if ballot_count < 1:
        raise ValueError("Must generate at least one ballot.")

    print("\nGenerating ballots...\n")

    ballots = []
    for _ in range(ballot_count):
        ranks = list(range(1, len(candidates) + 1))
        shuffle(ranks)
        ballot = {candidates[i]: ranks[i] for i in range(len(candidates))}
        ballots.append(ballot)

    return candidates, seats, ballots

print(cli_generate_election())

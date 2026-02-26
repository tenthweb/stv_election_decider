from random import shuffle


def stv(ballots, seats):
    # Convert ballots to (ordered_preferences, weight)
    weighted_ballots = []
    for ballot in ballots:
        prefs = tuple(
            c for c, r in sorted(ballot.items(), key=lambda x: x[1])
        )
        weighted_ballots.append([prefs, 1.0])

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
            remaining = candidates - set(elected) - eliminated
            for c in sorted(remaining):
                print(f"ELECTED: {c}")
                elected.append(c)
            break

        for c in sorted(counts):
            print(f"{c:>6}: {counts[c]:.3f}")

        winner = None
        for c in counts:
            if counts[c] >= quota:
                winner = c
                break

        if winner:
            print(f"\nELECTED: {winner}")
            elected.append(winner)
            total = counts[winner]
            surplus = total - quota
            transfer_fraction = surplus / total if surplus > 0 else 0.0

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

        lowest = min(counts, key=counts.get)
        lowest_votes = counts[lowest]
        print(f"\nELIMINATED: {lowest} ({lowest_votes:.3f} votes)")
        eliminated.add(lowest)

        new_ballots = []
        for prefs, weight in weighted_ballots:
            new_prefs = tuple(p for p in prefs if p != lowest)
            if new_prefs:
                new_ballots.append([new_prefs, weight])

        weighted_ballots = new_ballots

        remaining = candidates - set(elected) - eliminated
        if len(remaining) + len(elected) <= seats:
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


def run_cli():

    # welcome message
    print("Single Transferable Vote (STV) Election Simulator")
    print("=" * 50)
    print("This simulator allows you to run an STV election with random "
          "ballots.")
    print("Please provide the candidate names, number of seats, and number "
          "of ballots.")
    print("=" * 50)

    # Get candidates from user




    # Get candidates from user
    while True:
        candidates_input = input("Enter candidate names, separated by commas: ")
        # Strip whitespace and remove any empty strings
        candidates = [c.strip() for c in candidates_input.split(",") if c.strip()]

        if not candidates:
            print("Error: You must enter at least one valid candidate.")
            continue

        break

    # Number of seats
    while True:
        seats_input = input("Enter number of seats to fill: ").strip()

        # Validate seats input, make sure to deal with blank input and non-number inputs

        if seats_input == "":
            print("Error: Seats cannot be blank.")
            continue

        if not seats_input.isdigit():
            print("Error: Please enter a valid number.")
            continue

        seats = int(seats_input)

        if seats <= 0:
            print("Error: Number of seats must be greater than zero, or why would there be an election?")
            continue

        break


    # Number of ballots

    while True:
        num_ballots = input("Enter number of ballots to generate: ").strip()
        
        # Validate seats input, make sure to deal with blank input and non-number inputs

        if num_ballots == "":
            print("Number of ballots cannot be blank.")
            continue

        if not num_ballots.isdigit():
            print("Please enter a valid whole number.")
            continue

        # If num_ballots looks sort of like a number, try to convert to integer
        num_ballots = int(num_ballots)

        if num_ballots <= 0:
            print("Number of ballots must be greater than 0.")
            continue

        break

    # Generate random ballots
    ballots = []
    for _ in range(num_ballots):
        prefs = list(range(1, len(candidates) + 1))
        shuffle(prefs)
        ballot = {candidates[i]: prefs[i] for i in range(len(candidates))}
        ballots.append(ballot)

    # Run STV
    stv(ballots, seats)


if __name__ == "__main__":
    run_cli()

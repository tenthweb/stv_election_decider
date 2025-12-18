# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
'''the below code was taken with minor alterations from the 
Love Sandwiches project code'''

from itertools import count
from operator import invert
from bidict import bidict

import gspread
from google.oauth2.service_account import Credentials


'''classes for ballots and candidates will go here'''

class Election:
    def __init__(self, candidates, ballots, seats=1):
        self.candidates = candidates
        self.ballots = ballots
        self.seats = seats

        '''We need a list of Round objects'''

        self.rounds = []

        self.current_round = self.initialise_first_round()
        self.current_round_number = self.current_round.round_number

        self.current_counts = {candidate: 0 for candidate in candidates}

    def get_candidates(self):
        return self.candidates
    
    def get_candidate_count(self):
        return len(self.candidates)
    
    def get_ballots(self):
        return self.ballots
    
    def get_ballot_count(self):
        return len(self.ballots)
    
    def get_seats_count(self):
        return self.seats
    
    '''Using the 1/(seats+1) formula for Droop quota without using
    other variations, such as adding 1 or using floor or ceiling functions.
    We're using "strictly greater than the quota" as the criterion for
    winning, and allowing fractions of votes for surplus distribution,
    so this is acceptable.'''

    def get_droop_quota(self):
        ballot_count = len(self.ballots)
        candidate_count = len(self.candidates)
        droop_quota = (ballot_count / (self.seats + 1))
        return droop_quota
    
    def initialise_vote_count(self):
        self.current_counts = {candidate: 0 for candidate in self.candidates.inverse}
        return self.current_counts
    
    def initialise_first_round(self):
        first_round = Round(1, {candidate: 0 for candidate in self.candidates.inverse})
        self.rounds.append(first_round)
        return first_round

    def initialise__new_round(self, previous_round_number, previous_vote_count):
        round_number = previous_round_number + 1
        new_round = Round(round_number, previous_vote_count)
        self.rounds.append(new_round)
        return new_round


class Round:
    def __init__(self, round_number, previous_vote_count):
        self.round_number = round_number
        self.previous_vote_count = previous_vote_count
        self.winners = []
        self.current_vote_count = previous_vote_count

    def count_votes(self, current_vote_count, ballots):
        
        print("Vote count initialized:", self.current_vote_count)
        # print(self.previous_vote_count)
        if self.round_number == 1:
            for ballot in ballots:
                for line in ballot:
                    if line[1] == '1':
                        candidate_name = line[0]
                        self.current_vote_count[candidate_name] += 1
            vote_count = self.current_vote_count
        else:
            vote_count = self.previous_vote_count

            
        return vote_count

    def check_for_winners(self, droop_quota, current_vote_count):
        for candidate in current_vote_count:
            if current_vote_count[candidate] >= droop_quota:
                self.winners.append(candidate)
        return self.winners
    
    def redistribute_winner_votes(self, candidate, current_vote_count, ballots, droop_quota):
            surplus_votes = current_vote_count[candidate] - droop_quota
            print(f"Redistributing surplus votes for {candidate}, surplus votes: {surplus_votes}")
            next_preference_votes = {next_preference_candidate: 0  for next_preference_candidate in current_vote_count if next_preference_candidate != candidate}
            for ballot in ballots:
                for line in ballot:
                    if line[1] == '1' and line[0] == candidate:
                        # Find the next preference on this ballot
                        for next_line in ballot:
                            if next_line[1] == '2':
                                next_candidate = next_line[0]
                                next_preference_votes[next_candidate] += 1

            print(f"Next preference votes: {next_preference_votes}")
            next_preference_votes_total = sum(next_preference_votes.values())
            print(f"Total next preference votes: {next_preference_votes_total}")

        




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

'''The ballots_cleaned variable is a list of ballots. Each ballot is a list of 
lists, representing candidate name and preference number.'''
'''TODO make ballots into objects'''



current_election = Election(CANDIDATE_NAMES_AND_IDS, ballots_cleaned, 4)






'''Iterate through ballots, getting each ballot's first preference and adding one to that candidate's live vote count'''

def get_individual_ballot_count():
    ballot_count = len(ballots_cleaned) 
    return ballot_count

#print(f"Total number of ballots: {get_individual_ballot_count()}")


def check_for_winner(droop_quota, live_vote_count):
    winners = []
    for candidate in live_vote_count:
        if live_vote_count[candidate] >= droop_quota:
            winners.append(candidate)
    return winners

    

def get_surplus_votes(droop_quota, live_vote_count):
    pass

def remove_candidate_from_live_count(winner, live_vote_count):
    pass

def resdistribute_surplus_votes(winner, live_vote_count, ballots_cleaned, droop_quota):
    pass

def add_candidate_to_winners_list(winner, winners):
    pass

def find_lowest_candidates(live_vote_count):
    pass

def redistribute_lowest_candidate_votes(live_vote_count, ballots_cleaned):
    pass

def remove_lowest_candidates_from_live_count(live_vote_count):
    pass  


winners = []  
def current_round():
     return Round(1, check_for_winner(droop_quota, live_vote_count))


 
'''
if check_for_winner(droop_quota, live_vote_count):
    
    for winner in winners:
        get_surplus_votes(droop_quota, live_vote_count) 
        remove_candidate_from_live_count(winner, live_vote_count)
        resdistribute_surplus_votes(winner, live_vote_count, ballots_cleaned, droop_quota)
        
        add_candidate_to_winners_list(winner, winners)
    print("Winners:", check_for_winner(droop_quota, live_vote_count))
else:
    print("No winners yet, removing candidates with lowest votes and redistributing surplus votes.")
    find_lowest_candidates(live_vote_count)
    redistribute_lowest_candidate_votes(live_vote_count, ballots_cleaned)
    remove_lowest_candidates_from_live_count(live_vote_count)





    

print("Winners:", check_for_winner(get_droop_quota(get_individual_ballot_count()), live_vote_count))
'''
def get_surplus_votes(droop_quota, live_vote_count):
    surplus_votes = {}
    for candidate in live_vote_count:
        if live_vote_count[candidate] > droop_quota:
            surplus_votes[candidate] = live_vote_count[candidate] - droop_quota
    return surplus_votes

def get_lowest_candidates(live_vote_count):
    lowest_vote_count = min(live_vote_count.values())
    lowest_candidates = []
    for candidate in live_vote_count:
        if live_vote_count[candidate] == lowest_vote_count:
            lowest_candidates.append(candidate)
    return lowest_candidates



'''Test the logic just for the first round of counting'''

#print(current_election.rounds[0].count_votes(CANDIDATE_NAMES_AND_IDS,ballots_cleaned))
print(f"With {current_election.get_seats_count()} seats and {current_election.get_ballot_count()} ballots, the droop quota is {current_election.get_droop_quota()}.")

test_current_election_round_count = current_election.current_round.count_votes(CANDIDATE_NAMES_AND_IDS,ballots_cleaned)
print(f"round 1 vote count: {test_current_election_round_count}")
print(f"round 1 winners: {current_election.current_round.check_for_winners(current_election.get_droop_quota(), test_current_election_round_count)}")


current_election.current_round.redistribute_winner_votes(current_election.current_round.winners[0],
        test_current_election_round_count,
        ballots_cleaned,
        current_election.get_droop_quota())
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
'''the below code was taken with minor alterations from the 
Love Sandwiches project code'''

from bidict import bidict

import gspread
from google.oauth2.service_account import Credentials

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
print(BALLOTS_RAW)

for line in BALLOTS_RAW:
    
    if line == ['', ''] or line == []:
        ballots_cleaned.append(current_ballot)

    if line == ['', '']:    
        current_ballot = []

    else:
        current_ballot.append(line)
        
print(ballots_cleaned)

'''The ballots_cleaned variable is a list of ballots. Each ballot is a list of 
lists, representing candidate name and preference number.'''
'''TODO make ballots into objects'''


live_vote_count = {CANDIDATE_NAMES_AND_IDS[candidate]:0 for candidate in CANDIDATE_NAMES_AND_IDS}

print("Current live_vote_count:")
for value, key in live_vote_count.items():
    print(f"{value}: {key}")

#Phase 2 (Counting) Starts Here

'''Iterate through ballots, getting each ballot's first preference and adding one to that candidate's live vote count'''

def get_individual_ballot_count():
    ballot_count = len(ballots_cleaned) 
    return ballot_count

print(f"Total number of ballots: {get_individual_ballot_count()}")

def get_droop_quota(ballot_count):
    droop_quota = (ballot_count // (CANDIDATE_NUMBER +  1)) + 1
    return droop_quota

print("Droop quota:", get_droop_quota(get_individual_ballot_count()))

for ballot in ballots_cleaned:
    for entry in ballot:
        if entry[1] == '1':
            candidate_name = entry[0]
            live_vote_count[candidate_name] += 1

print("Updated live_vote_count:")
for value, key in live_vote_count.items():
    print(f"{value}: {key}")




# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
'''the below code was taken with minor alterations from the 
Love Sandwiches project code'''

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

candidate_worksheet = SHEET.worksheet('Candidates')
ballots = SHEET.worksheet('Ballots')
# ballots_raw = ballots.get_all_values()

'''We assume candidates have been given an ID by the ballot-setters and continue to use that one'''

'''For test ballot sets, we could create a list of candidates and give them an ID by alphabetising them

We don't want the candidate data to be changed, e.g. a user sneaking themselves onto the list!
'''

CANDIDATE_DATA =(candidate_worksheet.get_all_values())

CANDIDATE_NAMES = [CANDIDATE_DATA[i][0] for i in range(len(CANDIDATE_DATA))]

live_vote_table = {candidate for candidate in CANDIDATE_NAMES}
print(CANDIDATE_NAMES)
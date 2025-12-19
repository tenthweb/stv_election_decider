# Election Simulator

This program allows users to quickly set up and run a simulated election using the **Single Transferable Vote (STV)** system.

## Intended Use

The tool is designed for experimentation, learning, and testing election logic, rather than for real-world vote collection.

It allows users to input candidate names, number of seats, and it generates random ballots to simulate an STV election, and then displays the results step-by-step.

It runs inside the Code Institute mock terminal on Heroku.

This program is intended to be:

- Easy to use for non-technical users

- Suitable for simulations demonstrations, coursework

[Here is the live version link](https://stv_election_simulator.herokuapp.com/)

## Features

Using simple prompts, the program lets you define:

- A list of candidate names (entered as comma-separated values)

- The number of seats to be filled

- The number of ballots to generate

From these inputs, the program generates a complete election dataset, including ranked ballots, is then passed directly into the STV counting engine. The simulator supports fractional vote transfers, a Droop quota, and round-by-round reporting, making the full counting process transparent and easy to follow.

### Existing feature

- User input for candidates and seats

- Random ballot generation

- Step-by-step STV counting process

### Future features:
- Save and load raw election data from spreadsheet using the Google Drive and Google Sheets APIs, or from a SQL database or other file.
- Rerun elections with slightly altered data multiple times for e.g. situations with last-minute candidate withdrawals.
- Visualize the counting process with graphs.
- Backend: Use classes to encapsulate election logic and data structures. This would improve code organization and maintainability, and this process is very suitable for OOP design patterns with e.g. an Election class, Candidate class, Ballot class, etc.

## Data model:

- ballot: Represents a single voter's ranked preferences.

- candidate: Represents a candidate in the election.

- votes: Represents the total number of votes a candidate has received.

- quota: Represents the minimum number of votes required to win a seat.

- elected: Represents the list of candidates who have been elected.

- eliminated: Represents the list of candidates who have been eliminated.

- weighted_ballots: Represents a list of ballots with their weights.

### How these work together:

 Ballots are processed to tally votes for candidates.

- Candidates are elected or eliminated based on the STV counting process:
  - If a candidate reaches the quota, they are elected and their surplus votes are redistributed.

  - Redistribution is done counting the ballots that contributed to their election, weighting them according to their remaining preferences, and then transferring a fraction of the ballot to the next preferred candidate in proportion to the weight.

- If no candidate reaches the quota, the candidate with the fewest votes is eliminated, and their votes are redistributed to the next preferred candidates on those ballots.

### Functions:

- We have two main functions, one to handle the CLI and one to run the STV process:

  - `run_cli()` : Handles the user input and initiates the election process.

  - `stv(ballots, seats)`: Main function to run the STV election process.

## Testing:
- I have manually tested the code by running multiple elections, varying the following to ensure the STV process works correctly and produces expected results.

  - candidate names
  - seat numbers
  - ballot counts
  - Empty and invalid inputs

- I've passed the code through a PEP8 linter to ensure it adheres to Python coding standards.

### Bugs:

- Solved bug where Droop quota calculation was incorrect (number of candidates was used in the calculation instead of number of seats).

- Remaining bugs to fix: Null inputs causing crashes.


## Deployment instructions:

### To deploy this code to Heroku, follow these steps:
1. Ensure you have a Heroku account.
2. On the heroku dashboard, create a new app.
3. Give the app a name and choose a region.
4. Set python and nodejs as buildpacks in the "Settings" tab.
5. In the "Deploy" tab, connect your GitHub repository containing this code.
6. Enable automatic deploys or manually deploy the main branch.

## Credits
- Developed by Matthew Byrne
- Business logic and STV algorithm inspired by various online resources on Single Transferable Vote systems, including the [Wikipedia page on STV](https://en.wikipedia.org/wiki/Single_transferable_vote) and the [Irish electoral commission](https://www.electoralcommission.ie/irelands-voting-system/).
- Hosted on Heroku using Code Institute's mock terminal environment, using their provided template and deployment instructions.
- Some unused code was adapted from Code Institute's Love Sandwiches project.
- The code was produced in VScode. Autocompletion and linting were provided by the Pylance extension, as well as boilerplate code, e.g. autocompleting syntax for variable names, loops, and functions, and autocorrecting indentation.
- ChatGPT was used to help brainstorm features and future improvements, as well as to help debug some issues with the initial implementation of the STV algorithm.
- The random.py library was used to shuffle voter preferences when generating ballots.


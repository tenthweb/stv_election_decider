# Testing for STV Election Decider

## Main Line Functionality: Running the Elections

Three "typical" races were run, with 2-10 candidates, 1-5 seats, and 20-1000 ballots.

Expected behaviour: The code should choose the appropriate number of winners using our STV method, distributing votes from candidates in first and last position as approrpriate.

### Case 1: 2 Candidates, 1 Seat, 20 votes

* Observed Behaviour: Bob gets 11 votes, and so has reached the quota. He wins the election as expected.


![Simple 1-seat race with two candidates](<screenshots/Screenshot 2026-02-27 110133.png>)

### Case 2: 4 Candidates, 2 seats, 100 votes 

* Observed Behaviour:
 * First Round: nobody meets the quota, so Bob, the candidate with the least votes is elimated
 * Second Round: After redistributing, Dave now meets the quota, so he is elected
 * Third Round: After redistributing, nobody meets the quota, so Carol is eliminated with the least votes.

Two candidates are successfully elected as expected.

Note: Fractional votes start to appear after a candidate is elected, but not after one is eliminated. This is a clue that the system is working properly by sharing all an eliminated candidate's votes, but only a weighted amount of an elected one's.

![2-seat, 4 candidate, 100 vote race 1](<screenshots/Screenshot 2026-02-27 110423.png>)

![2-seat, 4 candidate, 100 vote race 2](<screenshots/Screenshot 2026-02-27 110643.png>)

### Case 3: 10 candidate, 6 seats, 1000 votes

Observed behaviour: The code handles the larger number of candidates, seats, and ballots as expected. 

![10 candidate, 6 seats, 1000 votes](<screenshots/Screenshot 2026-02-27 111622.png>)
![10 candidate, 6 seats, 1000 votes](<screenshots/Screenshot 2026-02-27 111626.png>)
![10 candidate, 6 seats, 1000 votes](<screenshots/Screenshot 2026-02-27 111614.png>)
![10 candidate, 6 seats, 1000 votes](<screenshots/Screenshot 2026-02-27 111631.png>)
![10 candidate, 6 seats, 1000 votes](<screenshots/Screenshot 2026-02-27 111635.png>)
![10 candidate, 6 seats, 1000 votes](<screenshots/Screenshot 2026-02-27 111640.png>)

## Command Line Interface Validation Testing

### Input for candidate list

#### Empty list

The user enters an empty string.

* Expected Behaviour: An error is thrown and the user is directed to enter at least one candidate.
* Observed Behaviour: The expected error is thrown, see screenshot:

![screenshot of error](/screenshots/Screenshot%202026-02-26%20233150.png)

#### Valid Whitespace

The user types a name with whitespace, in this case "Alice T." and "Henry R."

* Expected Behaviour: The code treats the whitespace normally, and saves the text as e.g. "Alice T." rather than "Alice" and "T."
* Observed Behaviour: The code treats the whitespace normally as in the screenshot below.

![screenshot of names with space](<screenshots/Screenshot 2026-02-26 233702.png>)

#### Extra Whitespace

The user includes extra whitespace between the comma-separated values, including both empty strings betweens the commas, and extra spaces before and after commas.

* Expected Behaviour: The code automatically strips the whitespace
* Observed Behaviour: The code strips the whitespace in all cases

![screenshot of behaviour](/screenshots/Screenshot%202026-02-26%20233150.png)

### Input for number of seats

#### Invalid input

##### Initial Run

The user puts in no seat number.

* Expected behaviour: The code should handle the error and ask the user to try again
* Observed behaviour: The code crashes as in the below:

![screenshot of failure with zero number of seats](<screenshots/Screenshot 2026-02-26 191430.png>)

##### Second Run

The user puts in no seat number, and other possible bad data was included: negative numbers, fractions.

* Expected behaviour: The code should handle the error and ask the user to try again.
* Observed behaviour: The code handles the error correctly as in the below:

![screenshot of correct handling of bad inputs for seats](<screenshots/Screenshot 2026-02-26 192628.png>)

#### Edge cases

The user puts in more seats than there are candidates. In future versions, logic might be put in to flag this to the user, but at present this should just run as normal and give seats to all the candidates.

* Expected behaviour: The code should give a seat to all candidates
* Observed behaviour: The code handles the error correctly as in the below:

![screenshot of 2 candidates in a 3-seat race](<screenshots/Screenshot 2026-02-27 105618.png>)

### Input for number of votes








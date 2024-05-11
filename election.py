import csv


class Election:

    def __init__(self) -> None:
        """
        Initializes the Election class
        """
        self.__voters = {}
        self.__votes = []
        self.__voted = []
        with open('Voting_Results.csv', 'w', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow(['Voter', 'Vote'])
        with open('Voters.csv', 'r') as csvfile:
            next(csvfile)
            content = csv.reader(csvfile, delimiter=',')
            for row in content:
                self.__voters[row[0].lower().strip()] = int(row[1].strip())

    def verify_voter(self, username, pin) -> str:
        """
        Method verifies if a username and pin is valid, if a username already voted, or if a username/pin is invalid
        :param username: Voter's username
        :param pin: Voter's pin
        :return: "valid" if the username/pin is valid, "already voted" if voter has voted, or "not valid" if the
        username/pin is invalid
        """
        if username in self.__voters and self.__voters[username] == pin:
            return 'valid'
        elif username in self.__voted:
            return 'already voted'
        else:
            return 'not valid'

    def add_vote(self, username, vote) -> None:
        """
        Method adds a vote for the selected box and records vote into a csv file
        :param username: voter's username
        :param vote: voter's vote
        """
        self.__votes.append(vote)
        self.__voted.append(username)
        with open('Voting_Results.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)
            content.writerow([username, vote])
        self.__voters.pop(username, None)

    def voting_results(self) -> str:
        """
        Method tallies the votes and returns a string declaring the winner(s)
        :return: string declaring the winner(s)
        """
        winner = []
        winning_score = 0
        tallied_votes = {x: self.__votes.count(x) for x in self.__votes}
        for key in tallied_votes:
            if tallied_votes[key] >= winning_score:
                winning_score = tallied_votes[key]
                winner.append(key)

        if len(winner) == 0:
            return 'No votes were received'
        if len(winner) == 1:
            return f'Your winner is {winner[0]} with {winning_score} votes'
        elif len(winner) == 2:
            return f'Your winners are {winner[0]} and {winner[1]}\n with {winning_score} votes each'
        else:
            winner_string = 'Your winners are\n'
            for i in range(len(winner)):
                if i <= len(winner) - 3:
                    winner_string += winner[i] + ', '
                elif i == len(winner) - 2:
                    winner_string += winner[i] + ', and '
                else:
                    winner_string += winner[i] + '\n'
            winner_string += 'with ' + str(winning_score) + ' votes each'
            return winner_string

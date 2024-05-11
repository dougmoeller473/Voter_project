from PyQt6.QtWidgets import *
from gui import *
from election import *


class Logic(QMainWindow, Ui_MainWindow):

    def __init__(self):
        """
        Initializes the Logic class
        """
        super().__init__()
        self.setupUi(self)
        self.election = Election()
        self.Clear_button.clicked.connect(lambda: self.clear())
        self.Submit_button.clicked.connect(lambda: self.submit())
        self.Tally_button.clicked.connect(lambda: self.tally())

    def submit(self):
        """
        Method verifies votes and adds votes to the total when the submit button is clicked
        """
        self.label_feedback.setText('')
        try:
            username = self.User_name.text().strip().lower()
            pin = int(self.PIN.text().strip())

            if self.election.verify_voter(username, pin) == 'valid':
                if self.radioButton_zelda.isChecked():
                    self.election.add_vote(username, 'Zelda')
                elif self.radioButton_mario_kart.isChecked():
                    self.election.add_vote(username, 'Mario Kart')
                elif self.radioButton_animal_crossing.isChecked():
                    self.election.add_vote(username, 'Animal-Crossing')
                elif self.radioButton_smash_bros.isChecked():
                    self.election.add_vote(username, 'Smash Bros.')
                else:
                    self.election.add_vote(username, self.write_in_field.text().strip().lower())
            elif self.election.verify_voter(username, pin) == 'already voted':
                self.label_feedback.setText('You have already voted\nPlease allow someone else to vote')
            else:
                self.label_feedback.setText('INVALID USERNAME AND/OR PIN')
        except ValueError:
            self.label_feedback.setText('Your PIN is a 4 digit number')

        self.User_name.clear()
        self.PIN.clear()
        self.write_in_field.clear()
        self.radioButton_zelda.setChecked(True)

    def clear(self):
        """
        Method clears the fields when the clear button is clicked
        """
        self.User_name.clear()
        self.PIN.clear()
        self.write_in_field.clear()
        self.radioButton_zelda.setChecked(True)
        self.label_feedback.setText('')

    def tally(self):
        """
        Method tabulates the votes when the tally button is pushed
        """
        self.label_feedback.setText(self.election.voting_results())

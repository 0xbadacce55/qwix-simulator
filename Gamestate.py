from Dice import Dice
import Constants

class Gamestate:
    def __init__(self, players):
        self.dice = []
        self.dice.append(Dice(Constants.WHITE)).append(Dice(Constants.WHITE)).append(Dice(Constants.RED)).append(Dice(Constants.BLUE)).append(Dice(Constants.GREEN)).append(Dice(Constants.YELLOW))
        self.players = players
        self.playerTurnIndex = 0
        self.gameOver = False

    def executeTurn(self) -> bool:
        self.determineGameOver
        if(self.gameOver):
            return False
        for dice in self.dice:
            dice.roll
        # for every player, execute their turn
        return True

    def determineGameOver(self):
        self.gameOver = True
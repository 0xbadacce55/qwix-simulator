from Dice import Dice
import Constants

class Gamestate:
    def __init__(self, players):
        self.dice = [Dice(Constants.RED), Dice(Constants.YELLOW), Dice(Constants.GREEN), Dice(Constants.BLUE), Dice(Constants.WHITE1), Dice(Constants.WHITE2)]
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
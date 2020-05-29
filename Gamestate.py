from Dice import Dice
import Constants

class Gamestate:
    def __init__(self, players):
        self.dice = [Dice(Constants.RED), Dice(Constants.YELLOW), Dice(Constants.GREEN), Dice(Constants.BLUE), Dice(Constants.WHITE1), Dice(Constants.WHITE2)]
        self.players = players
        self.player_turn_index = 0
        self.game_over = False

    def execute_turn(self) -> bool:
        self.determine_game_over
        if(self.game_over):
            return False
        for dice in self.dice:
            dice.roll
        # for every player, execute their turn
        return True

    def determine_game_over(self):
        self.game_over = True
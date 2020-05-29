import Constants

class Board:
    def __init__(self):
        self.rows = []
        self.furthest = []
        self.rows[Constants.RED] = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11:False, 12: False}
        self.furthest[Constants.RED] = 1
        self.rows[Constants.YELLOW] = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11:False, 12: False}
        self.furthest[Constants.YELLOW] = 1
        self.rows[Constants.BLUE] = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11:False, 12: False}
        self.furthest[Constants.BLUE] = 1
        self.rows[Constants.GREEN] = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11:False, 12: False}
        self.furthest[Constants.GREEN] = 1
        self.fehlwurfe = 0

    def is_legal_move(self, color, number) -> bool:
        if number < 12:
            if self.furthest[color] < number:
                return True
        else:
            if self.count_strikes(color) > 4:
                return True
        return False

    def move(self, color, number) -> bool:
        if self.is_legal_move(color, number):
            self.rows[color][number] = True
            self.furthest[color] = number
            return True
        else:
            return False

    def count_strikes(self, color) -> int:
        strikes = 0
        for number in self.rows[color]:
            if number is True:
                strikes += 1
        return strikes

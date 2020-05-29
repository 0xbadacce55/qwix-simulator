class Board:
    def __init__(self):
        self.rows[RED] = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11:False, 12: False}
        self.furthest[RED] = 1
        self.rows[YELLOW] = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11:False, 12: False}
        self.furthest[YELLOW] = 1
        self.rows[BLUE] = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11:False, 12: False}
        self.furthest[BLUE] = 1
        self.rows[GREEN] = {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11:False, 12: False}
        self.furthest[GREEN] = 1
        self.fehlwurfe = 0

    def move(color, number):
        pass

    def is_legal_move(color, number):
        pass

    def count_strikes(color):
        pass

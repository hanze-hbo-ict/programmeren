class Board:
    """A data type representing a Connect-4 board
    with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[" "] * width for row in range(height)]

        # We hoeven niets terug te geven vanuit een constructor!

    def __repr__(self):
        """This method returns a string representation
        for an object of type Board.
        """
        s = ""  # de string om terug te geven
        for row in range(0, self.height):
            s += "|"
            for col in range(0, self.width):
                s += self.data[row][col] + "|"
            s += "\n"

        s += (2 * self.width + 1) * "-"  # onderkant van het bord

        # hier moeten de nummers nog onder gezet worden
        s += "\n"
        for i in range(self.width):
            s += " " + str(i % 10)

        return s  # het bord is compleet, geef het terug

    def add_move(self, col, ox):
        """Adds a stone for player ox to column col"""
        i = 0
        while i < self.height and self.data[i][col] == " ":
            i += 1
        self.data[i - 1][col] = ox

    def clear(self):
        """Clears the board"""
        self.data = [[" "] * self.width for _ in range(self.height)]

    def set_board(self, move_string):
        """Accepts a string of columns and places
        alternating checkers in those columns,
        starting with 'X'.

        For example, call b.set_board('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.set_board('000000') to
        see them alternate in the left column.

        move_string must be a string of one-digit integers.
        """
        next_checker = "X"  # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == "X":
                next_checker = "O"
            else:
                next_checker = "X"

    def allows_move(self, col):
        """Checks whether column col can be played"""
        return 0 <= col < self.width and self.data[0][col] == " "

    def is_full(self):
        """Checks whether the board is full"""
        for col in range(self.width):
            if self.allows_move(col):
                return False
        return True

    def del_move(self, col):
        """Removes a stone from column col"""
        i = 0
        while i < self.height and self.data[i][col] == " ":
            i += 1
        if i < self.height:
            self.data[i][col] = " "

    def wins_for(self, ox):
        """Checks whether player ox wins the game"""
        for y in range(self.height):
            for x in range(self.width):
                if (
                    in_a_row_n_east(ox, y, x, self.data, 4)
                    or in_a_row_n_south(ox, y, x, self.data, 4)
                    or in_a_row_n_southeast(ox, y, x, self.data, 4)
                    or in_a_row_n_northeast(ox, y, x, self.data, 4)
                ):
                    return True
        return False

    def host_game(self):
        """Plays a game of Connect Four"""
        ox = "O"
        while True:
            # druk het bord af
            print(self)

            # controleer of het spel afgelopen is
            if self.wins_for(ox):
                print(ox, "heeft gewonnen!")
                break
            elif self.is_full():
                print("Gelijkspel!")
                break

            # verander de huidige speler
            if ox == "O":
                ox = "X"
            else:
                ox = "O"

            # laat de speler een kolom kiezen
            col = -1
            while not self.allows_move(col):
                col = int(input("Kolom voor " + ox + ": "))

            # voer de zet uit
            self.add_move(col, ox)

    def play_game(self, px, po, show_scores=False):
        """
        Plays a game of Connect Four between players px and po.
        If show_scores is True, the player's board evaluations are printed each turn.
        """
        ox = "O"
        while True:
            # druk het bord af
            print(self)

            # controleer of het spel afgelopen is
            if self.wins_for(ox):
                print(f"{ox} heeft gewonnen!")
                break
            elif self.is_full():
                print("Gelijkspel!")
                break

            # verander de huidige speler
            if ox == "O":
                ox = "X"
                player = px
            else:
                ox = "O"
                player = po

            if player == "human":
                # laat de menselijke speler een kolom kiezen
                col = -1
                while not self.allows_move(col):
                    col = int(input("Kolom voor " + ox + ": "))
            else:
                # de computerspeler berekent een zet
                if show_scores:
                    scores = player.scores_for(self)
                    print("Scores voor ", ox, ":", [int(sc) for sc in scores])
                    col = player.tiebreak_move(scores)
                else:
                    col = player.next_move(self)

            # voer de zet uit
            self.add_move(col, ox)


def in_a_row_n_east(ch, r_start, c_start, a, n):
    """Checks whether ch has n in a row starting at r_start, c_start going east"""
    if r_start < 0 or r_start >= len(a) or c_start < 0 or c_start >= len(a[0]) - n + 1:
        return False
    for i in range(0, n):
        if a[r_start][c_start + i] != ch:
            return False
    return True


def in_a_row_n_south(ch, r_start, c_start, a, n):
    """Checks whether ch has n in a row starting at r_start, c_start going south"""
    if r_start < 0 or r_start >= len(a) - n + 1 or c_start < 0 or c_start >= len(a[0]):
        return False
    for i in range(0, n):
        if a[r_start + i][c_start] != ch:
            return False
    return True


def in_a_row_n_southeast(ch, r_start, c_start, a, n):
    """Checks whether ch has n in a row starting at r_start, c_start going southeast"""
    if (
        r_start < 0
        or r_start >= len(a) - n + 1
        or c_start < 0
        or c_start >= len(a[0]) - n + 1
    ):
        return False
    for i in range(0, n):
        if a[r_start + i][c_start + i] != ch:
            return False
    return True


def in_a_row_n_northeast(ch, r_start, c_start, a, n):
    """Checks whether ch has n in a row starting at r_start, c_start going northeast"""
    if (
        r_start < n - 1
        or r_start >= len(a)
        or c_start < 0
        or c_start >= len(a[0]) - n + 1
    ):
        return False
    for i in range(0, n):
        if a[r_start - i][c_start + i] != ch:
            return False
    return True

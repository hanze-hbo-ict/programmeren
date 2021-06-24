# tests voor in_a_row_n_east
a = create_a(5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
assert in_a_row_n_east('O', 1, 1, a, 4)
assert in_a_row_n_east('O', 1, 3, a, 2)
assert not in_a_row_n_east('X', 3, 2, a, 4)
assert in_a_row_n_east('O', 4, 0, a, 5)


# tests voor in_a_row_n_south
a = create_a(5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
assert not in_a_row_n_south('X', 0, 0, a, 5)
assert in_a_row_n_south('O', 1, 1, a, 4)
assert not in_a_row_n_south('O', 0, 1, a, 6)
assert in_a_row_n_south('X', 4, 3, a, 1)


# tests voor in_a_row_n_southeast
a = create_a(5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX')
assert in_a_row_n_southeast('X', 1, 1, a, 4)
assert not in_a_row_n_southeast('O', 0, 1, a, 3)
assert in_a_row_n_southeast('O', 0, 1, a, 2)
assert not in_a_row_n_southeast('X', 3, 0, a, 2)


# tests voor in_a_row_n_northeast
a = create_a(5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX')
assert in_a_row_n_northeast('X', 4, 0, a, 5)
assert in_a_row_n_northeast('O', 4, 1, a, 4)
assert not in_a_row_n_northeast('O', 2, 0, a, 2)
assert not in_a_row_n_northeast('X', 0, 3, a, 1)
def tower_of_hanoi(n, A, B, C):
    # Base condition
    if n == 1:
        print("Move disk 1 from {} to {}".format(A, C))
    else:
        # function is called two times
        tower_of_hanoi(n - 1, A, C, B)
        print("Move disk {} from {} to {}".format(n, A, C))
        tower_of_hanoi(n - 1, B, A, C)


tower_of_hanoi(3, 'A', 'B', 'C')

def spiral_matrix(n):
    "x and y represent coords or current position. initialized to (0, 0) -> top left corner"
    x = 0 
    y = 0

    """dx and dy represent movement directions. they are as follows:
        RIGHT: dx = 1, dy = 0
        LEFT : dx = -1, dy = 0
        UP: dx = 0, dy = 1
        DOWN: dx = 0, dy = -1
        initialized to dx = 1, dy = 0 because we want to move RIGHT initially
        """
    xdirection = 1
    ydirection = 0

    """
    this is our matrix. it is initialized to a n * n matrix where each item in each row == 0
    """
    res = []

    for item in range(n):
        row = []
        for j in range(n):
            row.append(0)
        res.append(row)


    for i in range(n * n):
        res[ydirection][xdirection] = i + 1 #want to start filling the matrix with 1 and not 0 hence i + 1
        """
        the conditions below check if we need to change direction:
        0 <= x + dx < n: checks if we're out of bounds when moving right.
        0 <= y + dy < n: checks if we're out of bounds moving left.
        res[y+dy][x+dx] != 0: checks if the cell is not zero (we've already visited that cell if cell != 0)
        """
        if not 0 <= x + xdirection < n or not 0 <= y + ydirection < n or res[y+ydirection][x+xdirection] != 0:
            """if any condition above is true, direction must change:
            if we're moving right (dx = 1, dy = 0) but youre out of bounds, we apply -dy to dx and apply dx to dy.
            so, dx = 0 and dy = 1 which means we are switching to downward direction
            """
            xdirection, ydirection = -ydirection, xdirection

        x += xdirection
        y += ydirection #this is here so we can actually traverse each cell in the matrix!

    return res


print(spiral_matrix(5))
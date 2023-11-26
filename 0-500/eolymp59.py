def count_crossed_cells(N, summits):
    crossed_cells = set()

    for i in range(N - 1):
        x1, y1 = summits[i]
        x2, y2 = summits[i + 1]

        # Swap the coordinates if needed so that x1 <= x2
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        # Iterate through the cells that the line passes through
        for x in range(x1, x2 + 1):
            slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')
            y = y1 + slope * (x - x1)

            # Round to the nearest integer as cells have integer coordinates
            y = round(y)

            # Add the cell to the set
            crossed_cells.add((x, y))

    # Count the total number of unique cells
    total_crossed_cells = len(crossed_cells)
    return total_crossed_cells

# Example usage
if __name__ == "__main__":
    N = int(input())
    summits = [list(map(int, input().split())) for _ in range(N)]

    result = count_crossed_cells(N, summits)
    print(result)
?
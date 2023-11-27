def perform_fold(coordinates, hole, fold):
    x, y = hole
    direction, position = fold

    if direction == 'X':
        new_coordinates = [(x, y) if x <= position else (2 * position - x, y) for x, y in coordinates]
    else:
        new_coordinates = [(x, y) if y <= position else (x, 2 * position - y) for x, y in coordinates]

    new_holes = set([(x, y) for x, y in new_coordinates if x == position or y == position])

    return new_coordinates, new_holes

def find_holes(R, T, HX, HY, F, folds):
    paper = set([(x, y) for x in range(R + 1) for y in range(T + 1)])
    hole = (HX, HY)
    paper.remove(hole)

    for fold in folds:
        paper, hole = perform_fold(paper, hole, fold)

    return len(paper)

def main():
    T = int(input())
    for _ in range(T):
        R, T, HX, HY, F = map(int, input().split())
        folds = []
        for _ in range(F):
            direction, position = input().split()
            folds.append((direction, int(position)))
        result = find_holes(R, T, HX, HY, F, folds)
        print(result)

if __name__ == "__main__":
    main()
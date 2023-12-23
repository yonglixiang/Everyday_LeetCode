class SolutionA:
    """Use matrix"""
    def isPathCrossing(path: str) -> bool:
        length = len(path)
        width = (len(path) + 1) * 2
        
        pathMatrix = [[0 for _ in range(width)] for _ in range(width)]
        x, y = length, length
        pathMatrix[x][y] = 1
        
        for i in range(0, length):
            if path[i] == 'N':
                y += 1
            elif path[i] == 'S':
                y -= 1
            elif path[i] == 'E':
                x += 1
            elif path[i] == 'W':
                x -= 1
                
            if pathMatrix[x][y] == 1:
                return True
            else:
                pathMatrix[x][y] = 1
                
        return False

class SolutionB:
    """Use Dictionary"""
    def isPathCrossing(path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}
        
        for direction in path:
            if direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            
            if (x, y) in visited:
                return True
            else:
                visited.add((x,y))
                
        return False
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x_direction, y_direction = 0, 1
        x, y = 0, 0
        
        for direction in instructions:
            if direction == 'G':
                x, y = x + x_direction, y + y_direction
            elif direction == 'R':
                x_direction, y_direction = y_direction, x_direction * -1
            elif direction == 'L':
                x_direction, y_direction = -1*y_direction, x_direction
        
        if (x, y) == (0, 0):
            return True
        elif (x_direction, y_direction) != (0, 1):
            return True
        
        return False
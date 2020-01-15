class Plateau:
    def __init__(self, x_limit, y_limit):
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.rovers = []
    
    def addRover(self, rover):
        self.rovers.append(rover)

    def moveRover(self, roverIndex, instruction):
        self.rovers[roverIndex].move(instruction)
        if self.rovers[roverIndex].x > self.x_limit:
            self.rovers[roverIndex].x = self.x_limit
        if self.rovers[roverIndex].y > self.y_limit:
            self.rovers[roverIndex].y = self.y_limit

    def __str__(self):
        rovers_data = ''
        for rover in self.rovers:
            rovers_data = rovers_data + str(rover)

        return rovers_data

class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, instruction):
        turn_left = {
            'N' : 'W',
            'W' : 'S',
            'S' : 'E',
            'E' : 'N'
        } 

        turn_right = {
            'E' : 'S',
            'S' : 'W',
            'W' : 'N',
            'N' : 'E'
        }

        if instruction == 'M' :
            if self.direction == 'N':
                self.y = self.y + 1
            elif self.direction == 'S':
                self.y = self.y - 1
            elif self.direction == 'W':
                self.x = self.x - 1
            else:
                self.x = self.x + 1
        elif instruction == 'L' :
            self.direction = turn_left[self.direction]
        elif instruction == 'R' :
            self.direction = turn_right[self.direction]

    def __str__(self):
        return str(self.x) + ' ' + str(self.y) + ' ' + self.direction + '\n'

def main():
    file = open('input.txt', 'r')
    lines = file.readlines()

    gridLimits = lines[0].rstrip().split(' ')
    plateau = Plateau(int(gridLimits[0]), int(gridLimits[1]))
    
    for i in range(1, len(lines), 2):
        roverXY = lines[i].rstrip().split(' ')
        newRover = Rover(int(roverXY[0]), int(roverXY[1]), roverXY[2])
        plateau.addRover(rover= newRover)

        for instruction in lines[i+1]:
            plateau.moveRover(int(i/2), instruction)
        

    print(plateau)

if __name__ == "__main__":
    main()
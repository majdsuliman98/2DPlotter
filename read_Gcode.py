
from dataclasses import dataclass

@dataclass
class Coordinates:
    x:float
    y:float
    z:float

class plotter:
    gcodelines = []
    

    def read_gcode(self,filename):
        with open('Gcodes/{}.gcode'.format(filename)) as gcode:
            lines = gcode.readlines()
            self.gcodelines = lines
        
  
    def parse_gcode(self):
        self.coordinates = []
        for line in self.gcodelines:
                line = line.strip()
                if line.startswith("G1") and line[2:].strip():
                    values = line[2:].split()
                    x = float([value[1:] for value in values if value[0] == 'X'][0])
                    y = float([value[1:] for value in values if value[0] == 'Y'][0])
                    z = float([value[1:] for value in values if value[0] == 'Z'][0])
                    self.coordinates.append((x, y, z))
                    self.point = Coordinates(x,y,z)
                    self.sendCommand()
        
    def sendCommand(self):
            print("Sending command to stepper motors")
            print("moving to point X = {} Y = {} Z = {}".format(self.point.x,self.point.y,self.point.z))

       


        

p = plotter()
p.read_gcode("cam")
p.parse_gcode()


# print(coordinates)


# Testing new functions
 
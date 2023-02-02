
from dataclasses import dataclass
from drivers import *
@dataclass
class Coordinates:
    x:float
    y:float
    z:float

class Gcode:
    def __init__(self):
        self.coordinates = []
      

    def read_gcode(self,filename):
        with open('Gcodes/{}.gcode'.format(filename)) as gcode:
            lines = gcode.readlines()
            self.gcodelines = lines
        self.parse_gcode()
  
    def parse_gcode(self):
       
        for line in self.gcodelines:
                line = line.strip()
                if line.startswith("G1") and line[2:].strip():
                    values = line[2:].split()
                    x = float([value[1:] for value in values if value[0] == 'X'][0])
                    y = float([value[1:] for value in values if value[0] == 'Y'][0])
                    z = float([value[1:] for value in values if value[0] == 'Z'][0])
                    self.coordinates.append((x, y, z))
                    # self.point = Coordinates(x,y,z)
        
                    
    
    def startDrawing(self):
            main(self.coordinates)
            # print(self.coordinates[len(self.coordinates)-1])
            # for i in self.coordinates:
            #     if(i == self.coordinates[len(self.coordinates)-1]):
            #         print("last")
            
       


        

# p = plotter()
# p.read_gcode("frames")
# p.parse_gcode()


# print(coordinates)


# Testing new functions
 
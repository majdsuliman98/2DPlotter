
class printer:
    #Steps per revolution 
    StepM = 44

    #Limits 
    Xmin = 0
    Xmax = 40
    Ymin = 0 
    Ymax = 40
    Zmin = 0 
    Zmax = 1

    #Steps per millimeter 
    StepX = 100
    StepY = 100

    #Initial position 
    Xpos = Xmin
    Ypos = Ymin
    Zpos = Zmin

    def read_gcode(self,filename):
        with open('Gcodes/{}.gcode'.format(filename)) as gcode:
            lines = gcode.readlines()
        self.gcodelines = lines

    def processGcode(self):
       command = self.gcodelines
       for i in range(len(command)):
            self.l = command[i].split(" ")
            self.currentindex = i
            self.sendCommand()
    
    def sendCommand(self):
       
        if(self.l[0] == "G1"):
            print("Sending command to stepper motors {}".format(self.l[0]))
            print("moving to point {}, {}".format(self.l[1],self.l[2]))

        elif(self.l[0] == "G4"):
            print("Sending command to stepper motors {}".format(self.l[0]))
            print("dwelling for {} millisecond".format(self.l[1]))

        elif(self.l[0] == "M300"):
            print("Sending command to stepper motors {}".format(self.l[0]))
            if(self.l[1] == "S1.00"):
                print("pen is going up")   
            else:
                print("pen is going down")
        else:
            print("headline")


        

p = printer()
p.read_gcode("1")
p.processGcode()

# Testing new functions
 
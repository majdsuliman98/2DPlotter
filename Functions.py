
from subprocess import call,Popen,PIPE
from io import BytesIO
from time import sleep
from picamera import PiCamera
from cv2 import *
import fileinput
from PIL import Image
import platform
from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces

# sys.path.append('PICTOPLOT-MASTER/py-svg2gcode')

 
import sys
sys.path.insert(1, './inkscape')
import unicornlib

def openCamera():
   print("taking a picture")
   my_stream = BytesIO()
   camera = PiCamera()

   return camera.start_preview()





def img2bmp(imagepth,filename):
  
   Image.open(imagepth).save("./PBM images/{}.bmp".format(filename))
   # doc = aw.Document()
   # builder = aw.DocumentBuilder(doc)

   # shapes = [builder.insert_image(imagepth)]

   # # Calculate the maximum width and height and update page settings 
   # # to crop the document to fit the size of the pictures.
   # pageSetup = builder.page_setup
   # pageSetup.page_width = max(shape.width for shape in shapes)
   # pageSetup.page_height = sum(shape.height for shape in shapes)
   # pageSetup.top_margin = 0
   # pageSetup.left_margin = 0
   # pageSetup.bottom_margin = 0
   # pageSetup.right_margin = 0

   # doc.save('./PBM images/'+str(filename[0])+".bmp");




def CovertToPBM(threshold,name):
    #Code to convert the bmp to a pbm
    print ("Converting output.bmp to output.pbm")
    call(["mkbitmap",'-x', "-t"+str(threshold),'./PBM images/'+str(name)+".bmp"])  



def ConvertToSVG(name):
    #Converting tmp/photo.pbm to tmp/photo.svg
    print ("Converting output.bmp to output.svg")
    #We -t200 handles the size of blobs we want to discard and it will convert to 40mmx40mm size
    #call(["potrace","--svg","-t200","-P 40mmx40mm","-W 40mm","-H40mm","--tight","tmp/photo.pbm"])
    call(["potrace","--svg","-t100","-P 40mmx40mm","-W 40mm","--tight", '-o','./SVG/{}.svg'.format(name),'./PBM images/'+str(name)+".bmp"]) 

def FixSvgHeader(name):
      #code to remove the pt
      print ("Removing pt and offsetting the svg ready for plotting")
      f =fileinput.FileInput('./SVG/'+str(name)+".svg", inplace=True)
      for line in f:#loop through the lines
         # if line.startswith("<g transform="):#find the transform line
         #    scale=0.0105000#Fit Page
         #    if platform.system()=="Windows":
         #       scale=0.009500#Looks Better
         #    else:
         #       scale=0.009500#Looks Better
         #    # print('<g transform="translate(60.082978,20.809088) scale('+str(scale)+',-'+str(scale)+')"')#write the off set
         # else:    
            print(line.replace('pt"', '"'))#remove the pt
      f.close()#Tidy up

  
def ConvertToGCode(name):
   #Convert svg to gcode data
   print ("Convert svg to gcode data")
   print(name)
   e = unicornlib.MyEffect()
   e.affect(['--tab="plotter_setup"', '--pen-up-angle=0', '--pen-down-angle=1', '--start-delay=150', '--stop-delay=150', '--xy-feedrate=3500', '--z-feedrate=150', '--z-height=0', '--finished-height=0', '--register-pen=true', '--x-home=0', '--y-home=0', '--num-copies=1', '--continuous=false', '--pause-on-layer-change=false','./SVG/{}.svg'.format(str(name))])
   
   #Writing the gcode file
   #   print "Writing the gcode file"
   file = open("Gcodes/{}.gcode".format(str(name)),"w") 

   for c in e.context.codes:
      
      file.write(c + '\n') 
   file.close()
        

# ConvertToGCode('68747470733a2f2f7261772e6769746875622e636f6d2f6d696b6f6c616c7973656e6b6f2f6c656e612f6d61737465722f6c656e612e706e67')


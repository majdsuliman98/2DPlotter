import RPi.GPIO as GPIO
import threading
import queue
from time import sleep

# limit switches
LIM_SW_X = 17
LIM_SW_Y = 27
LIM_SW_Z = 22

# stepper motors
DIR_X = 14
STEP_X = 15

DIR_Y = 5
STEP_Y = 6

DIR_Y2 = 13
STEP_Y2 = 19

DIR_Z = 23
STEP_Z = 24

CW = 1 # clockwise rotation
CCW = 0  # counterclockwise rotation
steps_per_rev = 200 # Steps/revolution for NEMA17 | 360deg / 1.8deg
XY_delay = .005/2 # .005s -> 1 rev/s  | Delay for X and Y axes
Z_delay = .005 * 4 # Delay for Z axis
d = 8 / 200 # 8mm is the step of the screw, 200 is the n of steps for a full rotation
alpha = 360 / steps_per_rev # minimal angle based on the steps

plotter_running = True

debug_cnt1 = 0
debug_cnt2 = 0
debug_cnt3 = 0

initial_X = 0
initial_Y = 0
initial_Z = 0

current_X = 0
current_Y = 0
current_Z = 0

target_X = 0
target_Y = 0
target_Z = 0

  
def commandListener(commandQueueHandle : queue):
    global commandListener_running
    while commandListener_running:
        cmd = input()
        print("CL>> {}".format(cmd))
        commandQueueHandle.put(cmd)
        
        if cmd is "q":
            break
        
        sleep(.5)
        
    print("commandListener finished operation.")
        
def commandHandler(commandQueueHandle : queue):
    global commandHandler_running
    while commandHandler_running:
        user_input = commandQueueHandle.get()

        if user_input is not None:
            cmds = user_input.split(':')

            if len(cmds) == 2:
                cmd = cmds[0]
                val = float(cmds[1])
            elif len(cmds) == 3:
                cmd = cmds[0]
                val = float(cmds[1])
                val2 = float(cmds[2])
            else:
                cmd = user_input
                print(cmd)

            print("CH>> {}".format(user_input))
            
            if cmd == "whos a good plotter":
                print("woof woof")
            if cmd == "buzz_x_cw":
                print(">> Buzzing stepper X")
                setStepperDirection(DIR_X, CW)
                update_stepper(STEP_X, XY_delay)
            if cmd == "buzz_y_cw":
                print(">> Buzzing stepper Y")
                setStepperDirection(DIR_Y, CW)
                update_stepper(STEP_Y, XY_delay)
            if cmd == "buzz_y2_cw":
                print(">> Buzzing stepper Y2")
                setStepperDirection(DIR_Y2, CW)
                update_stepper(STEP_Y2, XY_delay)
            if cmd == "buzz_z_cw":
                print(">> Buzzing stepper Z")
                setStepperDirection(DIR_Z, CW)
                update_stepper(STEP_Z, Z_delay)
            if cmd == "buzz_x_ccw":
                print(">> Buzzing stepper X")
                setStepperDirection(DIR_X, CCW)
                update_stepper(STEP_X, XY_delay)
            if cmd == "buzz_y_ccw":
                print(">> Buzzing stepper Y")
                setStepperDirection(DIR_Y, CCW)
                update_stepper(STEP_Y, XY_delay)
            if cmd == "buzz_y2_ccw":
                print(">> Buzzing stepper Y2")
                setStepperDirection(DIR_Y2, CCW)
                update_stepper(STEP_Y1, XY_delay)
            if cmd == "buzz_z_ccw":
                print(">> Buzzing stepper Z")
                setStepperDirection(DIR_Z, CCW)
                update_stepper(STEP_Z, Z_delay)
            if cmd == "set_target_X":
                setPositionStepperX(val)
                print(">> Setting target X position to: {}".format(val))
            if cmd == "set_target_Y":
                setPositionStepperY(val)
                print(">> Setting target Y position to: {}".format(val))
            if cmd == "set_target_Z":
                setPositionStepperZ(val)
                print(">> Setting target Z position to: {}".format(val))
            if cmd == "set_pos":
                print(">> Setting target XY position to: X{} Y{}".format(val, val2))
                setPositionXY(val, val2)
            if cmd == "q":
                global plotter_running
                plotter_running = False
               
        sleep(.5)
        
    print("commandHandler finished operation.")
        
def motorX_Handler(motorQueueHandle : queue):
    global initial_X
    global current_X
    global target_X
    global motorX_Handler_running

    delay = 0
    while motorX_Handler_running:
        if round(abs(target_X - current_X), 4) >= d:
            if (abs(target_X - current_X) < abs(target_Y - current_Y)):
                delay = calculate_scaled_dt()
            else: 
                delay = XY_delay

            print("X delay: {}[s]".format(delay))

            vel = getVelocity(delay)

            if target_X > current_X:            # if the target is greater than current position, spin CW
                setStepperDirection(DIR_X, CW)
                current_X += delay * vel
            elif target_X < current_X:          # if the target is lower than current position, spin CCW
                current_X -= delay * vel
                setStepperDirection(DIR_X, CCW)
    
            update_stepper(STEP_X, delay)
            print("Current: {} | Target: {}".format(current_X, target_X))
      
    print("motorX_Handler finished operation.")

def motorY_Handler(motorQueueHandle : queue):
    global initial_Y
    global current_Y
    global target_Y
    global motorY_Handler_running

    delay = 0
    while motorY_Handler_running:
        if round(abs(target_Y - current_Y), 4) >= d:
            if (abs(target_X - current_X) > abs(target_Y - current_Y)):
                delay = calculate_scaled_dt()
            else: 
                delay = XY_delay

            print("Y delay: {}[s]".format(delay))

            vel = getVelocity(delay)

            if target_Y > current_Y:            # if the target is greater than current position, spin CW
                setStepperDirection(DIR_Y, CW)
                setStepperDirection(DIR_Y2, CW)
                current_Y += delay * vel
            elif target_Y < current_Y:          # if the target is lower than current position, spin CCW
                current_Y -= delay * vel
                setStepperDirection(DIR_Y, CCW)
                setStepperDirection(DIR_Y2, CCW)
    
            update_stepper(STEP_Y, delay)
            update_stepper(STEP_Y2, delay)
            # print("Current: {} | Target: {}".format(current_Y, target_Y))

        # if round(abs(target_Z - current_Z), 4) >= alpha:
        #     ang_vel = getAngularVelocity(Z_delay)

        #     if target_Z > current_Z:            # if the target is greater than current position, spin CW
        #         setStepperDirection(DIR_Z, CW)
        #         current_Z += Z_delay * ang_vel
        #     elif target_Z < current_Z:          # if the target is lower than current position, spin CCW
        #         current_Z -= Z_delay * ang_vel
        #         setStepperDirection(DIR_Z, CCW)
    
        #     update_stepper(STEP_Z, Z_delay)
        #     print("Current: {} | Target: {}".format(round(current_Z, 4), target_Z))
      
    print("motorY_Handler finished operation.")

def setPositionStepperX(target:float):
    global target_X
    target_X = target

def setPositionStepperY(target:float):
    global target_Y
    target_Y = target

def setPositionStepperZ(target:float):
    global target_Z
    target_Z = target

def setPositionXY(pos_X:float, pos_Y:float):
    global target_X
    global target_Y
    target_X = pos_X
    target_Y = pos_Y

    global initial_X
    global initial_Y
    global current_X
    global current_Y
    initial_X = current_X
    initial_Y = current_Y

def calculate_scaled_dt():
    global target_X
    global target_Y

    global initial_X
    global initial_Y

    D = 0 # longer distance
    d = 0 # shorter distance

    if (abs(target_X - initial_X) > abs(target_Y - initial_Y)):
        D = abs(target_X - initial_X)
        d = abs(target_Y - initial_Y)
    else:
        d = abs(target_X - initial_X)
        D = abs(target_Y - initial_Y)

    ratio = D / d
    scaled_dt = ratio * XY_delay

    return scaled_dt

def setStepperDirection(dir_pin:int, direction:bool):
    GPIO.output(dir_pin, direction)

def getVelocity(dt:float) -> float:
    global d
    velocity = d / dt
    # print("Velocity: {} [mm/s]".format(velocity))
    return velocity

def getAngularVelocity(dt:float) -> float:
    angular_velocity = 360 / steps_per_rev / dt
    # print("Angular Velocity: {} [deg/s]".format(angular_velocity))
    return angular_velocity

def update_stepper(step_pin:int, dt:float):
    GPIO.output(step_pin, GPIO.HIGH)
    sleep(dt/2)
    GPIO.output(step_pin, GPIO.LOW)
    sleep(dt/2)

def hardware_setup() -> bool:
    try:
        GPIO.setmode(GPIO.BCM)

        # limit switch setup
        GPIO.setup(LIM_SW_X, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(LIM_SW_Y, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(LIM_SW_Z, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # adding interrupts to the limit switch pins
        GPIO.add_event_detect(LIM_SW_X, GPIO.RISING, callback=LIM_SW_X_pressed, bouncetime=25)
        GPIO.add_event_detect(LIM_SW_Y, GPIO.RISING, callback=LIM_SW_Y_pressed, bouncetime=25)
        GPIO.add_event_detect(LIM_SW_Z, GPIO.RISING, callback=LIM_SW_Z_pressed, bouncetime=25)

        # stepper motor setup
        GPIO.setup(DIR_X, GPIO.OUT)
        GPIO.setup(STEP_X, GPIO.OUT)

        GPIO.setup(DIR_Y, GPIO.OUT)
        GPIO.setup(STEP_Y, GPIO.OUT)
        
        GPIO.setup(DIR_Y2, GPIO.OUT)
        GPIO.setup(STEP_Y2, GPIO.OUT)
        
        GPIO.setup(DIR_Z, GPIO.OUT)
        GPIO.setup(STEP_Z, GPIO.OUT)

        return True

    except:
        return False

def LIM_SW_X_pressed(channel) -> bool:
    global debug_cnt1
    debug_cnt1 = 1
    
def LIM_SW_Y_pressed(channel) -> bool:
    global debug_cnt2
    debug_cnt2 = 1

def LIM_SW_Z_pressed(channel) -> bool:
    global debug_cnt3
    debug_cnt3 = 1

def distance_to_steps(distance:float) -> int:
    SPR = 200 # steps per revolution
    trap_screw_const = 8 # 8 mm screw jump
    N_steps = round(SPR * distance / trap_screw_const)

    return N_steps

def angle_to_steps(angle:float) -> int:
    SPR = 200 # steps per revolution
    N_steps = round(angle / 360 * 200)

    return N_steps

def main():
    hardware_setup_done = False
      
    # queues
    commandQueueHandle = queue.Queue(maxsize = 4)
    motorQueueHandle = queue.Queue(maxsize = 64)
    
    # motor state variables
    global commandListener_running, commandHandler_running, motorX_Handler_running, motorY_Handler_running
    commandListener_running = True
    commandHandler_running = True
    motorX_Handler_running = True
    motorY_Handler_running = True
    
    # create the threads
    commandListenerThread = threading.Thread(target=commandListener, args=(commandQueueHandle,))
    commandHandlerThread = threading.Thread(target=commandHandler, args=(commandQueueHandle,))
    motorX_HandlerThread = threading.Thread(target=motorX_Handler, args=(motorQueueHandle,))
    motorY_HandlerThread = threading.Thread(target=motorY_Handler, args=(motorQueueHandle,))
    
    # start the threads
    commandListenerThread.start()
    commandHandlerThread.start()
    motorX_HandlerThread.start()
    motorY_HandlerThread.start()
        
    try:
        while plotter_running: 
            if not hardware_setup_done:
                if not hardware_setup():
                    print("Hardware Setup failed!")
                    # shut down the machine
                    plotter_on = False
                    continue

                hardware_setup_done = True
                print("Hardware setup successful!")
            
            global debug_cnt1, debug_cnt2, debug_cnt3
            if debug_cnt1 == 1:
                print("LIM1 pressed")
                debug_cnt1 = 0
            elif debug_cnt2 == 1:
                print("LIM2 pressed")
                debug_cnt2 = 0
            elif debug_cnt3 == 1:
                print("LIM3 pressed")
                debug_cnt3 = 0

            sleep(.5)
            
    except:
        print("An enormous hell broke lose.")
                
    finally:
        # disable threads
        commandListener_running = False
        commandHandler_running = False
        motorX_Handler_running = False
        motorY_Handler_running = False
        
        commandListenerThread.join()
        commandHandlerThread.join()  
        motorX_HandlerThread.join()
        motorY_HandlerThread.join()
      
        GPIO.cleanup()
        print("Cleanup done.")
        
        print("END")

if __name__ == "__main__":
    main()

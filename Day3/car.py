#car game
user_input = ""
is_car_running = False

while user_input != "QUIT":
    user_input = input(">").upper()
    
    if user_input == "HELP":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit
        """)
    
    elif user_input == "START":
        if is_car_running == True:
            print("Car is already running...")
        else:
            print("Car started...Ready to go!")
            is_car_running = True
            
    elif user_input == "STOP":
        if is_car_running == False:
            print("Car isn't running...")
        else:
            print("Car stopped.")
            is_car_running = False
            
    elif user_input =="QUIT":
        print("Goodbye!")
        break
    
    else:
        print("i don't understand that...")
        
   
        
        
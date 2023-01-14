from time import sleep
import random


def passenger_request() -> int:
    
    call = random.randint(0,10)
    
    print(f"privolali ma na {call}.poschodie...idem tam")
    
    return call


def passenger_ride() -> int:
    
    while True:
        
        try:
            floor_request = int(input("vyberte poschodie 0 - 10: "))
            
        except:
            continue
            
        if floor_request in range(11):
            
            print(f"ideme na {floor_request}.poschodie")
            return floor_request


def go_up(request: int, floor: int) -> int:

    while request != floor:
        print(floor)
        print("idem hore")
        floor += 1
        
    print(floor)
    
    return floor


def go_down(request: int, floor: int) -> int:
    
    while request != floor:
        print(floor)
        print("idem dole")
        floor -= 1
        
    print(floor)
    
    return floor


def exit_message(new_floor: int) -> str:
    
    e_message = f"sme na {new_floor}.poschodi"
    
    return e_message


def decision(request: int, floor: int):
    
    new_floor = None
    message = ""
    
    if  request == floor:
        new_floor = floor
        message = exit_message(new_floor)
        

    elif request > floor:
        new_floor = go_up(request, floor)
        message = exit_message(new_floor)
        
    else:
        new_floor = go_down(request, floor)
        message = exit_message(new_floor)
    
    print(message)
    
    return new_floor


def elevator():
    
    starter_lst = ["VÝŤAH SA ZAPÍNA", "-----ON-----", "čakám, kým ma niekto privolá"]

    for item in starter_lst:
        print(item); sleep(1)

    ride = 1
    
    while ride < 3:
        
        start_floor = 0
        
        p_request = passenger_request()
        
        p_pickup = decision(p_request, start_floor)
        
        p_selection = passenger_ride()
        
        p_ride = decision(p_selection, p_pickup)
        
        start_floor = p_ride
        
        ride += 1
        
    print("PORUCHA!!! vytah sa pokazil...pouzite prosim schodisko"); sleep(1)
    print("-----OFF-----")

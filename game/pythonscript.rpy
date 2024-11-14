
init python:
    def movePlayer(room, isSkip =False):
        global location_user
        if isSkip:
                if location_user == "hallway":
                    return Jump("start")
                elif location_user == "room 1":
                    return Jump("rm1")
                elif location_user == "room 2":
                    return Jump("rm2")
                elif location_user =="room 3":
                    return Jump("rm3")
    
        else:
                if room == "hallway":
                    return Jump("start")
                elif room == "room 1":
                    return Jump("rm1")
                elif room == "room 2":
                    return Jump("rm2")
                elif room =="room 3":
                    return Jump("rm3")
  
    def moveStranger():
        global location_stranger, location_user
        renpy.show("Stranger", at_list=[right],layer= "screens")

        if events == 2 or events == 5:
            location_stranger = "hallway"
        elif events == 3 or events == 4:
            location_stranger ="room 3"
        else:
            location_stranger = "room 2"

        if location_stranger == location_user:
            
            renpy.say(stranger, "AHA! FOUND YOU!{w=1}{nw}")
            renpy.say(frieren, "OMG!{w=1}{nw}")
            renpy.show_screen("gameover")
       
 
    class Inventory:
        def __init__(self, items, number_items):
            self.items = items
            self.number_items = number_items

        def add(self, item):
            self.items.append(item)
            self.number_items += 1

        def remove(self,item):
            self.items.remove(item)
            self.number_items -= 1

      

    class Items:
        def __init__ (self, name ,description, image):
            self.name =name 
            self.description = description
            self.image = image

    def door_clicked():
        renpy.call_in_new_context("warning")

    def dragged_key(dragged_items, dropped_on):
        global isUnlocked
        if dropped_on is not None:
            if dragged_items[0].drag_name =="key" and dropped_on.drag_name == "door":
                dragged_items[0].snap(dropped_on.x, dropped_on.y + 200)
                isUnlocked = True
                renpy.notify("The door is unlocked")
                inventory.items.remove(inventory.items[0])
            
        else:
            dragged_items[0].snap(dragged_items[0].start_x ,dragged_items[0].start_y )   
    

"""
    (180, 148, 84, 83)

    (181, 263, 84, 83)

    (180, 376, 82, 82)

    (183, 487, 82, 89)
"""
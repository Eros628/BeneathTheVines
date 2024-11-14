default beenfore = False
default isSkip = False
default turns = 0
default events = 0
default location_user = "hallway"
default location_stranger = "room 2"
default isUnlocked = False 
default inventory = Inventory([], 0)
define key1 = Items("key", "This key is used to room 2", "key_idle.png")

label start:
    $ location_user = "hallway"
    $ renpy.hide("Stranger",layer= "screens")

    hide screen gameover
    hide screen returnbutton

    scene hallway

    show screen iconInventory
    show screen test
    show screen turnstext

    
    if beenfore:
        show Frieren at left:
            ypos 1.4
  
    else:
        $ beenfore = True
        show Frieren at left:
            ypos 1.4
    


    
    if events == 2 or events == 5:
        pass
       


    $ ui.interact()


label rm1:
    $ location_user = "room 1"

    hide screen test
    show screen returnbutton

    scene room1
    
    show Frieren at left  with dissolve:
        ypos 1.4
    frieren "wew no ones here good to know"



    $ ui.interact()
   
    

label rm2:
    $ location_user = "room 2"
    hide screen test
    
    show screen returnbutton

    if len(inventory.items) == 0:
        show screen getkey
    
    scene room2
    show Frieren at left  with dissolve:
        ypos 1.4
    frieren "oh this is empty" with dissolve


    if events == 0 or events == 1:
        pass
       

    else: 
        frieren "oh this is empty" with dissolve
    
    $ ui.interact()



label rm3:
    $ location_user = "room 3"
    show screen returnbutton
    hide screen test

    scene room3
    
    show Frieren at left  with dissolve:
        ypos 1.4

    if events == 3 or events == 4:
        pass
       


    $ ui.interact()

label warning:
    frieren "oh this door is locked. there must be a key somewhere"
    return


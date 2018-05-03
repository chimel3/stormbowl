Storm Bowl

File Structure
Parent folder stormbowl hosts the virtual directory, with subfolder stormbowl to hold the main code and modules. Not sure about picture files etc yet.
Separate subfolder for classes.

Evolution of code
Initially I had decided to keep the primary code in functions within stormbowl.py with classes in separate files and certain functions with lots of code stored in separate Python modules.
The main function would hold the main code loop while it executes new_round function code until the end of the season.
The game board would be created as a separate class that allows each new match to have a new game board, reverting to the main routine at the end of each match.

However, this didn't work well when I started to get practically involved with creating multiple screens. Use of toplevel and multiple windows seemed clumsy as there is always the root window that needs to be running. So I either had to hide it, in which case exiting is harder to do, or keep it running which seemed messy.
I came across some code that allowed me to create each screen as a new frame, with the frame being destroyed when a new frame is created to replace it.
This worked using classes, with the main controlling part of this code also being created as a class, and this was where the initial tkinter Tk object was created. Whilst this worked, it meant that pretty much all of the code transitioned from the main function to this new class, leaving me uncertain what the point of the primary stormbowl.py code was.

Pushing code back into stormbowl.py
I then worked on moving the new controlling class - Game(), which creates the Tk object - back into stormbowl.py. This worked fine, leaving the individual frames in the separate screens.py class.
After experimenting with tkinter button code I decided that I could still execute general processing functions e.g. create_teams in stormbowl.py, executing from buttons in screens.py, with these processing functions then calling back into the Game class to run the next frame.

This still seemed sub-standard.
Firstly, I had a class - Game - in stormbowl.py rather than in a classes file.
Secondly, in order for Game to call each frame, it needed to know about any data that would need to be represented on any of the screens. Therefore, I felt that I would end up passing large amounts of data around from function to class to function. It felt better for Game to hold any information that it would need to populate screens, and would therefore also represent any Game data objects more completely.
It seemed that it would manifest itself most accutely through the game object I had created - when processing functions completed, or classes, they would need to call back to the game object to start the next frame. Therefore it seemed that the game object would be passed to every function, and any separate class or module file would need to import stormbowl.

Therefore, in response to this I did 3 things:
1) Move Game to its own class file so that it felt in the right place.
2) Move the game = Game() line from the main function in stormbowl to a separate module designed to create global variables for all modules. That way, all modules and classes needing to reference the game object could import this same module and have access to the game object without it having to be passed around.
3) The processing functions would create the objects, but they would be stored as permanent objects in the Game class, so e.g. club = Club(), but since club will be overwritten with the next club created, each club object is stored permanently in the Game class as self.clubs (a list).

This new global variables module was called config.py in line with standard convention for storing global variables in separate modules, with a start_game() function to instantiate the game object. This start_game() function would be called from stormbowl's main routine.
The Game class is then only invoked from the start_game function, which feels right as the class is hidden away.

At this stage I am starting to create some working concepts. The first is that I am attempting to code this as a series of microservices rather than a behemoth. This will allow me to transition small parts to different cloud services at a later date.
To do this, I'll need to split screens.py class into separate class files for each frame.

Abstracting away interaction with the config file
By this stage I was starting to see interaction with the stormbowl config file in lots of different modules, which meant that I was doing a lot of read operations to the same thing, and each module had to import json etc. Any changes to the structure of the config file could potentially mean making changes in lots of different places.
Therefore, I decided that it was better to centralise the config file interaction to the config module where I could then hold config file data as global variables, with different sections e.g. player or teams being held in separate variables for consumption wherever they are needed.
When doing this I decided to create a single function called get_config_data() that would produce all of the different data variables rather than different functions for each e.g. get_teams_data(), get_players_data() etc because this way I could read the config file once only. This function can then be invoked from the main stormbowl code as part of initialisation.
I was torn whether to expose each setting from the config file in an individual global variable. Initially I decided to in a bid to abstract all but config.py from the underlying json structure, but then realised that it didn't scale as regardless, I couldn't have variables for all of the individual teams and players attributes and so there had to be understanding in the other modules that were manipulating the data of the json structure, and anyway, it's just like list or dictionary objects. Therefore I decided I would create global variables for each top-level element initially e.g. players, teams, settings.

When I found myself storing the fixture list in the config file I started questioning when something belonged in config and when in game. This actually feels like game information as it's pertinent to this game only rather than being general configuration for each game.
When it comes to switching screens, I feel it makes sense to always do this from a common place, so will look to always perform it from the main stormbowl file where I can gather any needed arguments etc. Even if there are no arguments to pass I will stick with this pattern rather than do things such as call a screen from a button on a form in a previous screen. I hope that in this way it will be easier to see where things happen in the code over time, and also if I want to split out modules and functions into other places, I can do this without having to update code in lots of calling modules.
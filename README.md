# Inline-Input
![wtf](https://user-images.githubusercontent.com/75082388/162805166-ec0480cb-be5e-4463-9e1b-80bffd5b1f1c.png)


__Install library:__
```
pip install inline-input
```

__Use:__
```
# Preparing:
import inline #Import inline module
input = inline.input #replace default input

# Examples with new input:
inp = input(prefix=None) # default ">> "
inp = input(free=False) # or free=True, default is True
inp = input(minLength=2, maxLength=10) # default minLength=0, maxLength=0
inp = input(timeInfo=5) # or timeInfo=False, default is 1 second
inp = input(iHelp=2) # How many characters must the user type to be prompted to use the Autocomplete

# Autocomplete on Enter:
inline.autoCompleteOnEnter = True # Autocomplete on Enter and Tab, default False - only on Tab
inp = input(free=False) # Only your commands are allowed!

# Commands option 1:
inline.commands = ["Info", "Help", "Version", "Cls"]
inp = input() #Autocomplete with your commands on Tab

# Commands option 2:
inp = input(command=["Help", "Info", "Version"]) # or use inline.commands = ["Help", "Info", "Version"]

#Functions:
inline.clear_console(lineDel=1) #Delete one line of console
inline.predict(text, list) # Predicting a similar word
inline.isCommand(text, list) # Does the command exist on the list
```
Commands options:
```
#1
import inline #Import inline module
input = inline.input #replace default input

inline.commands = ["Info", "Help", "Version"]

answer = input("Command: ", free=False) # The Free=False parameter prohibits sending other commands not from the list
```
OR:
```
#2
import inline #Import inline module
input = inline.input #replace default input

commands = ["Info", "Help", "Version"]

answer = input(free=False, command=commands)
```
---
Example code:
```
#Navigating through folders
import os
import inline #Import inline module
input = inline.input #replace default input
path = "C:\\" #Default path

while True:
    commands = os.listdir(path)
    print("Choose directory:")

    for command in commands:
        if not command.startswith("$"):
            print(f"- {command}")
        else:
            commands.remove(command)

    inp = input(command=commands, cursor=False)
    os.system('cls')

    if inp == "." or inp.lower() == "return": # go back
        path = path[:-(len(path.split("\\")[-2]) + 2)] + "\\"
    elif os.path.isdir(path + inp + "\\"):
        path += inp + "\\"
    else:
        if os.path.isfile(path + inp):
            print("You want open the file?")
            inp_ = input(command=["Yes", "No"], free=False) # Free=False forces the user to use strictly our commands
            if inp_.lower() == "yes":
                os.system(path + inp)
        else:
            print("Directory does not exist:", path + inp + "\\", end="\n\n")
```

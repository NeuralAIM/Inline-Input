# Inline-Input
This module provides functions for predicting user input, checking if user input matches a command, and for inputting and formatting text with a prefix and/or postfix.

![wtf](https://user-images.githubusercontent.com/75082388/162805166-ec0480cb-be5e-4463-9e1b-80bffd5b1f1c.png)

## Getting started

__Install library:__
```
pip install inline-input
```
_Additional libraries will also be automatically installed to make it work: thefuzz, colorama_

### Predictions
The predict function allows you to get a prediction for a given user input. You can specify a list of options for the prediction to choose from, or use the default list of commands if no options are provided.

**Here's an example of how to use the predict function:**

```
options = ['help', 'exit', 'clear']
prediction, score = predict('h', options)
print(prediction) # 'help'
print(score) # 0.75
```

### Commands
The `is_command` function allows you to check if a user input matches a given command. You can specify a single command as a string, or a list of commands.

**Here's an example of how to use the `is_command` function:**

```
if is_command('exit'):
    print('Exiting program')

commands = ['help', 'exit', 'clear']
if is_command('c', commands):
    print('Clearing screen')
```

### Input
The input function allows you to get user input with a customizable prefix and postfix. You can also specify a list of commands for predictions, hide the cursor, and set a timer for the input.

**Here's an example of how to use the input function:**

```
prefix = '>> '
command = ['help', 'exit', 'clear']
inp = input(prefix, command)
print(inp)
```
For a full list of options and their default values, see the function definition at the top of this file.

### Additional functions
inline-input also includes several additional functions for working with the clipboard and console. These include:
```
get_clip(): gets the current clipboard text
clear_console(): clears the console
curVisible(isVisible=True): shows or hides the cursor|
```

The inline module is a tool that allows you to customize and enhance user input in your Python scripts. You can use it to add a prefix and postfix to your input, restrict the input to a certain length, hide the cursor, and more.

To use the inline module, you'll need to install it first. You can do this by running pip install inline. Then, you can import the input function from the inline module by adding import inline and input = inline.input to the top of your script.

### Here are some examples of how you can use the input function:

```
# Replace the default input function with inline.input
import inline
input = inline.input

# Get input with no prefix
inp = input(prefix=None) # defaults to ">> "

# Get input that is not free-form (user must choose from a list of options)
inp = input(free=False) # or free=True, default is True

# Get input with a minimum and maximum length
inp = input(minLength=2, maxLength=10) # by default minLength=0, maxLength=0

# Hide the cursor
inp = input(cursor=False) # show or hide cursor, True by default

# Hide the input and prediction text
inp = input(secret=True) # hide input and prediction text, False by default

# Set the cursor blink rate
inp = input(cursorVisibleTime=0.9, cursorNotVisibleTime=0.6) # cursor blink rate

# Set the time to display the tooltips
inp = input(timeInfo=5) # time to display the tooltips, the default is 2 seconds

# Turn off the timer for the tooltips
inp = input(timer=False) # setting of timer for the tooltips

# Set how many characters the user must type in order to be prompted for auto-completion
inp = input(iHelp=2) # how many characters the user must type in order to be prompted for auto-completion

# Set the initial text that will be entered for the user (the user can delete or edit it)
inp = input(inp="Initial text") # the text that will be entered for the user (the user can delete or edit it)
The inline module also includes several additional functions for working with the console. These include:

clear_console(lineDel=1): clears one or more lines from the console.
predict(text, list): predicts a similar word from the given list based on the input text.
isCommand(text, list): checks if the given text is a command in the given list.
```
















The simplest example:
```
import inline #Import inline module
input = inline.input #replace default input

while True:
    print("Say 'Yes' or 'No'")
    inp = input("Input: ", command=["Yes", "No"], free=False)
```

Commands options:
```
#1
import inline #Import inline module
input = inline.input #replace default input

inline.commands = ["Info", "Help", "Version"]

answer = input()
```
**OR:**
```
#2
import inline #Import inline module
input = inline.input #replace default input

commands = ["Info", "Help", "Version"]

answer = input(command=commands)
```

Autocomplete on Enter:
```
inline.autoCompleteOnEnter = True # Autocomplete on Enter and Tab, default False - only on Tab
inp = input(free=False) # Only your commands are allowed!
```

---
### Examples code:
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

### Another simple example:
```
import inline #Import inline module
input = inline.input #replace default input
commands = ["Exit"] #Default commands

while True:
    print("What kind of command do you want to create?")
    command = input(prefix="Name command: ")

    print("\nTry using your command!")
    if inline.isCommand(command, commands):
        inline.clear_console(lineDel=4) #delete last 4 lines
        print("Command already exists!")
        continue
    else:
        commands.append(command)
    inp = input(command=commands, free=False)

    print(f"\nGreat, {inp} is working!\n- What the command will print?")
    text = input("Enter text: ")

    print("\nTry using your command or write 'Exit'")
    inp = input(free=False, command=commands)
    if inp.lower() == commands[-1].lower(): # First try
        print(f"Printed: {text}")
    else:
        break

    print("\nDo you want to create another command?")
    inline.autoCompleteOnEnter = True
    inp = input(free=False, command=["Yes", "No"])
    inline.autoCompleteOnEnter = False
    if inline.isCommand(inp, "No"): #Best try
        print("Bye - bye!")
        break
```

_For more information and examples, see the function definitions and comments in the inline module source code._

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
inp = input(iHelp=2) # Tips for use Tab Autocomplete, default iHelp=3

# 
inline.autoCompleteOnEnter = True # Autocomplete on Enter and Tab, default False - only on Tab
inp = input(free=False) # Only your commands are allowed!

# Commands option 1:
inline.commands = ["Info", "Help", "Version", "Cls"]
inp = input() #Autocomplete with your commands on Tab

# Commands option 2:
inp = input(command=["Help", "Info", "Version"]) # or use inline.commands = ["Help", "Info", "Version"]
```

I'm not a programmer, my code is not pretty and intimidating : )

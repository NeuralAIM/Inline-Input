# Inline-Input
New input system for python

__Use:__

Commands option 1:
```
import inline

inline.commands = ["Help", "Info", "Quit", "Inline", "Magic"]
input = inline.input #replace default input

while True:
    inp = input()
    print(f"input: {inp}")
```
Commands option 2:
```
import inline

commands = ["Help", "Info", "Quit", "Inline", "Magic"]
input = inline.input #replace default input

while True:
    inp = input(command=commands)
    print(f"input: {inp}")
```
Strict answer choice:
```
import inline
inline.commands = ["Help", "Info", "Quit", "Inline", "Magic"]
input = inline.input #replace default input

while True:
    inp = input(free=False)
    print(f"input: {inp}")
```
![image](https://user-images.githubusercontent.com/75082388/162586479-77d2b8e6-458b-4700-97bc-109a6495c1f0.png)

Minimum input length:
```
import inline
inline.commands = ["Help", "Info", "Quit", "Inline", "Magic"]
input = inline.input #replace default input

while True:
    inp = input(minLength=5)
    print(f"input: {inp}")
```
![image](https://user-images.githubusercontent.com/75082388/162586647-f18bf23e-2337-484d-98b9-d535dcc09fe2.png)

Custom prefix:
```
import inline
inline.commands = ["Help", "Info", "Quit", "Inline", "Magic"]
input = inline.input #replace default input

while True:
    inp = input(prefix="Custom prefix: ")
    print(f"input: {inp}")
```
![image](https://user-images.githubusercontent.com/75082388/162586760-6f067103-47c0-4973-bd45-f172c0fb682e.png)

# Inline-Input
__Install library:__

```
pip install inline-input
```

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
    inp = input(minLength=5) #or input(maxLength=5)
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

Check for existence:
```
import inline
inline.commands = ["Help", "Info", "Quit", "Inline", "Magic"]
input = inline.input #replace default input

while True:
    inp = input()
    if inline.isCommand(inp): # or inline.isCommand(inp, command=commands)
        print(f"Inline command: {inp}")
    else:
        print(f"Unknown command: {inp}")
```

![image](https://user-images.githubusercontent.com/75082388/162587358-4ceb7ef3-00e8-4585-a7a4-8c03f7790345.png)

Prefiction commands:
```
import inline
inline.commands = ["Help", "Info", "Quit", "Inline", "Magic"]

prediction = inline.predict("In") # or inline.predict("In", command=commands)

print(f"Prediction Word: '{prediction[0]}'")
print(f"Prediction Score: {prediction[1]}%")
```
![image](https://user-images.githubusercontent.com/75082388/162587648-325c1ef6-b228-4d88-96e1-99336e46782e.png)

Default input with the same behavior:
```
import inline
input = inline.input #replace default input

while True:
    inp = input() #without commands
    print(f"Input: {inp}")
```
![image](https://user-images.githubusercontent.com/75082388/162589710-64051acd-b679-493e-abe8-6c71f8de6474.png)

Language definition:
```
import inline
inline.commands = ["English", "Русский"]
input = inline.input #replace default input

while True:
    inp = input(minLength=1)
    print(f"Input: {inp}")
    prediction = inline.predict(inp)[0]
    if prediction == "English":
        print(f"(EN) Prediction: {prediction}")
    elif prediction == "Русский":
        print(f"(РУ) Предсказывание: {prediction}")
```
![image](https://user-images.githubusercontent.com/75082388/162590144-c2cd96cb-c6f9-48c3-a804-828cbfb8b0e0.png)

Response Choices:
```
import inline
inline.commands = ["1 Games", "2 Films", "3 Other"]
input = inline.input #replace default input

while True:
    inp = input(minLength=1)
    print(f"Input: {inp}")
    prediction = inline.predict(inp)[0]
    print(f"Prediction: {prediction}")
```
![image](https://user-images.githubusercontent.com/75082388/162590336-738c766c-b8f2-4304-a783-d0ad4198a062.png)

Paste Clipboard:
```
import inline
inline.commands = ["Default text", "Pasted text"]
input = inline.input #replace default input

while True:
    inp = input()
    print(f"Input: {inp}")
```

![image](https://user-images.githubusercontent.com/75082388/162623834-90b78680-def6-46fa-a00a-ceb9cad65e2f.png)

Multiline autocomplete:
```
import inline
print("\n\n\n")
inline.commands = ["""Inline:.\n├───.input()\n│   └───prefix=">> "\n│       └───free=True"""]
input = inline.input #replace default input

while True:
    inp = input()
    print(f"Input: {inp}") #Press Ctrl+V
```

![image](https://user-images.githubusercontent.com/75082388/162626499-e3827a81-6747-4238-af2e-5f42b163288a.png)


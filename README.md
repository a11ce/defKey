# defKey

> Non-blocking keybinds using threads.

## Setup

- Download with `pip3 install defKey`
- Import with `import defKey`

## Usage

defKey allows the binding of keys to Python functions. When activated, defKey spawns a new thread which catches all keypresses (thus breaking `input()`) and, if they have been bound, spawns a new thread which executes the bound function. This is best for games and TUI programs. 

### Example

```
from defKey import defKey

def hello():
    print("hello")

def goodbye():
    print("goodbye")

def actualGoodbye():
    defKey.stop()
    
defKey.bind("h", hello)
defKey.bind("g", goodbye)
defKey.bind("q", actualGoodbye)

defKey.start()
```

You must call `defKey.stop()` before using `input()`. Binds will be retained and defKey can be restarted after.


---

All contributions are welcome by pull request or issue.

defKey is licensed under GNU General Public License v3.0. See [LICENSE](../master/LICENSE) for full text.
from thefuzz import process, utils
from colorama import Fore, init
import msvcrt as m
import ctypes
import ctypes.wintypes as w
from time import time
init(autoreset=True)
commands = None
autoCompleteOnEnter = False
CF_UNICODETEXT = 13
u32 = ctypes.WinDLL('user32')
k32 = ctypes.WinDLL('kernel32')
OpenClipboard = u32.OpenClipboard
OpenClipboard.argtypes = w.HWND,
OpenClipboard.restype = w.BOOL
GetClipboardData = u32.GetClipboardData
GetClipboardData.argtypes = w.UINT,
GetClipboardData.restype = w.HANDLE
GlobalLock = k32.GlobalLock
GlobalLock.argtypes = w.HGLOBAL,
GlobalLock.restype = w.LPVOID
GlobalUnlock = k32.GlobalUnlock
GlobalUnlock.argtypes = w.HGLOBAL,
GlobalUnlock.restype = w.BOOL
CloseClipboard = u32.CloseClipboard
CloseClipboard.argtypes = None
CloseClipboard.restype = w.BOOL

def predict(text, options=None):
    if options is None:
        options = commands
        return None, None

    if utils.full_process(text):
        pred, score = process.extractOne(text, options)
        return pred, score
    else:
        return None, None

def is_command(text, command=None):
    if command is None:
        command = commands
        return False

    if isinstance(command, str):
        command = [command]

    return text.lower() in [com.lower() for com in command]



def get_clip():
    try:
        OpenClipboard(None)
        h_clip_mem = GetClipboardData(CF_UNICODETEXT)
        text = ctypes.wstring_at(GlobalLock(h_clip_mem))
        GlobalUnlock(h_clip_mem)
        CloseClipboard()
        return text
    except:
        GlobalUnlock(h_clip_mem)
        CloseClipboard()
        return ""

def clear_console(pred=None, inp=None, lineDel=1):
    text = pred or inp or ''
    num_lines = len(text.split("\n"))
    if num_lines == 0:
        num_lines = 1
    print("\x1b[2K\r" + "\033[%d;A" % (num_lines), end="\r")


def curVisible(isVisible=True):
    if isVisible:
        print('\033[?25h', end="")
    else:
        print('\033[?25l', end="")


def input(prefix=">> ", command=None, free=True, cursor=True, timer=True, timeInfo=None, secret=False, inp='', minLength=0, maxLength=0, iHelp=3, cursorVisibleTime=0.9, cursorNotVisibleTime=0.6):
    if prefix is None:
        prefix = ""
    lastpred = ""
    print(prefix, end=f' \b')
    pred = ""
    postfix = ""
    curposx = 0
    #curposy = 0
    isprediction = True
    isCleared = False
    isSelected = False
    helptabi = 0
    s_time = time() - 0.1
    scur_time = time()

    if not cursor:
        curisVis = False
    else:
        curisVis = True
    curVisible(curisVis)
    
    if timeInfo is None:
        timeInfo = 2 * 10 #1 sec
    else:
        timeInfo = timeInfo * 10
    ipostfix = timeInfo

    if command is None:
        if commands is None:
            isprediction = False
        else:
            command = commands

    if minLength >= maxLength:
        if maxLength != 0:
            minLength = 0
            maxLength = 0

    while True:
        kbh = m.kbhit()
        if kbh or s_time + 0.1 < time():
            s_time = time()
            lentext = 0
            if kbh:
                if not cursor:
                    curisVis = False
                else:
                    curisVis = True
                    curVisible(curisVis)
                    scur_time = time()
                
                key = m.getwch()
                skey = key.encode('utf-8')
                postfix = ""
                ipostfix = timeInfo
                s_time = time() - 0.1
            elif cursor:
                if curisVis and scur_time + cursorVisibleTime < time():
                    curisVis = False
                    curVisible(curisVis)
                    scur_time = time()
                elif not curisVis and scur_time + cursorNotVisibleTime < time():
                    curisVis = True
                    curVisible(curisVis)
                    scur_time = time()

            if not kbh:
                if ipostfix > 0 and len(postfix) > 5:
                    if timer:
                        if postfix.endswith(f" ({(ipostfix+1) / 10}c)"):
                            postfix = postfix.replace(f" ({(ipostfix+1) / 10}c)", f" ({ipostfix / 10}c)")
                        else:
                            postfix += f" ({ipostfix / 10}c)"
                    ipostfix -= 1
                else:
                    postfix = ""

                key, skey = "", ""
            elif skey == b'\x01':
                if isSelected:
                    isSelected = False
                    postfix = "<W>Disable text select."
                elif len(inp) == 0:
                    postfix = "<F>No text to select."
                else:
                    isSelected = True
                    postfix = "All text selected."
            elif skey == b'\x16':
                cliptext = get_clip()
                if cliptext == "":
                    postfix = "<F>Clipboard is empty."
                elif len(cliptext.split("\n")) > 1:
                    inp += cliptext.split("\n")[0].replace("\r", "")
                    postfix = "<W>Only the first line was pasted."
                else:
                    inp += cliptext
                    postfix = "Text pasted!"
                
            elif skey == b'\xc3\xa0' and key == "à":
                key = m.getwch()
                if key == "K":
                    if not (curposx >= len(inp)):
                        curposx += 1
                    else:
                        postfix = "<F>The cursor is already left."
                elif key == "M":
                    if not (curposx <= 0):
                        curposx -= 1
                    else:
                        postfix = "<F>The cursor is already right."
                elif key == "H":
                    postfix =  "<F>Can't move the cursor up."
                elif key == "P":
                    postfix =  "<F>Can't move the cursor down."
                elif key == "R":
                    postfix = "<F>Use Ctrl + V to paste"
                elif key == "G":
                    if curposx < len(inp):
                        curposx = len(inp)
                        postfix = "Cursor moved to the home."
                    else:
                        postfix = "<F>The cursor is already left."
                elif key == "O":
                    if curposx > 0:
                        curposx = 0
                        postfix = "Cursor moved to the end."
                    else:
                        postfix = "<F>The cursor is already right."
                elif key == "I":
                    if curposx > 0:
                        curposx = 0
                        postfix = "Cursor moved to the end."
                    else:
                        postfix = "<F>The cursor is already right."
                elif key == "Q":
                    if curposx < len(inp):
                        curposx = len(inp)
                        postfix = "Cursor moved to the home."
                    else:
                        postfix = "<F>The cursor is already left."
                elif key == "S":
                        postfix = "<F>Use the backspace to delete."
                else:
                    postfix = "<F>Unknown key."

            elif skey == b'\x1b':
                postfix = "<F>You can't esc."
            elif skey == b"\x08":
                helptabi = 0
                if isSelected:
                    if len(inp) != 0:
                        inp = ""
                        postfix = "All text deleted!"
                    else:
                        postfix = "<F>You can't delete."
                else:
                    if curposx == 0:
                        if len(inp) != 0:
                            inp = inp[:-1]
                        else:
                            postfix = "<F>You can't delete."
                    else:
                        if len(inp[:-curposx]) != 0:
                            inp = inp[:-1-curposx] + inp[-curposx:]
                        else:
                            postfix = "<F>You can't delete."
            elif skey == b'\t':
                if pred != None:
                    inp = pred
                    postfix = "Autocompletion successful."
                else:
                    postfix = "<F>No suggestion for autocompletion."
            elif skey == b'\r':
                if minLength == 0 or len(inp) >= minLength:
                    if maxLength == 0 or len(inp) <= maxLength:
                        if free:
                            curVisible(True)
                            if isCleared:
                                clear_console(lastpred, inp)
                                print("\x1b[2K\r", end='\r')
                            else:
                                isCleared = True
                            return inp
                        else:
                            if is_command(inp, command=command):
                                curVisible(True)
                                if isCleared:
                                    clear_console(lastpred, inp)
                                    print("\x1b[2K\r", end='\r')
                                else:
                                    isCleared = True
                                if autoCompleteOnEnter:
                                    return pred
                                else:
                                    return inp
                            else:
                                postfix =  "<F>Doesn't match commands."
                    else:
                        postfix =  f"<F>Max length is {maxLength} characters."
                else:
                    postfix =  f"<F>Min length is {minLength} characters."
            elif len(key) == 1:
                if isSelected:
                    inp = ""
                if curposx == 0:
                    inp += key
                    if inp.lower() == lastpred[:len(inp)].lower():
                        if inp.lower() != lastpred.lower():
                            helptabi += 1
                            if helptabi >= iHelp:
                                postfix = "<W>Press Tab for Autocomplete!"
                        else:
                            helptabi = 0
                    else:
                        if helptabi >= iHelp:
                            postfix = "<W>Was I wrong?!"
                        helptabi = 0
                else:
                    inp = inp[:-curposx] + key + inp[-curposx:]
            else:
                postfix = "<F>Unknown key."

            if kbh and skey != b'\x01':
                isSelected = False
                
            print("\x1b[2K\r" + "\033[1;A")
            if isprediction:
                pred, score = predict(inp, command)
            else:
                pred = None

            postfixlen = len(postfix.replace("<F>", "").replace("<W>", ""))
            lentext += postfixlen
            if postfix.startswith("<F>"):
                colored_postfix = Fore.RED + postfix.replace("<F>", "")
            elif postfix.startswith("<W>"):
                colored_postfix = Fore.LIGHTYELLOW_EX + postfix.replace("<W>", "")
            else:
                colored_postfix = Fore.LIGHTGREEN_EX + postfix
            if pred != None:
                if isCleared:
                    clear_console(lastpred, inp)
                else:
                    isCleared = True

                isSimilar = pred[:len(inp)].lower() == inp.lower()
                if secret:
                    output = prefix + "*" * len(inp) + Fore.LIGHTBLACK_EX + "*" * len(pred[len(inp):])
                else:
                    output = prefix + inp + Fore.LIGHTBLACK_EX + pred[len(inp):]

                if len(pred) - len(inp) > 0:
                    lentext += len(pred) - len(inp)

                if score > 0:
                    if isSimilar:
                        print(output + f" ({score}%) " + colored_postfix, end='\b' * (lentext + len(f" ({score}%) ") + curposx))
                    else:
                        if len(pred.split("\n")) > 1:
                            if secret:
                                pred_ = "*" * len(pred.split("\n")[len(inp.split("\n"))-1].replace("\n", ""))
                            else:
                                pred_ = pred.split("\n")[len(inp.split("\n"))-1].replace("\n", "")
                            print(output + f"  [{pred_}] - ({score}%) " + colored_postfix, end='\b' * (lentext + len(f"  [{pred_}] - ({score}%) ") + curposx))
                        else:
                            if secret:
                                pred_ = "*" * len(pred)
                            else:
                                pred_ = pred
                            print(output + f"  [{pred_}] - ({score}%) " + colored_postfix, end='\b' * (lentext + len(f"  [{pred_}] - ({score}%) ") + curposx))
                else:
                    if isSimilar:
                        print(output + colored_postfix, end='\b' * lentext)
                    else:
                        if secret:
                            pred_ = "*" * len(pred)
                        else:
                            pred_ = pred
                        print(output + f"  [{pred_}] " + colored_postfix, end='\b' * (lentext + len(f"  [{pred_}] ") + curposx))
                lastpred = pred
            else:
                if isCleared:
                    clear_console(lastpred, inp)
                else:
                    isCleared = True
                lastpred = ""
                curposx = 0

                print("\x1b[2K\r", end='\r')

                if secret:
                    print(prefix + "*" * len(inp) + "  " + colored_postfix, end='\b' * (postfixlen + len("  ")))
                else:
                    print(prefix + inp + "  " + colored_postfix, end='\b' * (postfixlen + len("  ")))

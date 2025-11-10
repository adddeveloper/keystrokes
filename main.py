# requires: pip install pyautogui keyboard
import time
import pyautogui
import keyboard

def keystrokerfunc(args):
    """
    Usage example:
      keystrokerfunc(["keystrokes.txt", 5, 0.05, 2, True])
    args:
      args[0] -> path to keystrokes file
      args[1] -> delay before starting (seconds)
      args[2] -> delay between each character (seconds)
      args[3] -> how many spaces count as one tab
      args[4] -> stop typing when any keyboard input is detected (True/False)
    """
    if not (isinstance(args, (list, tuple)) and len(args) == 5):
        raise ValueError("Pass like: ['keystrokes.txt', delay_before, delay_between, tab_width, stop_when_keyboard]")

    filename, delay_before_start, delay_between_keys, tab_width, stopwhenkeyboard = args
    delay_before_start = float(delay_before_start)
    delay_between_keys = float(delay_between_keys)
    tab_width = int(tab_width)

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"Starting in {delay_before_start} seconds. Focus the window. \nPress 'c' to stop.")

    # Countdown before typing starts
    for sec in range(int(delay_before_start), 0, -1):
        if stopwhenkeyboard and keyboard.is_pressed('c'):
            print("\nStopped before start (keyboard input detected).")
            return
        print(f"{sec}...", end=" ", flush=True)
        time.sleep(1)

    print("\nSending keystrokes...")

    for line in lines:
        if stopwhenkeyboard and keyboard.is_pressed('c'):
            print("\nStopped (keyboard input detected).")
            return

        line = line.rstrip("\n")
        i = 0
        while i < len(line):
            if stopwhenkeyboard and keyboard.is_pressed('c'):
                print("\nStopped (keyboard input detected).")
                return

            if line[i] in (" ", "\t"):
                count = 1
                ch = line[i]
                while i + count < len(line) and line[i + count] == ch:
                    count += 1

                if ch == "\t":
                    # Real tabs -> one Tab key each
                    for _ in range(count):
                        pyautogui.press("tab")
                else:
                    # Spaces -> convert based on tab width
                    num_tabs = count // tab_width
                    remainder = count % tab_width
                    for _ in range(num_tabs):
                        pyautogui.press("tab")
                    if remainder > 0:
                        pyautogui.write(" " * remainder, interval=delay_between_keys)

                i += count
            else:
                pyautogui.write(line[i], interval=delay_between_keys)
                i += 1

        pyautogui.press("enter")

    print("Done.")


# SETTINGS
tabsrepresented = 4
stopwhenkeyboardisinuse = True
keystrokerfunc(["keystrokes.txt", 2, 0.001, tabsrepresented, stopwhenkeyboardisinuse])
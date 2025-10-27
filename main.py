# requires: pip install pyautogui
import time
import pyautogui

def keystrokerfunc(args):
    """
    Usage example:
      keystrokerfunc(["keystrokes.txt", 5, 0.05])
    args:
      args[0] -> path to keystrokes file (string)
      args[1] -> initial delay in seconds before starting (float or int)
      args[2] -> delay between each keystroke in seconds (float)
    """
    if not (isinstance(args, (list, tuple)) and len(args) == 3):
        raise ValueError("Pass a list like: ['keystrokes.txt', delay_before_start, delay_between_keys]")

    filename, delay_before_start, delay_between_keys = args

    try:
        delay_before_start = float(delay_before_start)
        delay_between_keys = float(delay_between_keys)
    except Exception as e:
        raise ValueError("Delays must be numbers (int/float).") from e

    # Read the keystrokes file
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")

    # Give user a short console countdown so they can focus the target window
    print(f"Starting in {delay_before_start} seconds. Focus the window you want to receive keystrokes.")
    try:
        for remaining in range(int(delay_before_start), 0, -1):
            print(f"{remaining}...", end=" ", flush=True)
            time.sleep(1)
        # Sleep any remaining fractional part
        frac = delay_before_start - int(delay_before_start)
        if frac > 0:
            time.sleep(frac)
    except KeyboardInterrupt:
        print("\nAborted before starting.")
        return

    print("\nSending keystrokes now... (press Ctrl-C to abort)")

    # Send keystrokes. pyautogui.write sends characters one-by-one using the provided interval.
    try:
        pyautogui.write(text, interval=delay_between_keys)
    except KeyboardInterrupt:
        print("\nAborted while sending.")
    except Exception as e:
        # pyautogui can raise if OS blocks synthetic input or if something else goes wrong
        raise RuntimeError("Failed to send keystrokes: " + str(e))

    print("Done.")

"""
Usage example:
    keystrokerfunc(["keystrokes.txt", 5, 0.05])
args:
    args[0] -> path to keystrokes file (string)
    args[1] -> initial delay in seconds before starting (float or int)
    args[2] -> delay between each keystroke in seconds (float)
"""
keystrokerfunc(["keystrokes.txt", 2, 0.05])
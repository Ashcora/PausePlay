import platform

import keyboard


def send_media_play_pause():
    """
    Simulates the media play/pause key press.
    Currently supported only on Windows.
    """
    os_name = platform.system()
    try:
        if os_name == "Windows":
            # Simulate media play/pause key press on Windows
            keyboard.press_and_release("play/pause media")
            print("Media play/pause command sent.")
        elif os_name == "Linux" or os_name == "Darwin":  # Darwin is macOS
            # Placeholder for future Linux/macOS support
            print(f"Media control on {os_name} is not implemented.")
        else:
            print(f"Unsupported operating system: {os_name}")
    except ImportError:
        print("The 'keyboard' module is required but not installed.")
        print("Please install the 'keyboard' module with: pip install keyboard")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to execute the media play/pause command.
    """
    # print("Starting the media control script...")
    send_media_play_pause()


if __name__ == "__main__":
    main()

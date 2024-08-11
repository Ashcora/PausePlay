import platform

import keyboard


def send_media_play_pause():
    """
    Simulates the media play/pause key press on Windows.
    """
    try:
        if platform.system() == "Windows":
            # Simulate media play/pause key press on Windows
            keyboard.press_and_release("play/pause media")
        else:
            print("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    send_media_play_pause()


if __name__ == "__main__":
    main()

# Python script specified for Windows to simulate media play/pause key without e.g. nircmd.exe

import platform

import keyboard


def send_media_play_pause():
    system = platform.system()
    if system == "Windows":
        # Simulate media play/pause key press on Windows
        keyboard.press_and_release("play/pause media")
    else:
        print("Unsupported operating system")


if __name__ == "__main__":
    send_media_play_pause()

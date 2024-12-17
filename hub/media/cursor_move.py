import pyautogui
import time

def move_cursor_and_return(offset_x, duration_hours):
    original_position = pyautogui.position()  # Get the original cursor position

    duration_minutes = duration_hours * 60
    for _ in range(duration_minutes):
        pyautogui.move(offset_x, 50)  # Move the cursor to the right (change offset_x as needed)
        time.sleep(20)  # Sleep for 60 seconds (1 minute)
        pyautogui.moveTo(original_position)  # Return to the original position

if __name__ == "__main__":
    cursor_offset_x = 10  # Change this value based on how much you want the cursor to move to the right
    duration_hours = 8  # Change this to the desired duration in hours
    move_cursor_and_return(cursor_offset_x, duration_hours)

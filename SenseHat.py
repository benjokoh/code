from sense_hat import SenseHat

# Initialize Sense HAT
sense = SenseHat()

# Define a color (red in this case)
color = (255, 0, 0)  # RGB values for red

# Set all pixels to the defined color
sense.clear(color)

# Keep the light on for 5 seconds
import time
time.sleep(5)

# Clear the display
sense.clear()
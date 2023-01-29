from PIL import ImageGrab

# Take a screenshot of the chat window
im = ImageGrab.grab(bbox=(100, 100, 500, 500))

# Save the image as chat.png
im.save('chat.png')

import pyautogui

# Set the phone number of the recipient
phone_number = '9013366855'

# Set the message you want to send
message = 'Hello, this is a message sent using pyautogui and Python'

# Open WhatsApp Web
pyautogui.hotkey('win', 'r')
pyautogui.typewrite('https://web.whatsapp.com/')
pyautogui.press('enter')

# Wait for the page to load
pyautogui.sleep(5)

# Find the search bar and enter the phone number
search_bar = pyautogui.locateOnScreen('search_bar.png')
pyautogui.click(search_bar)
pyautogui.typewrite(9013366855)

# Select the chat
chat = pyautogui.locateOnScreen('chat.png')
pyautogui.click(chat)

# Find the message input field and send the message
message_input = pyautogui.locateOnScreen('message_input.png')
pyautogui.click(message_input)
pyautogui.typewrite(message)
pyautogui.press('enter')

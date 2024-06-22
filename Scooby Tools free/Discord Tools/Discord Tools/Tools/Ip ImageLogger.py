import webbrowser


url1 = "https://youtu.be/ePS25bNWNeI"
url2 = "https://grabify.link"


while True:
    response = input("This will take you to the site and tutorial for the image logger are you sure you want to procced (Y/N)").lower()
    if response == 'y':
        break
    elif response == 'n':
        print("Exiting script...")
        exit()
    else:
        print("Invalid response. Please enter 'Y' or 'N'.")


webbrowser.open_new_tab(url1)
webbrowser.open_new_tab(url2)



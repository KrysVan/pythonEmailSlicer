def email_slicer():
    while True:
        text = input("Enter an email to slice:> ")

        if text.count("@") == 1 and len(text[:text.index("@")]) > 0 and len(text[text.index("@") + 1:]) > 3:
            user = text[:text.index("@")]
            domain = text[text.index("@")+1:]
            print("Your username is: " + user)
            print("Your domain is: " + domain)
        else:
            print("Invalid email address!!")
        if input("Continue or stop (c/s): > ") == "s":
            break
if __name__ == '__main__':
    email_slicer()

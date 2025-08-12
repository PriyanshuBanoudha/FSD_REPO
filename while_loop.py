cor_password = "python123"
while True:
    password = input("Enter the password: ")
    if password == cor_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password.")

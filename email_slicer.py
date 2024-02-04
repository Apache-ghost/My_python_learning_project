def main():
    print("welcome to email slicer!")
    print("")

    email_input=input("Enter your email address: ")
    (user_name,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")
    print("user_name: ",user_name)
    print("domain: ",domain)
    print("extension: ",extension)
while True:
    main()
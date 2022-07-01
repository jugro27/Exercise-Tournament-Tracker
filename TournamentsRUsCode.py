def startUp():
    print("Welcome to Tournaments R Us")
    print("============================")
    global numSlots
    numSlots = int(input("Enter the number of participants: "))
    print(f"There are {numSlots} participant slots ready for sign-ups.")
    goToMM = str(input("Enter 'M' to go to the main menu: "))
    if goToMM == "M":
        mainMenu()

def mainMenu():
    print("Participant Menu")
    print("================")
    print("1. Sign up")
    print("2. Cancel Sign Up")
    print("3. View Participants")
    print("4. Save Changes")
    print("5. Exit")
    mmChoice = int(input("Please enter the number of the menu you'd like to go to: "))
    if mmChoice == 1:
        signUp()
    if mmChoice == 2:
        cancelSignUp()
    if mmChoice == 3:
        viewParticipants()
    if mmChoice == 4:
        saveChanges()
    if mmChoice == 5:
        exit()

def signUp():
    print("Participant Sign Up")
    print("====================")
    global participantName
    participantName = str(input("Participant Name: "))
    names = []
    names.append(participantName)
    global desStartSlot
    slots = []
    desStartSlot = int(input(f"Desired starting slot #[1-{numSlots}]: "))
    if desStartSlot in slots:
        print(f"Error: Slot #{desStartSlot} is filled. Please choose another slot: ")
    else:
        slots.append(desStartSlot)
        print(f"Success: {participantName} is signed up for starting slot #{desStartSlot}")
    global namesAndSlots
    namesAndSlots = []
    for n in range (0, len(slots)):
        print(n)
        print(names)
        print(slots)
        namesAndSlots.append(names[n] + str(slots[n]))
    print(namesAndSlots)
    goToMM = str(input("Enter 'M' to go to the main menu: "))
    if goToMM == "M":
        mainMenu()

def cancelSignUp():
    print("Participant Cancellation")
    print("========================")
    cancelNameSlot = input("Participant name and starting slot [ex: John1]: ")
    for cancelNameSlot in namesAndSlots:
        if cancelNameSlot in namesAndSlots:
            namesAndSlots.remove(cancelNameSlot)
            print(f"Success: {cancelNameSlot} has been cancelled.")
            goToMM = str(input("Enter 'M' to go to the main menu: "))
            if goToMM == "M":
                mainMenu()
        else:
            print("Error: Those credentials did not match our records, please try another input.")
            cancelSignUp()

def viewParticipants():
    print("View Participants")
    print("=================")
    viewNameSlot = input("Participant name and starting slot [ex: John1]: ")
    for viewSlot in namesAndSlots:
        if viewSlot in namesAndSlots:
            print(namesAndSlots)
            goToMM = str(input("Enter 'M' to go to the main menu: "))
            if goToMM == "M":
                mainMenu()
        else:
            print("There is not a participant on that slot, please try again.")
            viewParticipants()

def saveChanges():
    print("Save Changes")
    print("============")
    global wantSave
    wantSave = str(input("Save your changes to CSV? [Y/N]: "))
    if wantSave == "Y":
        file = open("TournamentParticipants.csv", "w")
        for line in namesAndSlots:
            file.writelines(namesAndSlots)
            print("Your changes have been saved.")
            file.close()
            mainMenu()
    elif wantSave == "N":
        mainMenu()

def exit():
    print("Any unsaved changes will be lost.")
    wantExit = str(input("Are you sure you want to exit? [Y/N]: " ))
    if wantExit == "Y":
        exit
    elif wantExit == "N":
        mainMenu()

startUp()
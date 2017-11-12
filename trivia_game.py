def Trivia():

    #Opens the CSV file and stores it in the array myFile
    myFile = open("trivia.csv","r")

    #Reads the lines of the CSV file into the variable players
    players = myFile.readlines()

    #Initializes Question Number and Score
    question_number = 1
    score = 0

    print("Welcome to the greatest Trivia Show on Earth!")
    print("There are 20 questions total, but you may stop playing the game at any time.")

    #Loops through each question
    for p in players:

        #Splits each cell of the CSV file into its parts
        data = p.split(",")

        #Places question and answers into variables
        questions = data[0]
        answera = data[1]
        answerb = data[2]
        answerc = data[3]
        answerd = data[4]
        correct_answer = data[5]
        correct_answer = int(correct_answer)

        #Prints the question and the 4 answers
        print("")
        print("Question #",question_number)
        print(questions)
        print(answera)
        print(answerb)
        print(answerc)
        print(answerd)
        print("")

        #Asks the user for their answer
        answer = input("Answer: ")
        answer = int(answer)
        print("")

        #Checks if the answer is correct and prints appropriate responses
        if correct_answer == answer:
            score = score + 1
            print("That is the correct answer")
            print("Your current score is", score)
            print("")
            question_number = question_number + 1

        else:
            print("That is not the correct answer")
            print("Your current score is", score)
            print("")
            question_number = question_number + 1

        print("Would you like to continue playing the game? ")
        response = input("Y for yes, N for no: ")
        if response == 'N':
            break

    print("")
    print("Thank you for playing the greatest Trivia Game on Earth!")

Trivia()
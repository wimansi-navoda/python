#trivia Game

#list of Question
question = [
    "What is the capital of France",
    "What is 5+7?",
    "Which  of the following is a programming language? ",
    "What the colour do you get whten you mix red and white"
]

#list of options for each quetion
options = [
    ["1 . London", "2. berline", "3. parise", "4. marid" ],
    ["1 . 10", "2. 11", "3. 12", "4. 13" ],
    ["1 . python", "2. snake", "3. apple", "4. car" ],
    ["1 . pink", "2. purple", "3. orange", "4. green" ]
]

#list of correct answer
correct_answer = [3, 3, 1, 1]# paris, 12, python, pink
#start of the game
play_again = "yes"
while play_again == "yes":
    score = 0
    print ( "--- Welcome to the trivia game---")
    print ("Answer the following Question by entering the number corresponding to your choice.")

    #initialize index
    index = 0

    #number_of_Questions
    number_of_Questions = 4

    #loop 
    while index < number_of_Questions:
        print ("Question" + str (index + 1) + ":" + question[index])
        #display
        for option in options[index]:
            print(option)

        #get user input
        answer = int(input("Enter the number of your answer"))

        #check if answer is correct
        if answer == "correct_answers"[index]:
            print("correct")
            score = score + 1

        else:
            print("incorrect")

        #move to next qestion
        index = index + 1


        #disply the final score
        print ("trivia completed")
        print("your score: "+ str(score) + " out of " + str(number_of_Questions))

        #ask 
        play_again = input("Do you want to play again ?(yes/no): ")
        if play_again != "yes":
            print("Thank you for playing Goodbye")




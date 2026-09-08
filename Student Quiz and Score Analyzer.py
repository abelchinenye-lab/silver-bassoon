## Student Quiz & Score Analyzer

quiz = {
    "How many states are there in Nigeria?": "36",
    "What is the capital of Nigeria?": "Abuja",
    "Is Nigeria a country or a continent?": "Country",
    "Do we have teachers in schools?": "Yes",
    "Is the weather condition in Nigeria favorable?": "No"
}
while True:
 
## Ask for the student's name
 name = input("Enter your Full Name: ")
 score = 0
 wrong_answers = []

## For Loop
 for question, correct_answer in quiz.items():
     print("\n" + question)
     user_answer = input("Input your answer: ")

## Check the answer
     if user_answer.lower() == correct_answer.lower():
         print("It is correct!")
         score += 1 
     else: 
         print("It is wrong!")
         print("correct answer:", correct_answer )
 wrong_answers.append(question)


## Calculate the percentage        
 percentage = (score / len(quiz)) * 100

## Determine the performance
 if percentage >= 80:
     result = "Excellent"
 elif percentage >= 60:
     result = "Good"
 elif percentage >= 50:
     result = "Fair"
 else:
     result = "Study Harder"

## Display the results
 print("\nStudent:", name)
 print("Quiz finished!")
 print("Your score is:", score, "/", len(quiz))
 print("percentage:", percentage, "%")
 print("Performance:", result)

## Ask whether to continue
 again = input("Would you like to take the quiz again? (yes/no):")
 if again.lower() != "yes":
     print("Quiz system closed.")
     break
    


#Grades.py
#This program outputs grades on a scale from 1F-5A.


def main():
    scores = 'FFDCBA'
    tests_scores = eval(input("Enter the points scored on the test: "))
    print("The letter grade for your score was a " + scores[tests_scores] +".")

main()
    

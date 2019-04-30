# Grading System Mission

scores = [] #make a list for the scores

sum = 0 #Initialize the sum

for count in range(1,6):
    print ('Please enter test score # ',count, '(value should be between 0 and 20)' ) #Prompt user to enter score 1, 2,...5
    score = input ()
    scores.append(score) #store the scores in a list to print a summary
    sum = sum + float(score) #add the scores together converting input to a float
    

print ('Your scores are: ',scores)
print ('The sum of your scores is ', sum)

if sum >= 85:  # Predict the grade based on these 5 scores
    grade = 'A'
elif sum >= 75:
    grade = 'B'
elif sum >= 65:
    grade = 'C'
elif sum >= 50:
    grade = 'D'
else:
    grade = 'F'

print ('Your grade is estimated to be: ',grade)






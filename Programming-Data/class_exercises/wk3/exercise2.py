# Exercise 2:
#
# Show the grade of a student based on the subject's mark
# if mark < 50 student grade is fail
# if mark between 50 and 60 student grade is pass
# if mark between 60 and 80 student grade is credit
# if mark >= 80 student grade is distinction

while True:

    mark = float(input("enter subject mark: "))

    if mark < 50:
        grade = "fail"
    elif 50 <= mark < 60:
        grade = "pass"
    elif 60 <= mark < 80:
        grade = "credit"
    elif mark  >= 80:
        grade = "distinction"
    else:
        print("grade is unknown")

    print("Grade is: ", grade)
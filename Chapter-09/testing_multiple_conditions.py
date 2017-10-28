score = int(input("Enter your marks: "))

if score >= 90:
    print("Excellent ! Your grade is A")
else:
    if score >= 80:
        print("Great ! Your grade is B")
    else:
        if score >= 70:
            print("Good ! Your grade is C")
        else:
            if score >= 60:
                print("Your grade is D. You should work hard on you subjects.")
            else:
                print("You failed in the exam")
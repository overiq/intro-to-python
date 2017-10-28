gre_score = int(input("Enter your GRE score: "))
per_grad = int(input("Enter percent secured in graduation: "))

if per_grad > 70:
    if gre_score > 150:
        print("Congratulations you are eligible for loan.")
    else:
        print("Your GRE score is no good enough. You should retake the exam.")
else:
    print("Sorry, you are not eligible for loan.")
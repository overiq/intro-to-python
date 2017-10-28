gre_score = int(input("Enter your GRE score: "))
per_grad = int(input("Enter percent secured in graduation: "))

if per_grad > 70:
    # outer if block
    if gre_score > 150:
        # inner if block
        print("Congratulations you are eligible for loan")
else:
    print("Sorry, you are not eligible for loan")
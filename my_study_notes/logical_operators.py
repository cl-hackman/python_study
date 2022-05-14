good_credit_score = True
bad_credit_score = False
student = False
entrepreneur = True
message = "eligible" if good_credit_score and student else "not eligible"
print(message)
message_2 = "eligible" if good_credit_score or bad_credit_score else "not eligble"
print(message_2)
if not student:
    print("eligible")
if (good_credit_score or bad_credit_score) and entrepreneur:
    print("loan not approved")
# USE LOGICAL OPERATORS IN IF STATEMENTS FOR SHORTER CODE: see fizzbuzz_function.py
# and, or, not are logical operators used for more complex conditions
# and condition works when booleans are same
# or condition works when one boolean is opposite the other
# not condition works by running the opposite of the boolean value

# You are given the follow variables. Notice how e and f are booleans:

a = 10
b = 20
c = 30
d = 20

e = True
f = False

# The following code will take in the "test_variable_1" and "test_variable_2" and do a conditional test to see if both of the values are equal or not.

test_variable_1 = a
test_variable_2 = b

if test_variable_1 == test_variable_2:
    print("The values match!")
else:
    print("The values do not match!")

# 1. Using the same test_variable_1 and test_variable_2, create a new conditional that checks if either value is greater than 25. If it is, than print out "One of the values is greater than 25". Otherwise, print "Neither of the Values are greater than 25". You will need an Or statement.


# 2. Now, create another conditional that checks weather or not both items are divisible by 20. A positive statement should only be printed if BOTH values satify the condition. You will need an And statement


# 3. Next, create a conditional that first checks if at least one of the values is less than 15 or greater than 25. If this rings true, then print the statement "At least one of the test variables satisfies the condition." After that first check, the code should then perform a second check using an Elif statement, checking if at least one of the variables equals 20. If this is true, then print "At least one of the variables equals 20." Lastly, end it all with a final Else statement that prints "No conditions were met"


# 4. Lastly, end it with a conditional that takes a new test variable, test_variable_3. This variable will equal either e or f.

test_variable_3 = e

# Write out a conditional that simply takes test_variable_3, and prints "The variable is true" or "The variable is false", depending on the boolean. This is simply to show that if statements in python can take just a boolean variable and still function.


# Once that's complete, set test_variable_1 = 24 and test_variable_2 = 26. Rerun the code from section 3 and copy the printed statement into the quiz.
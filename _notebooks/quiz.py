import getpass, sys
def question_and_answer(prompt):
    print("Question:" +prompt)
    msg = input()
    print("Answer:" +msg)

def question_with_response(prompt):
    print("Question: " + prompt)
    msg = input()
    return msg

questions = 5
correct = 0

print('Hello, ' + getpass.getuser() + " running " + sys.executable)
print("You will be asked " + str(questions) + " questions.")
question_and_answer("Are you ready to take a test?")

rsp = question_with_response("What command is used to include other functions that were previously developed?")
if rsp == "import":
    print(rsp + " is correct! Yay!")
    correct += 1
else:
    print(rsp + " is incorrect! Sorry!")

rsp = question_with_response("What command is used to evaluate correct or incorrect response in this example?")
if rsp == "if":
    print(rsp + " is correct! Yay!")
    correct += 1
else:
    print(rsp + " is incorrect! Sorry!")

rsp = question_with_response("Each 'if' command contains an '_________' to determine a true or false condition?")
if rsp == "expression":
    print(rsp + " is correct! Yay!")
    correct += 1
else:
    print(rsp + " is incorrect! Sorry!")

rsp = question_with_response("What is the term used to describe a set of two or more lines of code?")
if rsp == "sequence":
    print(rsp + " is correct! Yay!")
    correct +=1
else:
    print(rsp + " is incorrect! Sorry!")

rsp = question_with_response("What is a key word used in Python to describe a function?")
if rsp == "def":
    print(rsp + " is correct! Yay!")
    correct +=1
else:
    print(rsp + " is incorrect! Sorry!")

rsp = question_with_response("What is the name of the library that we are importing this function from?")
if rsp == "os":
    print(rsp + " is correct! Yay!")
    correct +=1
else:
    print(rsp + " is incorrect! Sorry!")



print(getpass.getuser() + " you scored " + str(correct) +"/" + str(questions))
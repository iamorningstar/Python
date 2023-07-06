# It was a challenging question to create a logic or a program to predict at what age you should drive

# --------------------
#  text scripting
# --------------------

introduction = "I'm a question answer logic program"
nameask = "Please Inter your name"
ageask = "Please inter your age"
pointer = "Hi there"
emotion = "Hay"
statment1 = "Your age is"
statment2 = "lower then"
statment3 = "above"
statment4 = "Answer quality"
statment5 = "And"
statment6 = "Not"
statment7 = "Greater then"
statment8 = "Equal then"
anser1 = "!Congratulation you cane also Drive."
anser2 = "You can't Drive. Because your age is lower then 18"
anser3 = "We are not able to find correct information about your age come to our office and check physically."
anser4 = "Oops, you gave wrong information"
anser5 = "You are too young to think about these things now"
anser6 = " You say your age is above 100 ,I have no idea about this sir"
qulaty1 = "Good"
qulaty2 = "Very Good"
qulaty3 = "Bad"
qulaty4 = "Vary Bad"
qulaty5 = "Medum"
qulaty6 = "Poor"


# --------------------
#  numeric scripting
# --------------------

maximumlowerthen = 1
minimum = 7
equalise = 18
maximumupperthen = 100

# --------------------
#  logic
# --------------------

print(pointer)
print(introduction)
print(nameask)
nametake = input()
print(ageask)
agetake = input()
converter = int(agetake)

# --------------------
#  if else statement rag
# --------------------

if converter > maximumlowerthen and converter < minimum :
    print(emotion,nametake,statment1,agetake,statment5,statment2,minimum,statment5,statment3,maximumlowerthen)
    # print(nametake)
    # print(statment1)
    # print(agetake)
    # print(statment5)
    # print(statment2)
    # print(minimum)
    # print(statment5)
    # print(statment3)
    # print(maximumlowerthen)
    # print("anes1")
    print(qulaty3)
    print(anser5)
    print(anser2)
elif converter > minimum and converter < equalise :
    print(emotion)
    print(nametake)
    print(statment1)
    print(agetake)
    print(statment5)
    print(statment2)
    print(maximumupperthen)
    print(statment5)
    print(statment3)
    print(maximumlowerthen)
    print(",")
    print(minimum)
    print("anes1")
    print(qulaty1)
    print(anser2)
elif converter > equalise and converter < maximumupperthen :
    print(emotion)
    print(nametake)
    print(statment1)
    print(agetake)
    print(statment5)
    print(statment2)
    print(maximumupperthen)
    print(statment5)
    print(statment3)
    print(maximumlowerthen)
    print(",")
    print(minimum)
    print(",")
    print(equalise)
    print("anes1")
    print(qulaty2)
    print(anser1)
elif converter == maximumlowerthen :
    print(emotion)
    print(nametake)
    print(statment1)
    print(agetake)
    print(statment5)
    print(statment8)
    print(maximumlowerthen)
    print("anes1")
    print(qulaty6)
    print(anser4)
    print(anser2)
elif converter == maximumupperthen :
    print(emotion)
    print(nametake)
    print(statment1)
    print(agetake)
    print(statment5)
    print(statment8)
    print(maximumupperthen)
    print("anes1")
    print(qulaty6)
    print(anser4)
    print(anser1)
elif converter == minimum :
    print(emotion)
    print(nametake)
    print(statment1)
    print(agetake)
    print(statment5)
    print(statment8)
    print(minimum)
    print("anes1")
    print(qulaty6)
    print(anser4)
    print(anser2)
elif converter == equalise :
    print(emotion)
    print(nametake)
    print(statment1)
    print(agetake)
    print(statment5)
    print(statment8)
    print(equalise)
    print("anes1")
    print(qulaty6)
    print(anser3)















# elif converter > maximumupperthen and converter < maximumlowerthen:
#     print(emotion)
#     print(statment1)
#     print(agetake)
#     print(statment5)
#     print(statment7)
#     print(maximumupperthen)
#     print(statment5)
#     print(statment3)
#     print(maximumlowerthen)
#     print("anes3")
# elif converter < maximumupperthen and converter < maximumlowerthen:
#     print(emotion)
#     print(statment1)
#     print(agetake)
#     print(statment5)
#     print(statment2)
#     print(maximumupperthen)
#     print(statment5)
#     print(statment3)
#     print(maximumlowerthen)
#     print("anes4")
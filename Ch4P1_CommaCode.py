def commacode(input_list):
    if len(input_list)==0:
        print ("")
    elif len(input_list)==1:
        print (str(input_list[0]))
    else:
        print (", ".join(input_list[:-1]) + ", and " + str(input_list[-1]))

spam = ["good morning","good afternoon", "good night"]
commacode(spam)

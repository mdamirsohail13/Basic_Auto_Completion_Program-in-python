dct=[]
flag = "yes"
while flag=="yes":
    s = input("Enter the substring :")
    output = ""
    if len(dct)==0:
        print("No Suggestion.")
    else:
        for w in dct:
            if s in w:
                output += (w+"\n")
        if output=="" :
            print("No Suggestion.")
        else:
            print("Suggestions are :-")
            print(output)

    print("Do you want to add your word in dictionary : (yes/no) ?")
    st = input()
    if st=="yes":
        dct.append(s)

    print("Try Again : (yes/no) ?")
    flag = input().strip()
    print("========================================================")

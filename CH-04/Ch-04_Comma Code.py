def list_comma(list):
    com=''
    for i in range(len(spam)-1):
        com=com+str(spam[i])+','
    com=com+'and'+' '+str(spam[len(spam)-1])
    print(com)
spam=['apples','bananas','tofu','cats']
list_comma(spam)
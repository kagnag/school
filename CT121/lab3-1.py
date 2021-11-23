import re
f = open('1.txt', 'r')
line = f.readlines()

for inp in line:
    # cau 1
    if(re.match("t|h", inp, re.IGNORECASE) and re.findall(r're+', inp)):

    # cau 2
    # if(re.findall(r'\A[a-zA-Z0-9.+-?! ]{20,}\b', inp)):
    #     print(inp, len(inp))

    # cau 3
    # if(re.findall(r'(\?\!)$', inp)):

    # cau 4 
    # if(re.findall(r'a+', inp) and re.findall(r'r+', inp) and re.findall(r's+', inp)
    #     and re.findall(r'm+', inp) and re.findall(r'l+', inp)):

    # cau 5
    # if(not(re.findall(r'[.,]', inp))):
          
    # cau 6
    # if(re.findall(r'mouse', inp)):

    # cau 7
    # if(re.findall(r'ba*', inp)):

    # cau 8
    # if(re.findall(r'\A[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Z|a-z]+\b', inp)):
    #     inp = inp.split('@')[1]

    # cau 9
    # if(re.findall(r'<head>', inp)):
    #     inp = re.sub(r'(<head>)|(</head>)', '', inp)

        print(inp)
f.close
import re

str = input().split(" ")

for inp in str:
    # cau 1
    if(re.findall(r'([a-z])', inp) and re.findall(r'[0-9]', inp)):

    # cau 2
    # if(re.findall(r'ab*', inp)):

    # cau 3
    # if(re.findall(r'(\Aa).(b)$', inp)):

    # cau 4
    # if(re.findall(r'[a-z]', inp)) and re.findall(r'_', inp):

    # cau 5 -
    # if(re.findall(r'\A[a-zA-Z0-9]{5,5}\b', inp)):

    # cau 6
    # if(re.findall(r'h+', inp)):

    # cau 7
    # if( re.findall(r'\A[0-9]', inp)):

    # cau 8
    # if(re.findall(r'_', inp)):
    #     inp = re.sub(r'_', " ", inp)

    # cau 9 - mm-dd-yy -> dd-mm-yy
    # if(re.findall(r'\A[0-9][0-9]-[0-9][0-9]-[0-9][0-9]\b', inp)):

        print(inp)
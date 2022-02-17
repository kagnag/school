import collections

# bai 1
def bai1(s1, s2):
    str1 = s1.replace(s1[0:2], s2[0:2])
    str2 = s2.replace(s2[0:2], s1[0:2])
    result = str1 + " " + str2
    return result
# a = input()       
# b = input()
# print("chuoi moi sinh ra tu 2 chuoi sau khi doi 2 ky tu dau\n", bai1(a, b))

# bai 2 
def del_idx_even(s):
    result = ""
    for i in range(len(s)):
        if i % 2:
            result += s[i]
    return result

# a = input()   
#print(del_idx_even(a))

# bai 3
def num_word(s):
    result = s.split(" ")
    return dict((i, result.count(i)) for i in result)

# a = input()   
# print(num_word(a))

# bai 4
def mahoa(s):
    result = ""
    n = 3
    for i in range(len(s)):
        char = s[i]
        if "A" <= char <= "Z":
            result = result + chr((ord(char) - n - 65) % 26 + 65)
        elif "a" <= char <= "z":
            result = result + chr((ord(char) - n - 97) % 26 + 97)
        else:
            result += char
    return result

# a = input()   
# print(mahoa(a))

# bai 5
def chuoi_hople(str1, str2):
    s1 = list(str1)
    s2 = list(str2)
    for i in s2:
        if i not in s1:
            return print("Chuoi khong chop le")
    return print("chuoi hop le")
    
# print("Nhap bo chu cai nhap")
# a1 = input()
# print("Nhap chuoi can kiem tra")
# a2 = input()
# chuoi_hople(a1, a2)

# bai 6
def change_string_list(s):
    result = s.split(" ")
    return result

# a = input()   
# print(change_string_list(a))

# bai 7
def khong_lap_1st(s):
    result = collections.Counter(s)
    for i in s:
        if result[i] == 1:
            return i

# a = input()   
# print(khong_lap_1st(a))

# bai 8
def xoa_khoang_trang(s):
    result = s.replace(" ", "")
    return result

# a = input()   
# print(xoa_khoang_trang(a))

# bai 9
def lap_1st(s):
    result = s.split(" ")
    tmp = set()
    for i in result:
        if i in tmp:
            return i
        else:
            tmp.add(i)
    return 'None'

# a = input()   
# print(lap_1st(a))

# bai 10
def max_length_0(s):
    count = 0
    max_c = 0
    for i in range(len(s)):
        if s[i] == '0':
            count += 1
        elif s[i] == '1':
            max_c = max(max_c, count)
            count = 0
    return max(max_c, count)

# a = input()   
# print(max_length_0(a))

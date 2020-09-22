import sys
import pprint

case_num = int(input())

lst_case = list()

for i in range(0, case_num):
    lst_case.append([])

    str1 = sys.stdin.readline().rstrip()
    str2 = sys.stdin.readline().rstrip()

    lst_case[i].append(str1)
    lst_case[i].append(str2)

#pprint.pprint(lst_case)


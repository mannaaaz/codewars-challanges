#Task
#Given a string s. You have to return another string such that even-indexed and odd-indexed characters of s are grouped and groups are space-separated (see sample below)

#Note: 
#0 is considered to be an even index. 
#All input strings are valid with no spaces
#input: 'CodeWars'
#output 'CdWr oeas'

#Even indices 0, 2, 4, 6, so we have 'CdWr' as the first group
#odd ones are 1, 3, 5, 7, so the second group is 'oeas'
#And the final string to return is 'Cdwr oeas'


#Solution

def sort_my_string(s):
        evenList, oddList = [], []
        for i, char in enumerate(s):
            if i % 2 == 0:
                evenList.append(char)
            elif i % 2 == 1:
                oddList.append(char)
        return "".join(evenList) + " " + "".join(oddList)

sort_my_string('CodeWars')

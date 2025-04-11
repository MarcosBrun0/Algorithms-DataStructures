
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if len(str1)>len(str2):
            shortString = str2
            longString = str1
        else:
            shortString = str1
            longString = str2        
        for i in range(len(shortString),0,-1):
            prefix = shortString[:i]
            concatenation = ""
            gcdOfShort = False
            while len(concatenation) < len(longString):
                concatenation += prefix
                if concatenation == shortString:
                    gcdOfShort = True
                if concatenation == longString and gcdOfShort == True:
                    return prefix

# Apos resolver encontrei essa forma que é bem especifica do python, a ideia é que é possivel multiplicar strings, e o // é uma divisão que só aceita resultado inteiro
# if prefix * (len(shortString) // len(prefix)) == shortString and \
#    prefix * (len(longString) // len(prefix)) == longString:
#     return prefix

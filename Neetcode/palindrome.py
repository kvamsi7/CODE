# def breakPalindrome(palindromeStr):
#     combinations_list = []
#     for ind in range(0,len(palindromeStr)):
#         let_ord = ord(palindromeStr[ind])-1
#         mod_palind = ""
#         while(let_ord > 96):
#             if(let_ord == 97):
#                 mod_palind = palindromeStr[:ind] + "a" + palindromeStr[ind+1:]
#             else:
#                 mod_palind = palindromeStr[:ind] + chr(let_ord) + palindromeStr[ind+1:]
#             let_ord = let_ord - 1
#             combinations_list.append(mod_palind)
#     combinations_list.sort()
    
#     if len(combinations_list) > 0:
#         return combinations_list[0]
#     else:
#         return "IMPOSSIBLE"

def breakPalindrome(palindromeStr):
    mid = len(palindromeStr)//2
    for i in range(0,mid):
        if palindromeStr[i] != 'a':
            return palindromeStr[:i] +'a'+palindromeStr[i+1:]
    return "IMPOSSIBLE"

if __name__ == "__main__":
    s = input()
    print(breakPalindrome(s))
def loSs(s):
            longest=''
            res=0
            list=[]
            for start in range(len(s)):
                longest=''
                for i in range(start,len(s)):
                    if s[i] in longest:
                        list.append(longest)
                        longest=s[i]
                    else:
                        res=max(res,i-start+1)
                list.append(longest)
            print("hamid")    
            # return(len(max(list,key=len))) 


def lengthOfLongestSubstring(s):
    n = len(s)
    longest_len = 0
    start = 0
    char_index_map = {}
    
    for end in range(n):
        if s[end] in char_index_map:
            # If the character is already present in the current substring,
            # update the start pointer to the next position after the last occurrence of the character
            start = max(start, char_index_map[s[end]] + 1)
        
        # Update the index of the current character in the map
        char_index_map[s[end]] = end
        
        # Update the length of the longest substring
        longest_len = max(longest_len, end - start + 1)
    
    return longest_len     
       

def lengthOfLongestSubstring(str):
     
    n = len(str)
    res = 0
  
    for i in range(n):
         
        visited = [0] * 256  
  
        for j in range(i, n):
  
            if (visited[ord(str[j])] == True):
                break
  
            else:
                res = max(res, j - i + 1)
                visited[ord(str[j])] = True
             
        visited[ord(str[i])] = False
     
    return res    


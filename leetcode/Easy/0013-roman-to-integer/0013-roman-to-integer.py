class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {}
        roman["I"] =            1
        roman["V"] =            5
        roman["X"] =            10
        roman["L"] =            50
        roman["C"] =            100
        roman["D"] =            500
        roman["M"] =            1000
        
        num = 0
        i = 0 
        while i < len(s):
            special_num = 0
            
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                special_str = s[i]+s[i+1]
                # if special_str == "IV":
                #     special_num = 4
                # elif special_str == "IX":
                #     special_num = 9
                # elif special_str == "XL":
                #     special_num = 40
                # elif special_str == "XC":
                #     special_num = 90
                # elif special_str == "CD":
                #     special_num = 400
                # elif special_str == "CM":
                #     special_num = 900
            
                num += roman[s[i+1]] - roman[s[i]]
                i += 2 
            else:
                num += roman[s[i]]
                i += 1

            
        return num 
            
            
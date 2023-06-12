class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        aa = 0
        abba = 0
        center = 0

        for word in list(set(words)): # minimum. 
            left, right = word
            if left == right:
                aa += words.count(word) // 2 * 2 
                if words.count(word) % 2 == 1: # e.g. abaa "aa" aaba, ab does not center
                    center = 2
            else:
                inv_word_cnt = words.count(right+left) # right+left is word[::-1]
                word_cnt = words.count(word)
                
                abba += min(inv_word_cnt, word_cnt) * 0.5 # get number of abba format 
                '''
                min(0,1) = 0 -> 0 * 0.5 = 0.0 -> int(0.0) = 0
                min(1,2) = 1 -> 1 * 0.5 = 0.5 -> int(0.5) = 0
                min(2,3) = 2 -> 2 * 0.5 = 1.0 -> int(1.0) = 1
                min(3,4) = 3 -> 3 * 0.5 = 1.5 -> int(1.5) = 1
                min(4,5) = 4 -> 4 * 0.5 = 2.0 -> int(2.0) = 2
                '''

        res = (aa*2) + int(abba)*4 + center 

        return res

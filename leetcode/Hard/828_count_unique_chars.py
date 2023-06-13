class Solution(object):
    def uniqueLetterString(self, s):
        index = {}
        result = 0
        for i, c in enumerate(s):
            k, j = index.setdefault(c, [-1, -1])
            print(k, j)
            result += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            result += (len(s) - j) * (j - k)
        return result

if __name__ == '__main__':

    s = "ABCA"

    '''
    0 : A이 unique인 부분 문자열 = A, AB, ABC
    1 : B이 unique인 부분 문자열 = B, AB, BC, BCA, ABC, ABCA
    3 : C이 unique인 부분 문자열 = C, BC, ABC, CA, BCA, ABCA
    4 : A이 unique인 부분 문자열 = A, CA, BCA
    '''

    result = Solution().uniqueLetterString(s)
    print(result)

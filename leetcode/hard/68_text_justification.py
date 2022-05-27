class Solution(object):
    def fullJustify(self, words, maxWidth):

        all_sentences = []
        sentences = []
        words_width = 0

        # 1. 문자열 조합 나누기
        # e.g. [['This', 'is', 'an'], ['example', 'of', 'text'], ['justification.']]
        for idx, word in enumerate(words):
            sentences.append(word)
            # 마지막 인덱스인 경우 마지막 단어를 all_results에 넣어주고 끝냄
            if idx == len(words) - 1:
                all_sentences.append(sentences)
                break
            words_width += len(word) + 1 # 공백 포함
            # 현재까지 모은 sentences 길이와 다음에 모을 sentences 길이가 maxWidth를 넘지 않는지 체크,
            # 넘는다면 적절한 조합이라고 판단하여 all_sentences 에 넣음
            if words_width + len(words[idx+1]) > maxWidth:
                all_sentences.append(sentences)
                sentences = []
                words_width = 0

        # 2. 나눈 문자열 조합에서 추가해야하는 공백 수(padding_width)를 구하고,
        #    마지막 줄은 왼쪽 정렬 처리,
        #    마지막 줄이 아니라면 오른쪽 보다 왼쪽에 더 많은 공백 할당 처리
        new_all_sentences = []
        for sentences in all_sentences:

            # 추가해야할 공백 수(padding_width) 계산
            sentences_width = len("".join(sentences))
            padding_width = maxWidth - sentences_width

            # 공백 추가 필요한 횟수
            padding_num = len(sentences) - 1

            # 한 단어인 경우
            if padding_num == 0:
                per_padding = padding_width
            else:
                per_padding = padding_width // padding_num

            # 마지막 줄 처리
            if all_sentences.index(sentences) == len(all_sentences) - 1:
                sentences = " ".join(sentences)
                sentences = sentences + " " * (padding_width - padding_num)
                new_all_sentences.append(sentences)
            else:
                # 마지막 줄이 아닌 경우 균등 공백 처리
                if padding_num == 0:
                    new_all_sentences.append(sentences[0] + " " * per_padding)
                else:
                    # 균등 공백 처리
                    if padding_width % padding_num == 0:
                        new_all_sentences.append((" " * (per_padding)).join(sentences))  # onestep00님 코드 참고
                    else:
                        # 균등 공백 처리 아닐 경우 blanks 계산하여 per_padding 처리
                        new_sentences = []

                        remain = padding_width % padding_num
                        blanks = [per_padding] * padding_num

                        for j in range(remain):
                            blanks[j] += 1

                        for j in range(1, padding_num + 1):
                            new_sentences.append(sentences[j-1])
                            new_sentences.append((" " * blanks[j-1]))
                        new_sentences.append(sentences[j])
                        new_all_sentences.append("".join(new_sentences))

        print(new_all_sentences)

if __name__ == "__main__":
    words1 = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth1 = 16

    words2 = ["What","must","be","acknowledgment","shall","be"]
    maxWidth2 = 16

    words3 = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
     "is", "everything", "else", "we", "do"]
    maxWidth3 = 20

    words4 = ["The","important","thing","is","not","to","stop","questioning.","Curiosity","has","its","own","reason","for","existing."]
    maxWidth4 = 17

    words5 = ["Here", "is", "an", "example", "of", "text", "justification."]
    maxWidth5 = 15

    words6 = ["My", "momma", "always", "said,", "\"Life", "was", "like", "a", "box", "of", "chocolates.", "You", "never", "know",
     "what", "you're", "gonna", "get."]
    maxWidth6 = 20

    Solution().fullJustify(words1, maxWidth1)
    Solution().fullJustify(words2, maxWidth2)
    Solution().fullJustify(words3, maxWidth3)
    Solution().fullJustify(words4, maxWidth4)
    Solution().fullJustify(words5, maxWidth5)
    Solution().fullJustify(words6, maxWidth6)

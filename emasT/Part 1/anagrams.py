def anagrams(word1,word2):
    if len(word1)!=len(word2):
        return False
    count = {}
    for char in word1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in word2:
        if char not in count:
            return False
        if char in count:
            count[char]-=1
        if count[char] < 0:
            return False
    return True


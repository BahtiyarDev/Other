def checker(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word2[i] == word2[-1]:
            break
        else:
            if word1[i] == word2[i]:
                count +=1
    print(count)

    if count/len(word1) > 0.75:
        return True
    else:
        return False
    
print(checker('apple', 'aple'))
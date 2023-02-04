sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

max_words = 0
temp_words = 0
i = 0
while (i<len(sentences)):
    j=0
    while(j<len(sentences[i])):
        if(sentences[i][j] == " "):
            temp_words+=1
        j+=1
    temp_words+=1
    if(max_words<=temp_words):
        max_words=temp_words
    i+=1
    temp_words=0
print(max_words)
K = int(input())
words=[]
for i in range(K):
    words.append(input())
N,M=map(int,input().split()) #M Max letter , N no of lines 
counter=0
for j in range(N):
    line=0
    for i in words:

        word_size=len(i)

        if word_size>M:
            continue

        if line == 0:
            line += word_size
            counter += 1
        elif word_size+1 + line <=M:
            line += word_size + 1
            counter += 1
    
    if counter == K:
        break
        
print(counter)   


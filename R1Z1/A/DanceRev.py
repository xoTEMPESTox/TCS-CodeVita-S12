N = int(input())
value=[]
for i in range(N):
    value.append(input())

counter = 0 
rythm = [value[0],value[1]]

for j in range(2,N):
    if value[j] not in rythm:
        if j + 1 < N and value[j + 1] == rythm[0]:
            rythm[1] = value[j]
        else:
            rythm[0] = value[j]
        counter += 1
    
print(counter)

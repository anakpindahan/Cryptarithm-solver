import time

letterList = []
words = []
solusi = []

def solve(copyWords, letterToNum, trial, solusi):
    if(all([int(letterToNum[z[0]]) != 0 for z in copyWords])):
        for i in range(0,len(copyWords)):
            word = copyWords[i]    
            for letter, num in letterToNum.items():
                word = word.replace(letter, str(num))
            copyWords[i] = word
        if(sum([int(z) for z in copyWords[:-1]]) == int(copyWords[-1]) and letterToNum not in solusi):
            for word in copyWords[:-1]:
                print(word)
            print('----+')
            print(copyWords[-1])
            print('!!!!!!')
            print("Jawaban ini ditemukan setelah " + str(trial) + " tes")
            solusi.append(letterToNum)


firstWord = input()
for x in firstWord:
    if x not in letterList:
        letterList.append(x)
words.append(firstWord)
while(True):
    secondWord = input()
    if secondWord[-1] == '+':
        for x in secondWord[:-1]:
            if x not in letterList:
                letterList.append(x)
        words.append(secondWord[:-1])
        break
    else:
        for x in secondWord:
            if x not in letterList:
                letterList.append(x)
        words.append(secondWord)
bar = input()
result = input()
for x in result:
    if x not in letterList:
        letterList.append(x)
words.append(result)

start = time.time()

print("Solusi:")
print("------------")
if(len(letterList) < 7):
    for z in range(10 ** (len(letterList) - 1), 10 ** len(letterList)):
        if(len(set(y for y in str(z))) == len(letterList)):
            letterToNum = dict(zip(letterList, [y for y in str(z)]))
            copyWords = words.copy()
            solve(copyWords, letterToNum, z, solusi)
            
elif(len(letterList) <= 10):
    numList = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    for z in range(1, 3265920):
        max = 0
        for i in range(0, 9):
            if(numList[i] < numList[i+1]):
                max = i
        maxG = max+1
        for j in range(max, 10):
            if(numList[j] > numList[max]):
                maxG = j
        temp = numList[max]
        numList[max] = numList[maxG]
        numList[maxG] = temp
        left = max+1
        right = 9
        while left < right:
            temp = numList[left]
            numList[left] = numList[right]
            numList[right] = temp
            left += 1
            right -= 1
        letterToNum = dict(zip(letterList, numList[:len(letterList)]))
            copyWords = words.copy()
            solve(copyWords, letterToNum, z, solusi)
else:
    print("Huruf yang diberikan terlalu banyak")

end = time.time()

print("Waktu yang diperlukan adalah " + str(end - start) + " detik")
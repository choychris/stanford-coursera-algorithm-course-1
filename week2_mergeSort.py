from math import ceil, floor
lines = [int(line.rstrip('\n')) for line in open('./_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt')]
# lista = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]

def mergeSortCount(fullList):
  n = len(fullList)
  m = int(ceil(float(n)/2))
  # print (fullList[m:])
  if(n == 1):
    return 0

  firstHalf = mergeSortCount(fullList[:m])
  secondHalf = mergeSortCount(fullList[m:])
  splitCount = mergeSplitInversionCount(fullList)

  return firstHalf + secondHalf + splitCount

def mergeSort(fullList):
  n = len(fullList)
  m = int(ceil(float(n)/2))
  # print (fullList[m:])
  if(n == 1):
    return fullList

  sortedArray = []
  i=0
  j=0
  firstHalf = mergeSort(fullList[:m])
  secondHalf = mergeSort(fullList[m:])
  while len(sortedArray) < n:
    if(secondHalf[j:] == []):
      sortedArray.append(firstHalf[i])
      i += 1
    elif (firstHalf[i:] == []):
      sortedArray.append(secondHalf[j])
      j += 1
    elif (firstHalf[i] < secondHalf[j]):
      sortedArray.append(firstHalf[i])
      i += 1
    elif (firstHalf[i] > secondHalf[j]):
      sortedArray.append(secondHalf[j])
      j += 1
  return sortedArray

def mergeSplitInversionCount(theArray):
  count = 0
  n = len(theArray)
  m = int(ceil(float(n)/2))
  i = 0
  j = 0
  firstHalfCount = m
  firstHalf = mergeSort(theArray[:m])
  secondHalf = mergeSort(theArray[m:])
  # print('m', m)
  # print('firstHalf', firstHalf)
  # print('secondHalf', secondHalf)
  for x in range(0, n):
    if(secondHalf[j:] == []):
      # print(secondHalf[j:])
      break
    elif(firstHalf[i:] == []):
      # print(firstHalf[i:])
      break
    elif(firstHalf[i] < secondHalf[j]):
      i += 1
      firstHalfCount -= 1
      # print(firstHalfCount)
    elif(firstHalf[i] > secondHalf[j]):
      j += 1
      count += firstHalfCount
      # print(count)

  return count

# print(mergeSortCount(lines))
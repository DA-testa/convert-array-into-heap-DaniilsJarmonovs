# python3
def build_heap(heap):
    swaps = []
    for i in range(count-1, -1, -1):
        current = i
        parent = (current-1)//2
        while(i>0 and parent>=0 and heap[current] < heap[parent]):
            heap[current], heap[parent] = heap[parent], heap[current]
            swaps.append([parent, current])
            if(current%2==0):
                if(heap[parent] > heap[current-1]):
                    heap[parent], heap[current-1] = heap[current-1], heap[parent]
                    swaps.append([current-1, parent])
            else:
                 if(heap[parent] > heap[current+1]):
                     heap[parent], heap[current+1] = heap[current+1], heap[parent]
                     swaps.append([current+1, parent])
            current = parent
            parent = (current-1)//2

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    #print(heap)
    return swaps


def main():
    inp = input()
    global count
    if("I" in inp):
        count = int(input())
        heap = list(map(int, input().split()))
    elif("F" in inp):
        FName = input()
        with open(FName, mode="r") as file:
            count = int(file.readline())
            text = file.readline()
            heap = list(map(int, text.split()))

    assert len(heap) == count
    swaps = build_heap(heap)
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i in swaps:
        print(i[0], i[1])
    ##for i, j in swaps:
      ##  print(i, j)


if __name__ == "__main__":
    main()
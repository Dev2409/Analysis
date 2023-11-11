def processArray(arr):
    i = 0
    while i < len(arr) - 1:
        if 100 <= arr[i] <= 999:
            max_val = arr[i]
            j = i + 1
            while j < len(arr) and 100 <= arr[j] <= 999:
                max_val = max(max_val, arr[j])
                j += 1
            arr[i] = max_val
            del arr[i + 1:j]
        i += 1
    return len(arr)

def main():
    arr = []
    while True:
        try:
            num = int(input())
            if num < 0:
                break
            arr.append(num)
        except ValueError:
            pass;

    length = processArray(arr)

    for i in range(length):
        print(arr[i])

if __name__ == "__main__":
    main()

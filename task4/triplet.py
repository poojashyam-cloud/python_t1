def hasTripletSum(arr, target):
    n = len(arr)

    # Fix the first element as arr[i]
    for i in range(n - 2):

        # Fix the second element as arr[j]
        for j in range(i + 1, n - 1):

            # Now look for the third number
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True

    return False


if __name__ == "__main__":
    arr = [10,20,30,9]
    target = 59
    if hasTripletSum(arr, target):
        print("true")
    else:
        print("false")
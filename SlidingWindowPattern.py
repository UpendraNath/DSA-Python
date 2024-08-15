def main1(arr: list[int], K:int):
    #Initialize the list to store final result and window sum
    results = []
    window_sum, window_start= 0, 0

    for window_end in range(len(arr)):
        print("cuurent window end:",window_end)
        window_sum += arr[window_end]
        print("outer loop")
        print(window_sum)

        if window_end>= K-1:
            print("inside window_end ",window_end)
            print("inner_if")
            results.append(window_sum)
            print("current window sum :", window_sum)
            window_sum -= arr[window_start]
            print("new window sum :", window_sum)
            window_start += 1
            print("new window start", window_start)
            print("results", results)

    return min(results)

if __name__ == "__main__":
    test_arr = [10, 4, 2, 5, 6, 3, 8, 1]
    test_k =3
    print(main1(test_arr,test_k))

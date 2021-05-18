def determine_last_name(arr):
    if '.' not in arr[len(arr)-1] and arr[len(arr)-1][0].lower() != arr[len(arr)-1][0]:
        return arr[len(arr)-1]
    return arr[len(arr)-2]
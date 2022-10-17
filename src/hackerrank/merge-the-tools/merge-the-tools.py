def merge_the_tools(string, k):
    # is guaranteed that n is a multiple of k
    n = len(string)
    # so we can chunk like this:
    chunked_string = [string[i:i+k] for i in range(0, n, k)]

    # get each subsequence and check if they repeat
    for t in chunked_string:
        u = ""
        for i in t:
            if (i in u):
                pass
            else:
                u = u+i
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

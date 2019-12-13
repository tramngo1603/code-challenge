# To do: when the input is already the largest number that could be represented
# by the number, would it return the input number itself, or raise an error?

def my_func(num):
    int_list = [int(i) for i in str(num)]
    n = len(int_list)

    for j in reversed(range(n)):
        if int_list[j] > int_list[j-1]:

            m = min(int_list[j:])
            m = int_list.index(m)
            int_list[j-1], int_list[m] = int_list[m], int_list[j-1]
            int_list[j:] = sorted(int_list[j:])
            break

    result = int("".join(map(str, int_list)))
    return result

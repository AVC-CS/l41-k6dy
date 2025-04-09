def main():

    N = int(input('Enter the number N: '))
    result = []

    for i in range(N + 1):
        result.append(2 ** i)
    return result


if __name__ == '__main__':
    print(main())
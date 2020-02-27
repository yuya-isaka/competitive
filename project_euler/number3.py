if __name__ == "__main__":
    division = 3
    target = 600851475143

    while division < target:
        quotient, remainder = divmod(target, division)

        if remainder == 0:
            print('%d can be divided by %d' % (target, division))

            target = quotient

        else:
            division += 2

    print('largest prime factor is %d' % division)
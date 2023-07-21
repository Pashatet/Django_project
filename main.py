def fig(height, width):


    # for i in range(height):
    #     for j in range(i):
    #         print("*", end="")
    # print()

    for i in range(height):

        for j in range(height - i):
            print(" ", end="")

        for k in range(i + 1):
            print("*", end="")
        for l in range(width - 1):
            print(" ", end="")
        print()

fig(10,5)
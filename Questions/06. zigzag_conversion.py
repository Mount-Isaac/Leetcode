def zigzag_conversion(s, numRows):
    main_list = []

    for x in range(numRows):
        main_list.append([str(x)])
    return main_list

print(zigzag_conversion('paypalishiring', 3))

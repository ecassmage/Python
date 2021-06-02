def parseLog():
    information = open("LoggingTimes.txt").readlines()
    if len(information) < 2:
        return
    # print(information[0], end='')
    # print(information[1])
    line1 = information[0].replace("\n", '').split(' ')
    line2 = information[1].replace("\n", '').split(' ')
    # print(
    #     f"{float(line1[0]) / float(line2[0])} {float(line1[1]) / float(line2[1])} {float(line1[2]) / float(line2[2])}")
    LoggingFile = open("TimeLogs.txt", 'a')
    LoggingFile.write(
        f"Test1: {line1[0]} ::: Test2: {line2[0]}\n"
        f"{float(line1[0]) / float(line2[0])} "
        f"{float(line1[1]) / float(line2[1])} "
        f"{float(line1[2]) / float(line2[2])}"
        f"\n\n"
    )
    LoggingFile.close()

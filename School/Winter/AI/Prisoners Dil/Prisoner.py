import random
import json


def getOdds():
    """
    Generates a random number.
    :return: returns random number
    """
    num = random.randrange(100)  # + random.random()
    return num if num <= 100 else 100


def betray(oddsOfBetrayal):
    """
    checks odds of betrayal utilized the getOdds() function to generate a
    random number so as to be used for calculating odds.
    :param oddsOfBetrayal: utilizes a number which indicates odds. Controlled inside the prisoners.json file.
    :return: returns boolean for if a betrayal occurred or not.
    """
    return True if getOdds() < oddsOfBetrayal else False


def PrisonerSubject():
    """
    Runs a simulation however many times are specified in the json file and will
    calculate the time this subject would face if they chose to betray or didn't.
    :return: Nothing.
    """
    info = json.load(open("prisoners.json"))  # imports json initializing file

    start, stop = round(info["OtherPrisoner"]["BetrayalOdds"]), round(info["OtherPrisoner"]["BetrayalOdds"]) + 1
    if isinstance(info["OtherPrisoner"]['Iterate'], list):
        start, stop = info["OtherPrisoner"]['Iterate']
        stop += 1
    Betrayals = 0
    NoBetrayals = 0

    for odds in range(start, stop):
        NoBetrayal, Betrayal = 0, 0

        for _ in range(info["Tests"]):
            OtherPrisonerBetrayalFactor = betray(odds)

            if OtherPrisonerBetrayalFactor:  # if True
                Betrayal += info["Punishments"]["DoubleBetrayal"]
                NoBetrayal += info["Punishments"]["SingleBetrayal_NotBetrayer"]

            else:  # if False
                Betrayal += info["Punishments"]["SingleBetrayal_Betrayer"]
                NoBetrayal += info["Punishments"]["NoBetrayals"]

        print(f"Odds: {odds}%")
        #                             Accumulated years prison, Averaged over x number of tests.
        print(f"\tDidn't Betray:    {NoBetrayal} (years total), Average Time (years): {NoBetrayal / info['Tests']}\n"
              f"\tDid Betray:       {Betrayal} (years total), Average Time (years): {Betrayal / info['Tests']}\n"
              f"\tConclusion:       {'Betray' if Betrayal < NoBetrayal else 'Do not Betray'}\n")

        match Betrayal < NoBetrayal:
            case True:
                Betrayals += 1
            case False:
                NoBetrayals += 1

    print(f"Final Conclusion: \n"
          f"\tBetrayals:    {Betrayals}\n"
          f"\tNo Betrayals: {NoBetrayals}\n")


if __name__ == '__main__':
    RunProg = True
    while True:
        if RunProg:
            PrisonerSubject()
            RunProg = False
        inp = input("\nQuit: to exit\n"
                    "Run: to run program\n"
                    "Type here: ")
        match inp.lower():
            case 'quit':
                exit()
            case 'run':
                RunProg = True

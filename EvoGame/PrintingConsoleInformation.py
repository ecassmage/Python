import Logic


def smallest(contested, contestant):
    return contested if contested < contestant else contestant


def largest(contested, contestant):
    return contested if contested > contestant else contestant


def statCalculations(GUI, after=True):
    speed, vision, size, fertility, age, energyUse, energyAtEnd = 0, 0, 0, 0, 0, 0, 0
    speedL, visionL, sizeL, fertilityL, ageL, energyUseL, energyAtEndL = 0, 0, 0, 0, 0, 0, 0
    speedS, visionS, sizeS, fertilityS, ageS, energyUseS, energyAtEndS = 0, 0, 0, 0, 0, 0, 0
    try:
        tempFirst = GUI.usedHumans[0]
        speedS, visionS, sizeS, fertilityS, \
            ageS, energyUseS, energyAtEndS = \
            tempFirst.speed, tempFirst.vision, tempFirst.size, tempFirst.fertility, \
            tempFirst.age, Logic.energyLoss(tempFirst), tempFirst.energy
    except IndexError:
        pass
    for human in GUI.usedHumans:
        speed += human.speed
        vision += human.vision
        size += human.size
        fertility += human.fertility
        age += human.age
        energyUse += Logic.energyLoss(human)
        energyAtEnd += human.energy
        speedL = largest(speedL, human.speed)
        visionL = largest(visionL, human.vision)
        sizeL = largest(sizeL, human.size)
        fertilityL = largest(fertilityL, human.fertility)
        ageL = largest(ageL, human.age)
        energyUseL = largest(energyUseL, Logic.energyLoss(human))
        energyAtEndL = largest(energyAtEndL, human.energy)
        speedS = smallest(speedS, human.speed)
        visionS = smallest(visionS, human.vision)
        sizeS = smallest(sizeS, human.size)
        fertilityS = smallest(fertilityS, human.fertility)
        ageS = smallest(ageS, human.age)
        energyUseS = smallest(energyUseS, Logic.energyLoss(human))
        energyAtEndS = smallest(energyAtEndS, human.energy)

    if after is False:
        print("____________________________________________________________________________________________________"
              "____________________________________________________________________________________________________")
        print("\tNext Round")
    if speed == 0 or vision == 0 or size == 0 or fertility == 0 or age == 0:
        print(
            f"A Zero was found where it shouldn't have been, "
            f"{speed}, {vision}, {size}, {fertility}, {age}, {energyUse}, {energyAtEnd}\n"
        )
    else:
        L = len(GUI.usedHumans)
        print(f"Average Speed: {format(speed / L, '.2f')}, Average Vision: {format(vision / L, '.2f')}, "
              f"Average Size: {format(size / L, '.2f')}, Average Fertility: {format(fertility / L, '.2f')}, "
              f"Average Age: {format(age / L, '.2f')}, Average Energy Used: {format(energyUse / L, '.2f')}, "
              f"Average Energy Remaining: {format(energyAtEnd / L, '.2f')}\n")
    print(f"Smallest Speed: {format(speedS, '.2f')}, Smallest Vision: {format(visionS, '.2f')}, "
          f"Smallest Size: {format(sizeS, '.2f')}, Smallest Fertility: {format(fertilityS, '.2f')}, "
          f"Smallest Age: {format(ageS, '.2f')}, Smallest Energy Used: {format(energyUseS, '.2f')}, "
          f"Smallest Energy Remaining: {format(energyAtEndS, '.2f')}")
    print(f"Largest Speed: {format(speedL, '.2f')}, Largest Vision: {format(visionL, '.2f')}, "
          f"Largest Size: {format(sizeL, '.2f')}, Largest Fertility: {format(fertilityL, '.2f')}, "
          f"Largest Age: {format(ageL, '.2f')}, Largest Energy Used: {format(energyUseL, '.2f')}, "
          f"Largest Energy Remaining: {format(energyAtEndL, '.2f')}\n")
    print(f"Total Human Population: {len(GUI.usedHumans)}, Total Food Available: {GUI.sizeOfDict()}, "
          f"Total Energy At Start: {GUI.settings['human']['energy']}\n\n")
    if after:
        print()
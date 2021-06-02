import time


def routineRoundChecks(screen):
    for human in screen.usedHumans:
        checkMoves(human)
    makeTurnMoves(screen.usedHumans)


def checkMoves(human):
    if human.survive or human.eaten:
        return
    human.isFoodEaten()
    human.findCoord()


def energyLoss(human):
    # energy = (human.fertility * ((human.speed ** 2) * (human.size ** 3) + human.vision)) / 40
    fertility = human.fertility * human.canvas.settings['game_rules']['ability_costs']['fertility_costs']
    speed = (human.speed ** 2) * human.canvas.settings['game_rules']['ability_costs']['speed_costs']
    size = (human.size ** 3) * human.canvas.settings['game_rules']['ability_costs']['size_costs']
    vision = human.vision * human.canvas.settings['game_rules']['ability_costs']['vision_costs']
    return 1.1 * ((speed * size + vision) + (fertility * human.speed * human.size * human.vision) + 100)
    # return (fertility * (speed * size + vision)) + 100


def routineHumanChecksAfterAllMovesDone(humans):
    for human in humans:
        if human.energy <= 0 and human.survive is False:
            human.killHuman()
        human.refreshRemainingMoves()
        if human.survive is False:
            human.energy -= energyLoss(human)


def makeTurnMoves(humans):

    finished = 0
    while makePixelTurnMoves(humans) < len(humans):

        if humans[0].canvas.refreshSpeed == "Medium" or humans[0].canvas.refreshSpeed == "medium":
            humans[0].canvas.tk.update()

    if humans[0].canvas.refreshSpeed == "Fast" or humans[0].canvas.refreshSpeed == "fast":
        humans[0].canvas.tk.update()

    elif humans[0].canvas.refreshSpeed == "Ultra" or humans[0].canvas.refreshSpeed == "ultra":
        if humans[0].canvas.megaFast == humans[0].canvas.settings['dev']['ultra']:
            humans[0].canvas.tk.update()
            humans[0].canvas.megaFast = 0
        else:
            humans[0].canvas.megaFast += 1

            # print(humans[0].canvas.megaFast)

    routineHumanChecksAfterAllMovesDone(humans)


def makePixelTurnMoves(humans, finished=0):
    for human in humans:
        if human.survive or human.alive is False:  # human.survive is True or human.alive is False
            finished += 1
            continue
        if human.beingChased[0] is False or human.chosenTarget is None or human.moveTo is None:
            human.whatIsHumanChasing()
        human.move()

        if human.movesRemaining == 0:
            finished += 1

        if human.canvas.refreshSpeed == "Slow" or human.canvas.refreshSpeed == "slow":
            human.canvas.tk.update()
    return finished

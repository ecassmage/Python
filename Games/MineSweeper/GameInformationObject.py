from Settings import JOpen


class GameInformation:
    def __init__(self):
        self.GameJSON = JOpen.JOpen("settings.json")  # Might Get rid of this, Not Sure
        self.GameDifficulty = self.GameJSON[self.GameJSON["Default"]]
        self.SafeStartMode = self.GameJSON["Safe Start"]  # Basically Are you Guaranteed to not hit a mine on your first choice or not True means Guaranteed, False means you might choose a mine on this first choice.

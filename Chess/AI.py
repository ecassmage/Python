import Pieces
import copy


def checkMovesThatKill(board, piece, coord):
    """
    [R N B K Q B N R]
    [P P P P P P P P]
    [. . . . . . . .]
    [. . . . X . X .]
    [. . . X . . . X]
    [. . . . . N . .]
    [P P P X P P P X]
    [R N B Q X B X R]
    """
    return


def isThisMoveLegal(board, move):
    if move in board.coord:
        return True
    return False


def pawnsAreSpecial(piece):
    if piece.hadMoves is False:
        pass
    return


def notAPawnSoNotSpecial(board, piece):
    fakeBoard = copy.deepcopy(board.)
    for move in piece.moves:
        if piece.repetition:
            pass
        else:
            tempCoord = (piece.x + move[0], piece.y + move[1])
            if isThisMoveLegal(board, tempCoord):
                pass


def checkMove(board, piece):
    if type(piece) is Pieces.Pawn:
        pawnsAreSpecial(piece)
    else:
        notAPawnSoNotSpecial(board, piece)
    return


def loopThroughTeamPieces(board, team):
    for piece in team.pieces:
        checkMove(board, piece)


def main(board, team):
    loopThroughTeamPieces(board, team)
    return


if __name__ == "__main__":
    # main()
    pass

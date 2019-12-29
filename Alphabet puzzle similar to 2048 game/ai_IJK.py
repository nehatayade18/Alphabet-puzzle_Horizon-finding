#!/usr/local/bin/python3

"""
This is where you should write your AI code!

Authors: Viral Prajapati vkprajap

Based on skeleton code by Abhilash Kuhikar, October 2019
"""

from logic_IJK import Game_IJK
import random


# Suggests next move to be played by the current player given the current game
#
# inputs:
#     game : Current state of the game 
#
# This function should analyze the current state of the game and determine the 
# best move for the current player. It should then call "yield" on that move.

def next_move(game: Game_IJK) -> None:
    '''board: list of list of strings -> current state of the game
       current_player: int -> player who will make the next move either ('+') or ('-')
       deterministic: bool -> either True or False, indicating whether the game is deterministic or not
    '''
    board = game.getGame()
    player = game.getCurrentPlayer()
    #deterministic = game.getDeterministic()

    MAX, MIN = float('inf'), float('-inf')

    ### Heuristics ###

    def emptyTilesHeuristic(board):
        emptyTiles = 0
        for i in range(36):
            if board[i] == " ":
                emptyTiles += 1

        return emptyTiles

    def weightedTilesHeuristic(board, player):
        boardScore = [6 * 35, 6 * 34, 6 * 33, 6 * 32, 6 * 31, 6 * 30,
                      6 * 24, 6 * 25, 6 * 26, 6 * 27, 6 * 28, 6 * 29,
                      6 * 23, 6 * 22, 6 * 21, 6 * 20, 6 * 19, 6 * 18,
                      6 * 12, 6 * 13, 6 * 14, 6 * 15, 6 * 16, 6 * 17,
                      6 * 11, 6 * 10, 6 * 9, 6 * 8, 6 * 7, 6 * 6,
                      6 * 0, 6 * 1, 6 * 2, 6 * 3, 6 * 4, 6 * 5]

        boardScore1 = [2 ** 5, 2 ** 5, 2 ** 5, 2 ** 5, 2 ** 5, 2 ** 5,
                      2 ** 5, 2 ** 4, 2 ** 4, 2 ** 4, 2 ** 4, 2 ** 5,
                      2 ** 5, 2 ** 4, 2 ** 3, 2 ** 3, 2 ** 4, 2 ** 5,
                      2 ** 5, 2 ** 4, 2 ** 3, 2 ** 3, 2 ** 4, 2 ** 5,
                      2 ** 5, 2 ** 4, 2 ** 4, 2 ** 4, 2 ** 4, 2 ** 5,
                      2 ** 5, 2 ** 5, 2 ** 5, 2 ** 5, 2 ** 5, 2 ** 5]

        score = 0
        upperScore = 0
        lowerScore = 0
        for i in range(36):
            currentElement = ord(board[i])
            if currentElement >= 65 and currentElement <= 90:
                upperScore += 2 ** (currentElement - 64)
            elif currentElement >= 95 and currentElement <= 122:
                lowerScore += 2 ** (currentElement - 96)
            else:
                pass
        if player == "+":
            score = upperScore - lowerScore
        else:
            score = lowerScore - upperScore

        return score
    
    def calculateMonotonicity(state):
        score = 0
        for i in range(6):
            row = state[i]
            for j in range(6):
                x = row[j]
                if state[i][j] != 0 and j != 5 :
                    for z in range(j+1 ,6):
                        if state[i][z] != 0 :
                            index = z
                            break
                        elif z == 5 and state[i][z] == 0:
                            index = z
                    if x <= row[index] and row[index] != 0  :
                        score = score + 15
                    elif x > row[index] and row[index] != 0 :
                        score = score - 10
                    if x <= state[index][j] :
                        score = score + 10
                    elif x > state[index][j] :
                        score = score - 15
                if state[i][j] != 0 and i!= 5 :
                    for z in range(i + 1, 6) :
                        if state[z][j] != 0:
                            index = z
                            break
                        elif z == 5 and state[z][j] == 0:
                            index = z
                    if x <= state[index][j] and state[index][j] != 0  :
                        score = score + 10
                    elif x > state[index][j] and state[index][j] != 0 :
                        score = score - 15
                elif state[i][j] == 0 :
                    score = score + 0
        return score

    def calculateSmoothness(state):
        score = 0
        for i in range(6):
            row = state[i]
            for j in range(6):
                x = row[j]
                if j != 5 and (x - state[i][j + 1]) <= 1:
                    score = score + 5
                if i != 5 and (x - state[i + 1][j]) <= 1:
                    score = score + 5

        return score
    
    def strToNum(state):
        for i in range(0, 6):
            for j in range(0, 6):
                if state[i][j] == "A" or state[i][j] == "a":
                    state[i][j] = 1
                elif state[i][j] == "B" or state[i][j] == "b":
                    state[i][j] = 2
                elif state[i][j] == "C" or state[i][j] == "c":
                    state[i][j] = 3
                elif state[i][j] == "D" or state[i][j] == "d":
                    state[i][j] = 4
                elif state[i][j] == "E" or state[i][j] == "e":
                    state[i][j] = 5
                elif state[i][j] == "F" or state[i][j] == "f":
                    state[i][j] = 6
                elif state[i][j] == "G" or state[i][j] == "g":
                    state[i][j] = 7
                elif state[i][j] == "H" or state[i][j] == "h":
                    state[i][j] = 8
                elif state[i][j] == "I" or state[i][j] == "i":
                    state[i][j] = 9
                elif state[i][j] == "J" or state[i][j] == "j":
                    state[i][j] = 10
                elif state[i][j] == "K" or state[i][j] == "k":
                    state[i][j] = 11
                else:
                    state[i][j] = 0
        return state

    def calHeuristic(board, state, player):

        state = strToNum(state)
        emptyTiles = emptyTilesHeuristic(board) * 100
        #boardScore = weightedTilesHeuristic(board, player) * 50
        monotonicity = calculateMonotonicity(state) * 100
        smoothness = calculateSmoothness(state) * 200
        
        return emptyTiles + monotonicity + smoothness

    def successors(game1):
        moves = ['U', 'D', 'L', 'R']

        futureStates = []
        for move in moves:
            successor = game.makeMove(move)
            successor = successor.getGame()
            futureStates.append((successor,move))
        return futureStates

    def flattenList(lisst):
        flatList = []
        for lists in lisst:
            for value in lists:
                flatList.append(value)
        return flatList

    def getMove(arr):
        for i in range(len(arr)):
            arr[i] = list(arr[i])
            if i >= 0 and i < 64:
                arr[i][1] = 'U'
            elif i >= 64 and i < 128:
                arr[i][1] = 'D'
            elif i >= 128 and i < 192:
                arr[i][1] = 'L'
            elif i >= 192 and i < 256:
                arr[i][1] = 'R'

        return arr

    def parseTree(game1, player):
        depthOne = successors(game1)
        depthTwo = []
        for states in depthOne:
            depthTwo.append(successors(states[0]))
        depthTwo = flattenList(depthTwo)
        depthThree = []
        for states in depthTwo:
            depthThree.append(successors(states[0]))
        depthThree = flattenList(depthThree)
        depthFour = []
        for states in depthThree:
            depthFour.append(successors(states[0]))
        depthFour = flattenList(depthFour)
        
        futureStates = []
        futureMoves = []
        for i in depthFour:
            futureStates.append(i[0])
            futureMoves.append(i[1])
        scores = calScore(futureStates, player)
        finalMoves = []
        for i in range(len(scores)):
            finalMoves.append((scores[i],futureMoves[i]))
        finalMoves = getMove(finalMoves)
        return finalMoves

    def calScore(arrStates, player):
        scores = []
        for state in arrStates:
            board = flattenList(state)
            score = calHeuristic(board, state, player)
            scores.append(score)
        return scores

# Took reference from geeksforgeeks #
    def minimax(depth, node, maxPlayer, values, alpha, beta):
        if depth == 4:
            return values[node][0], values[node][1]
        if maxPlayer:
            bestScore = MIN
            bestMove = " "
            for i in range(0, 4):
                val, newMove = minimax(depth + 1, node * 4 + i, False, values, alpha, beta)
                if val > bestScore:
                    bestScore = val
                    bestMove = newMove
                alpha = max(alpha, bestScore)

                if beta <= alpha:
                    break
            return (bestScore, bestMove)
        else:
            bestScore = MAX
            bestMove = " "
            for i in range(0, 4):
                val, newMove = minimax(depth + 1, node * 4 + i, True, values, alpha, beta)
                if val < bestScore:
                    bestScore = val
                    bestMove = newMove
                beta = min(beta, bestScore)
                if beta <= alpha:
                    break
            return (bestScore, bestMove)

    validStates = parseTree(board, player)
    score, move = minimax(0, 0, True, validStates, MIN, MAX)

    yield move

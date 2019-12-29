# PART 1: Alphabet puzzle similar to 2048

Problem Solving Approach:

The IJK problem is similar to the classic and popular 2048 board game. So using the tricks and techniques of 2048 game we have implemented IJK. The basic flow of the implementation of ai_IJK is for each state ai looks for all the possible states using valid 4 moves ('U','D','L','R') for a predefined depth(i.e. 4), then we use an evaluation function to assign score to each of this states at depth 4. Now on this score we use minimax algorithm to find out the most optimum move for the AI.

Evaluation Function:

For evaluation function we have implemented 4 heuristic functions.
	1. Empty Tiles:
		This heuristic function helps avoiding crowding of the board by giving bonus if board contains more number of empty tiles.
	2. Weighted Tiles:
		This heuristic calculates score by summing up the products of weights and tile values for every occupied tile on a board. This heuristic function is inspired from 'Beginner’s guide to AI and writing your own bot for the 2048 game'(https://medium.com/@bartoszzadrony/beginners-guide-to-ai-and-writing-your-own-bot-for-the-2048-game-4b8083faaf53).
	3. Monotonicity:
		This heuristic function calculates monotonicity of each element, i.e. each tile should be in lexicographical order, thus if tile = 'C' then, tiles < B should be on its left and tiles > B should be on its right. If this pattern is not fulfilled than penalty is assigned. And same for top and bottom tile.
	4. Smoothness:
		This heuristic decreases the heuristic value by the total of all differences of all adjacent pair of tiles. It basically makes sure that same valued tiles are adjacent to each other. This heuristic function is inspired from 'Minimax and Expectimax Algorithm to Solve 2048'(https://azaky.github.io/2048-AI/paper.pdf).

Minimax Algorithm:

Minimax algorithm is used to find the optimum move using the score calculated by our above evaluation function. Implemented minimax is minimax with alpha beta pruning for depth 4.

Initial State:
For Deterministic Mode:
	board of 6 x 6 with "a" on board location (1,1)
For Non Deterministic Mode:
	board of 6 x 6 with "a" on random board location
	
Goal State:
	board containing final element that is k or K
	

Citation:
Discussed the types of heuristics that can be used with vanshah.


# Part 2: Geolocating images by finding horizon

Logic:
viterbi Algorithm used:
#Non-human input:Main function(Viterbi):  
This function calculates the most probable path of following the discretion in the images. The emission probability is calculated from edge strength. Transpose of matrix is taken and then column wise each strength is divided by the sum of the column to return the emission probability. Log transform is taken to avoid issues related with large numbers. The emission probabilities(e[j][i]) are taken as starting points after sorting to obtain the highest gradient row. Each emission probability is assigned as a start point for determining the best path of gradients based on edge strength. For each emission probabilities selected in the row the main function, two variable arrays(nodes) are allotted that store the probability of most likely path so far. The emission probability is multiplied with each of the most recent state before transition giving a set of observed states. This is stored as start probability is an array wrt each state traversed. Separate arrays store the start indices and the start probabilities.  In the for loop, for each observation(j=1,2,3..) and for each state(i=1,2,3..), the emission probability(e[j][i]) is multiplied with transition probability and the currently observed state.
Prob_var1[j,i] <- max (prob_var1[I,j-1]*e[j][i]*T[i])
 If the transition of state i to j is from a higher gradient to another one, the compare array stores the increased intensity value in it. If the transition is to a lower gradient, the probability value is decreased. The obtained probability is then added to the path probabilities and the transition index value to the index array.

#Viterbi function human input: 
Viterbi with human input takes x and y coordinates as inputs from the user and the distance of strength values row and column wise are computed in for loops. Total distance of all the maximum gradient values from the selected coordinates is calculated and their addition of vertical and horizontal distances. The minimum distances are chosen from array of distances is chosen to plot the curve of maximum transition calculated from the function of Viterbi with human inputs. In this function, 25 different paths are generated for 25 different start points and then these distances are compared with human entered values. Points corresponding to minimum of the distances are selected for edge plot. Rest all calculations are same as the above function. The ridge plots edge on the image separating horizons.

Referred: https://en.wikipedia.org/wiki/Viterbi_algorithm
Image samples:
 
Output image1
https://github.iu.edu/cs-b551-fa2019/ntayade-daugge-vkprajap-a2/blob/master/output1.jpg
 
Output image 2:
https://github.iu.edu/cs-b551-fa2019/ntayade-daugge-vkprajap-a2/blob/master/output2.jpg

Output image 5:
https://github.iu.edu/cs-b551-fa2019/ntayade-daugge-vkprajap-a2/blob/master/output5.jpg
 
Downloaded image sample:
https://github.iu.edu/cs-b551-fa2019/ntayade-daugge-vkprajap-a2/blob/master/download.jpg

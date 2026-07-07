# tictactoe-rl

This project trains an agent to learn tictactoe on its own and later allows the user to play tic tac toe with the agent.
This project does not use neural networks, no strategy is taught to the agent by any outside source. It uses Q-Learning to learn tictactoe from scratch.
I used Claude to help me write the code line by line and understand the concepts more clearly. 

## How it works

How does this agent learn? The agent first randomly guesses its moves. However, when it arrives at a win, loss, or draw, the result is passed down to each previous position every iterative game. 
This allows the agent to evaluate the position. The epsilon for random moves decreases over time, allowing for more exploitation and less exploration over time. This is called epsilon decay. 

## Files

There are 5 files. 
board.py sets up the board. 
test_board.py tests if the board is working correctly
agent.py defines what the agent can do. 
train.py trains the agent to play against itself.
play.py allows the user to play against the agent. If the agent is not trained, the user will play against an agent choosing randomly.

## Usage

Train the agent (takes about a few minutes though depends on the computer):

    python3 train.py

Play against it:

    python3 play.py

Or double-click `play.command` (macOS). If downloaded as ZIP, 
run `chmod +x play.command` first.

## Results

Untrained agent plays randomly
A trained agent basically never loses though there may be exceptions I am not aware of. 

## Next

Replace Q-table with a neural network and add tree search. This would be the path toward AlphaZero-style agents for larger games requiring more data. 
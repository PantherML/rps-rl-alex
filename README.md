# RPS Reinforcement Learning
The goal is to use reinforcement learning for the optimal policy for rock paper scissors.

The optimal policy would be one where each state (Rock, Paper, Scissors) maps to the move to defeat each of those states 100%.

How the environment works is by default it sets up a best out of 3 game. As the agent you'll know ahead of time what the opponenets move is, the goal is to learn the proper defense to win. The jupyter notebook features a full template for you to use with an agent that initally does random moves (or you can try out does one move consistently). This results in that the agent will only win 50% of best of 3's on average, with winning each match 1/3 of the time. The goal is to have 100% win and each match be 100% win.

## How to setup

1. Install python of course :stuck_out_tongue: 
2. In the terminal run the follwing command `pip install pipenv --user` 
  - This installs a program that I use to simply virtual environments, library versions, etc. (feel free to ask why you should do this!)
3. Maybe update the `Pipfile` to your python version (it has `3.8` set but if you are using a version such as `3.9` or `3.10` set it to that)
4. Next run in the terminal `pipenv install`, this will install everything you need! :smile:
5. Finally, run `pipenv run jupyter lab`, this will open up jupyter lab and you will have a notebook called `Experiment` where you'll do your work

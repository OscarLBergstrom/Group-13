# Decide - Group-13

## Anti-Ballistic Missile System

Decide is a program that decides wether a defence system should launch an Anti-Ballistic Missile or not. 

### Structure

**The inputs for the program are:**
* POINTS - an array containing coordinates of datapoints
* NUMPOINTS - The number of points
* PARAMETERS - Contains multiple parameters that are important for the LIC functions.
* LCM - Logical center matrix
* PUV - Preliminary Unlocking Vector. 

**The outputs for the program are:** 
* Launch - A "YES" or a "NO" depending on if the missile should launch. Sent through standard output.

    In addition, the following intermediate results are computed:

* CMV - Conditions met vector
* PUM - Prelimerary unlocking matrix
* FUV - Final unlocking vector

### Control flow
Decide depends on a vector called FUV where every value must be True for decide to return True. 

FUV depends on matrix (15x15) called PUM. 

PUM depends on a matrix called CMW given by 15 logical functions called LIC.

The control flow is visualised on in the image below. 

![](https://i.imgur.com/VTqxt3S.png)

# Statement of contribution

The work was divided per the following.

LIC 0,7,12 Felipe Oliver

LIC 1,8,13 Filip Wetterdal Todorovic

LIC 2,4,9 Gustaf Johansson

LIC 3,10,14 Oscar Bergström

LIC 5,6,11 Jacob Trossing

README Oscar Bergström

PUM, FUV Jacob Trossing & Gustaf Johansson

DECIDE Filip Wetterdal Todorovic & Felipe Oliver

# Work process and state

## Process

Communication is based around a slack group.

CircleCI is used in order to make sure that commits and pull requests pass tests and compilation. 

We started of by dividing the assignment into smaller issues which were divided amongst the groupmembers. 

For each issue we created a branch to commit to. Each commit were connected to an issue.  

If another issue was discovered we would create another GitHub Issue and work towards solving it. 

Each PR had to be approved by another groupmember. 

## Current State

The current state that the team is in is "In Use".

The practices and tools have been used to complete this assignment.

We reguraly inspect the tools in order to improve our work. Because group is still fairly new to the practices we still need to inspect them reguarly to find improvements.

The pratices and tools have been adapted to complete this assignment/context.

The team has agreed on the practices and they are supported across all teammembers. 

Practices such as PR reviews have been used to handle feedback and make sure that people follow the practices set by the team.

The practices are supported by the teams communication on slack. 

## Next state

One obstaceles to reach the next state is that every groupmember needs to become familiar with the processes and tools used in the project. This will be done by continious feedback and continiously use the practices and tools. 


### P+ contribution

In order to achive the P+ grade we used CircleCI integration on Github. 

We also connected the commits to issues in the title or description.



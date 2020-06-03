# Notes on Chapter 4: Beyond Classical Search

## Local Search

in many problems, the path that was taken to get to a goal doesn’t matter

e.g. in the n-queens problems, you are asked to place n chess queens on a square nxn board so that no two queens are in the same row, column, or diagonal (i.e. no two queens attack each other)

the order in which the queens are placed doesn’t matter; all we care about is the final configuration

this suggests another approach to searching: keep track of just the current node, generate its successors, and then choose one of those successors to be the next current node

this is the basic idea of **local search**

local search typically uses **much** less memory than classical search algorithms like A*-search, and in practice has been used to find good solutions to large and difficult problems

Figure 4.1 of the textbook shows the **state-space landscape** of a search problem, which can be a useful way of thinking about local search

essentially, we want to find the highest point in the landscape, and local search says to do this by taking one step at a time in a close-by direction

as Figure 4.1 shows, local search can get stuck in local maxima, or stuck on plateaus, and so some strategy is needed to deal with such problems

- note that we now talk about *maximizing* the score of a node, i.e. the higher the better; this is the opposite of what we did with A*-search, where in A*-search the lower the f-value the better

## Hill Climbing

**hill-climbing** is a simple local search algorithm that can find local maximas

- a local maxima is a point near (i.e. local) to the start point that is a maximum value

the idea is you have a current state, and then you always move to the successor state that has the highest value (for some function of interest); if no successor state has a higher value, then current state is a local maxima

```
function Hill-Climbing(problem) returns a state that is a local maxima
  current <-- initial-state
  loop:
     neighbor <-- highest-valued successor of current
     if neighbor.value <= current.value then return current
     current <-- neighbor
```

the code is simple, fast, and memory-efficient, and so can be implemented in many situations

hill-climbing is a kind of **greedy search**: it always chooses the next current node to be the one that increases its objective function the most

if more than one successor is tied for the highest-valued successor, then most hill-climbing implementations choose the next current state at random

- if many successors tie for the highest-value, then the agent may be on a plateau, which mean it will wander around randomly until it hits an edge

there are many variations on basic hill-climbing, e.g.:

- **stochastic hill-climbing** chooses at random from among the uphill moves, possible giving a greater chance to moves that are steeper; we note that most deep-learning neural nets uses a version of stochastic hill-climbing to do their learning

- **first-choice hill-climbing** generates successors at random, and stopping as soon as it finds one that has a higher value than the current node

- random-restart hill-climbing

   

  does a series of hill-climbing searches starting from randomly chosen initial states; when the agent gets to a local maxima, it re-starts at a randomly chosen start point

  - this has can be a very effective strategy for some problems, e.g. the n-queens problem for n=3 million can be solved in under a minute by a random-start search

in practice, it can be hard to find the best variation of hill-climbing to use for a particular problem, and so often a lot of experimentation is needed

## Simulate Annealing

basic hill-climbing never makes downward moves, i.e. it will never choose a successor node with a value lower than the parent node if it can avoid it

- that’s why it stops when it reaches a local maxima

in metallurgy, **annealing** is the process of slowly cooling down metal to harden it; quickly cooling metal can result in brittleness that makes it weaker and easy to shatter

**simulated annealing** is a search algorithm inspired by this process

simulated annealing works by choosing a successor at random; if that successor has a lower value, then it is accepted; but if the successor has a higher value, then there is some probability, based on a changing temperature T, that the higher value will be accepted

the temperature T starts out high (hot), and decreases as the algorithm continues

the higher T is, the more likely simulated annealing will choose a downward step

here’s pseudocode for simulated annealing; note that `schedule` is a function that maps the time `t` into a temperature `T`

```
function Simulated_Annealing(problem, schedule) returns solution state
  current <-- initial-state
  for t = 1 to infinity do:
    T <-- schedule(t)
    if T == 0, then return current
    next <-- randomly selected successor of current
    dE <-- next.Value - current.Value
    if dE > 0 then
      current <-- next
    else
      current <-- next with probability e^{dE/T}
```

## Local Beam Search

basic local search stores only *one* state, and chooses among the successors of that one state

**local beam search** keeps track of kk states

first it generates kk random states

then it generates the successors of those kk states; if any of the successors is a goal, then the algorithms stops

otherwise, it picks the kk best successors for the next step

**stochastic local beam search** is a variation of local beam search that chooses the kk successors at random, with the probability of choosing a particular successor proportional to the value of the successor

- i.e. the higher the value of a node, the more likely it will be chosen

## Genetic Algorithms

a **genetic algorithm** is a variant of local beam search where the next state is generated by *combining* two parent states instead of modifying a single state

it tries to mimic the process of evolution and genetics in an algorithmic way

like local beam search, genetic algorithms use a collection of kk states

to generate the next collection of states, pairs of states are chosen in a randomly weighted way (i.e. the better states have a proportionally higher chance of being chosen), and then pairs are somehow combined to create a new state

- the process of combining is like breeding, and the resulting state contains information from both its parent states

for example, suppose we represent states of a search problem as bit strings of size 20

then given two 20-bit strings representing states, one way to combine them is to use **cross-over**, e.g. create a new 20-bit child state that consists of the first 10 bits of its first parent, and the last 10 bits of its second parent

another common operation is genetic algorithms is **mutation**, e.g. randomly modifying a part of the state with the hope that some mutations will result in useful new states

genetic algorithms are popular in some communities, but a *lot* of work is typically required to find a good set of parameters for a genetic algorithm to work well

- what size of kk?
- how should states be combined?
  - many, many different ways have been proposed!
- how frequently should mutations occur?

if these parameters are not chosen well, then genetic algorithms can perform quite poorly, e.g. as little more than expensive versions of hill-climbing

no doubt part of the appeal of genetic algorithms is that they have a pleasing connection to evolution and genetics, something that many people think must surely be a good thing since we know that those processes have produced people!

plus, tinkering with all the different aspects of genetic algorithm can be fun

but in general, it’s hard to recommend them over other, simpler, variations of hill-climbing

## Rest of the Chapter

in this course we won’t cover any of the topics after genetic algorithms

we encourage you to browse through them if you are curious — there are many interesting and useful topics in the remainder of this chapter!
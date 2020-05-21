# Agents

**Agent** 指能自主活动的软件或硬件实体。（通常翻译为**智能体**）

## Agent Architecture (Agent体系结构)

our textbook outlines an **agent-oriented** perspective on AI, which can be diagrammed like this:

```
  Agent                                                                   Environment
+----------------------------------------------+                      +-------------------+
|                                              |                      |                   |
|                                              |   Percepts           |                   |
|                   Sensors <--------------------------------------------+                |
|                      |                       |                      |                   |
|                      |                       |                      |                   |
|                      |                       |                      |                   |
|                      |                       |                      |                   |
|              +-------v--------+              |                      |                   |
|              |                |              |                      |                   |
|              |                |              |                      |                   |
|              |                |              |                      |                   |
|              |       ?        |              |                      |                   |
|              |                |              |                      |                   |
|              |                |              |                      |                   |
|              |                |              |                      |                   |
|              |                |              |                      |                   |
|              +-------+--------+              |                      |                   |
|                      |                       |                      |                   |
|                      |                       |                      |                   |
|                      |                       |                      |                   |
|                      v                       |    Actions           |                   |
|                   Actuators +------------------------------------------>                |
|                                              |                      |                   |
|                                              |                      |                   |
+----------------------------------------------+                      +-------------------+
```

the idea is that the agent senses the environment, and then, after some thinking, uses its actuators(执行器) to modify the environment

- on a robot, actuators would be things like grippers(手爪), wheels, a horn(喇叭) — anything that could change the state of the environment
- for this course, we will usually have little to say about actuators, and will usually assume that changing the environment can be done accurately and easily
  - these are hardware thing, which usually considered by engineers.
  - we deal with software stuff.
- but for real-life robots, where actuators are a significant part of its interaction, much more care would need to be taken, e.g. it's possible that an actuator could *fail* and not change the environment correctly
  - e.g. a robot trying to pick up a cup of tea might accidentally knock over the teapot; or the robot might not grasp(抓紧) the cup firmly enough and it could slip out of the robot's grasp (perhaps even without the robot knowing it has dropped the cup!); or the robot might grasp the cup *too* firmly and shatter(捏碎) the cup.

The box inside the agent is the software programmers write. 

* it's a black-box takes in percepts, and output actions. 
* we have to write programs make those actions rational and interesting.

(Human also be considered an agent. We perceive the world and change the world via our action based on those perceptions.)

a **percept(认知)** is an agent's perceptual(感知的) input at any point in time

- a percept could come from a camera, voice, sonar(声呐), a text file, a bit stream, etc.
- most computers have a clock, on every tick of the internal clock, agents do something. Over time, the agent generate a *percept sequence*.

an agent's **percept sequence** is the sequence of everything it has perceived.

- in general, an agent's choice of actions can depend upon its entire percept history (but on no percepts from the future)
- the percept sequence is not a combination of all possible perceivable environments, but a series of single possible perceivable environments. 
- can think of it this way: the world around us is changing, in any time step we can look at around us and what we see is a partial view of the world in that exact time. The series of our observations is our percept sequence. 

### two-location vacuum-cleaner

e.g. the two-location vacuum-cleaner(吸尘器) world in Figure 2.2 of the text is useful

- there are two adjacent locations, A and B, connect like this:

  ```
  +----------------------------+
  |A            |B             |
  |             |              |
  |             |              |
  |             |              |
  |             |              |
  |             |              |
  +-------------+--------------+
  ```

- the vacuum is in either location A, or location B

- a location is either clean or dirty

- the vacuum agent can perform these actions: move left, move right, suck up dirt, or do nothing (which is not really an action, but it's often useful to have an explicit symbol meaning no action is done)

- the vacuum agent can perceive two different things:

  - it's location, whether it's at A or B
  - whether its current location is clean or dirty

  exactly *how* it does this perceiving we often don't need to worry about; maybe it uses a camera, or a map (for the location), or a special dirt sensor , etc.

- [A, Clean] is an example of a percept for this agent: it perceives that it is in location A, and location A is clean

- [B, Dirty] is another percept, meaning the agent perceives that it is in location B and location B is dirty

- it is quite possible that the agent's perceptions could be wrong — it might have faulty or inaccurate sensors

  - this is an important problem, but we will often ignore it, since the problems we deal with are often difficult enough already

- a percept sequence for this agent might be this: [[A, Dirty], [A, Clean], [B, Clean]]

  - this percept sequence corresponds to the agent starting in location A, cleaning up the dirt in that location, and then moving to location B

- a simple program for this agent might be something like this:

  > loop forever:
  >
  > > If most recent percept is [A, Clean], then move-right
  > >
  > > If most recent percept is [A, Dirty], then suck-up-dirt
  > >
  > > If most recent percept is [B, Clean], then move-left
  > >
  > > If most recent percept is [B, Dirty], then suck-up-dirt

  this particular program only takes into account the most recent percept, and so does not need to keep track of any history

  * it does not contain a memory.

## Rational Agents

what does it mean for an agent to be **rational**?

intuitively, it means that the agent always does “the right thing”

what is the “right thing”?

we will generally use a **performance measure** on a sequence of environmental states; the better the performance according to this measure, the more rational the agent

e.g. one possible performance measure for the vacuum-cleaning agent would be that there are as few dirty squares as possible

e.g. another possible performance measure for the vacuum-cleaning agent would be to maximize the amount of dirt it picks up over time

- but beware: for this performance measure, a "clever" agent might realize that it could clean up all the dirt, then dump it out, clean it up again, dump it out(倒出来), etc.
- if the agent dump out dirt on the middle of the floor, then it does the "wrong thing".

## (记)Definition of a Rational Agent 

a rational agent needs:

- a performance measure that defines its criterion(准则) for success
- some prior knowledge of the environment
- to know the actions it can perform
- its percept sequence to date

so we can define a **rational agent** as follows:

> For each possible percept sequence, a **rational agent** should select an action that is expected to maximize its performance measure, given the evidence provided by the percept-sequence and whatever built-in knowledge the agent has.

**memorize this definition!**

(human defines the performance measure, not the agent. eg. for a self-driving car, the measure may be as least as people it running on. The robots even don't know the performance measurement.)

(The performance measure of a agent is tested by functions, which give a score for the performance.)

notice that this definition implies we can't necessarily tell if an agent is rational just by looking at its program — we must take into account the relevant performance measure.

also, different agents working on the same problem in the same environment with the same percept sequence could behave differently due to their built-in knowledge.

also, what is the most rational thing to do might not be the *best* thing to do, in the sense that the agent may have incomplete information about the environment.

- a poker-playing agent can't win all the time, because it doesn't know what cards the players will be dealt
- but it can still act rationally, by making the best decision give the information it has at any point in the game

also, if its actions allow it to do so, an agent might do **information-gathering actions** to learn more about the environment

- a robot that crosses the street ought to look both ways before crossing: looking both ways is an information-gathering action
- a poker-playing agent might purposely play a hand in a crazy-seeming way to see how other players react, remembering what they learned for later

also, we usually want our agents to be **autonomous**, i.e. we want them to operate on their own without a lot of prior information or direct guidance from their designers

autonomy requires learning, e.g. we'd like to be able to put a vacuum-cleaning robot in any environment without also having to give it a map of the environment

- so we would expect an autonomous vacuum-cleaning robot to not only keep things clean, but intelligently navigate its way around the environment
- if you are familiar with Roomba vacuum-cleaning robots, then you know that it is possible to do such things!

in general, we usually expect rational agents to deal with partial and unknown information, and to learn new behaviors when necessary

## Environments

the task environment in which an agent is working can have a big impact

the **PEAS** model can be a helpful way of describing task environments; a good description of a task environment must specify the:

- Performance measure
- Environment
- Actuators
- Sensors

e.g. a taxi-driving agent

- **performance measure**: safety, speed, legality(合法性), passenger comfort, profit
- **environment**: roads, including other traffic, pedestrians(行人), weather conditions
- **actuators**: steering(方向盘), breaks, accelerator, turn signals, horn, lights
- **sensors**: camera, sonar, speedometer(速度计), odometer(里程表), GPS, engine sensors

e.g. a poker-playing web agent

- **performance measure**: profit, fun for human players
- **environment**: online poker on the web
- **actuators**: API for placing bets(打赌), chatting, etc.
- **sensors**: API for checking state of game (e.g. size of pot, other players visible cards), etc.

e.g. a poker-playing robot

- **performance measure**: profit, fun for human players, energy consumption, safety, maintenance
- **environment**: home game table
- **actuators**: hand for holding cards, placing bets, facial expressions, sounds, voice for asking questions
- **sensors**: camera for seeing other cards, camera for facial recognition (to help guess if player has a weak/strong hand), voice recognition for listening to questions

e.g. medical diagnosis(诊断) agent (Fig 2.5)

- **performance measure**: patient health; costs
- **environment**: patient, hospital, staff
- **actuators**: display of questions, tests, diagnoses, treatments(治疗), referrals(转诊病人)
- **sensors**: keyboard entry of symptoms(症状), findings, patients answers

## Properties of Environments

**fully observable** vs. **partially observable**

- if an agents sensors give it access to the *complete environment* at each point in time, we say the environment is **fully observable**
  - in a fully observable environment, an agent need not store the state since its sensors tell it everything it needs to know
- if *only a part of the environment* can be sensed at each point in time, the environment is said to be **partially observable**
  - this is the more realistic case, since often impartial, incomplete, or inaccurate information is an ordinary part of the environment

**deterministic(确定性的)** vs. **stochastic(随机的)**

- if the next state of the environment is completely determined by the previous state sequence, and the action of the agent, then we say the environment is **deterministic**; otherwise, we say the environment is **stochastic**
  - note that a partially observable environment could *appear* to an agent to be stochastic, even though in fact it is deterministic
  - most practical environments are so complex that they are treated as if they are stochastic

**static** vs. **dynamic**

- if the environment can change while the agent is thinking, then we say the environment is **dynamic**; otherwise, it is **static**
- dynamic environments are usually more challenging to deal with, because they put time-pressure on the agent's thinking: if a decision takes too long, it may no longer be valid
  - e.g. a self-driving car must decide to hit the breaks or not very quickly in some situations!

**discrete** vs. **continuous**

- if time is handled in discrete sequential steps (like the discrete ticking of a CPU), then the environment is said to be **discrete**
- if instead time is handled as a continuous stream (as in physics), then the environment is said to be **continuous**
- discrete math and continuous math is quite different!

**known** vs. **unknown**

- if the outcomes of all actions are known ahead of time by the agent, then we say the environment is **known**
- if instead the outcomes of some actions are not known ahead of time, meaning the agent must test things out to find out what will happen, then the environment is said to be **unknown**

## The Structure of Agents

a large part of AI research is concerned with the structure of agent programs, and here we will consider a few high-level architectures for agents

## Table-driven Agents

this is a **look-up table agent** that uses a (giant!) table of actions indexed by percept-sequences

given any percept sequence, the agent simply "looks up" in the table the action that it ought to do

this can be quite effective in simple situations, but is completely unreasonable in even moderately complicated situations

to see how unreasonable table-driven agents are, we can do some simple calculations

let P be the set of different possible percepts, and T the “lifetime” of the agent, i.e. the length of time it exists

then the total number of percept sequences is exponential, i.e. $\sum_{i=1}^T |P|^t$.

- e.g. a self-driving taxi that gets 27 megabytes of input per second from a camera sensor would need a look-up table with 10250,000,000,00010250,000,000,000 entries, for one hour of driving
- there are only about 10801080 atoms in the observable universe, so such a large table could not even be stored
- but even if we could create such a huge table, it would take a huge amount of time to create: how could the entries be filled-in a reasonable amount of time? how would figure out for each percept sequence what the correct action would be?

## Simple Reflex Agents

a **simple reflex agent** decides what to do based solely on the current percept, and ignores all previous percepts

a simple reflex agent thus does not need to store any state — it just reacts to whatever it currently “sees”

typically, simple reflex agents may consist of **condition-action rules**

- also known as **situation-action rules**, or **if-then rules**, or **productions**

e.g. if the-car-in-front-is-breaking, then apply-breaks

pro:

- simple programs!

con:

- single percepts are simply not enough in all situations to be able to do the right thing
  - e.g. the decision of whether or not to believe that a car driving in front of you is breaking depends one more than just seeing if their break lights are on
    - what if the break lights are broken?
    - what if some light other than the break-light also goes on near the break light? (thus resulting in unnecessary breaking)
    - what if a police officer is waving you around the car?
- can get stuck in infinite loops (e.g. see vacuum cleaner example on top of p. 50)
  - randomness can be used to help break out of such loops
- e.g. siri

## Model-based Reflex Agents

**model-based reflex agents** save information about the external world using internal state

e.g. a vacuuming agent might keep an internal map of the environment it has visited so far, event the parts it can't currently sense

such agents can act far more intelligently, since they are not limited to what they can currently perceive

it may need some memory.

a model-based agent could use its internal model to *simulate* actions before doing them, to estimate what might happen (it can plan ahead a little bit)

- this is very useful! for example, people don't have to actually drive their car off a cliff(跌下悬崖) to realize that would be a very bad thing to do
- but simulating an environments is not easy, since the agent will normally have incomplete information about the environment, and the simulation is usually only be an approximation of reality

## Goal-based Agents

**goals** are descriptions of desirable states

e.g. if you come to a fork in the road (分岔路口) where you can go either left or right, how do you choose which way to go? hopefully you have a goal about where you want to go that helps you decide

in general, achieving goals is can be quite tricky, and sometimes long sequences of carefully planned actions are needed

e.g. the goal of baking a cake; you need to at least:

- have a recipe for the cake
- have all the ingredients for the cake
  - if you are missing some ingredients, then you have the sub-goal of getting those ingredients
- have all the pots, pans, measuring cups, etc. for the cake
- you must follow the recipe for mixing and baking the ingredients
- your recipe may not give exact measurements, and may include instructions like "season to taste (按照你的口味)"
  - which suggests the agent must be able to taste the cake
- at any point in this process, unexpected things might happen that the agent should try to “recover” from, e.g.
  - the power could go out
  - someone could come to the door and interrupt you

in AI, the sub-fields of **search** and **planning** are about this sort of problem

## Utility Agents

**utility agents** are goal-based agents that also take into account the quality of the action sequences used to achieve goals

e.g. there might be three ways to drive from your house to the airport: a fast but bumpy way, a slow but smooth way, and a way that is fast, smooth, but noisy

- all three ways achieve the goal of getting to the airport
- but some ways are better than others, depending upon the situation
- so we often add a **utility** function that is a measure of the agent's "happiness" with a particular sequence of actions
- an agent will usually want to achieve its goals in a way that maximizes its *overall* utility
- an agent's utility function is usually an internal version of the environments performance measure
- if the environment contains randomness, then the agent will usually try to maximize its **expected utility**, since in a random environment it can't always be sure of the outcomes of its actions

**utility-maximizing agents** are the goal of much AI research

it may sound simple, but its hard to come up with good utility functions in complex environments, and computational complexity concerns are usually an issue (i.e. what if computing maximum utility requires exponential time?)

## Learning Agents

while it is possible to program intelligent agents by hands, that can be extremely difficulty for many problems of interest to AI

e.g. suppose you a program that recognizes *hand-written* numbers on paper

- there are thousands of small and subtle variations in how people write numbers, and it is extremely difficult to say exactly what the rules are for, say, distinguishing between the number 4 and the number 7
- so in practice, the most successful hand-writing recognition programs have been *learning* programs that *learn* how to recognize numbers by from looking at thousands and thousands of training examples

in general, a learning agent is able to modify its various components in ways that improve its overall performance

any of the above kinds of agents could also have a learning component, and in practice learning has been one of the most successful areas of AI
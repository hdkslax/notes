# Introduction to Artificial Intelligence (AI)

## What is AI?

* AI is the study of **intelligence**, particularly intelligent machines

* AI is mainly interested in understanding and creating things that think, or act, rationally (or intelligently)
  * So far success has been for only on specific problems.
  * e.g. we want self-driving cars to “do the right thing” in all situations, and this seems to require acting and thinking rationally

* humans are a special case: so far, they are the only know things that are capable of *general* rational thought and action

* so AI is often compared to human performance, and we will often take humans as inspiration for how computers might solve similar problems
  * e.g. if a computer can do X as well as a human, then the computer is intelligent with respect to X.
  * Be careful: humans don't do everything well, so a computer achieving human-level performance on, say, multiplying 5-digit numbers, would mean your computer isn't very good. 



## The Turing Test

determining if something is truly intelligent is a tricky problem

famously, in the 1950s computer scientist [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) proposed what is now called [the Turing Test](https://en.wikipedia.org/wiki/Turing_test)

[the Turing Test](https://en.wikipedia.org/wiki/Turing_test) is a thought experiment (思想实验): a computer and a human questioner have a conversation through a computer terminal, such that the questioner has no idea if they are conversing with a computer or a real human; the computers goal is to make the questioner think they are human.

[the Turing Test](https://en.wikipedia.org/wiki/Turing_test) is open-ended: the questioner can ask anything they like, and may judge the computers response however they like

of course, some questions are human-centric (以人为本的), e.g. the questioner might ask “What was your mother’s name?”, or “How many toes do you have on your left foot?” which would seem to require that the computer lie

but such details aside (除了这些细节), it is interesting to think about the sorts of things a program that could pass [the Turing Test](https://en.wikipedia.org/wiki/Turing_test) would need to be able to do; it would have to:

* understand, and generate, natural language (natural language processing, NLP)
* store and retrieve the things it knows and hears (knowledge representation, KR)
* used its stored information to infer new, and maybe novel, conclusions (automated reasoning 自动推理)
* learn about new circumstances, or find new patterns (machine learning, ML)

all of these are significant and challenging parts of AI research today, and the general consensus (共识) is that we are nowhere near being able to make a program that could pass [the Turing Test](https://en.wikipedia.org/wiki/Turing_test) (我们离开发能够通过Turing Test的程序还差得远)

in practice, [the Turing Test](https://en.wikipedia.org/wiki/Turing_test) has had little direct impact on AI research, since it is too complex, and researchers have preferred to focus on the underlying principles of AI

yet you will often hear mention of [the Turing Test](https://en.wikipedia.org/wiki/Turing_test) in movies, books, and the popular press; it is certainly useful for inspiring people, but it has not been a direct topic of much AI research — it’s just too much to ask (yet!)

## Thinking Humanly: Cognitive Science 认知科学

**cognitive science** is its own discipline, although it is closely related to AI

cognitive science is essentially interested in how *humans* think, and is interested in models of cognition, intelligence, rational behaviour, etc. that models how humans might do such things

the goal of cognitive science is to explain how *humans* think, and if that helps further the cause of AI in general, then that’s a bonus.

in contrast, the “computer science” approach to AI that we will be taking is more engineering-oriented: depending upon the problem we are trying to solve, mimicking how humans solve that problem may, or may not, be a good idea

* we will use any idea or approach that gives good results!
* it won’t matter to us if a good approach to solving a problem is not the way a human would do it

## Rational Agents 理性主体

a useful perspective on AI is that it is interested in creating and understanding **rational agents**

an agent is something that “acts” in the world, and by rational we mean “doing the right thing”

e.g. we want self-driving cars to be rational agents; we also Alexa and Siri and other such “intelligent assistants” to be rational agents

* Alexa 是 Amazon 推出的一款智能助理

a human is a rational agent, and a major question in AI is if anything other than a human is a rational agent

* many AI researchers think the answer to this question is obviously “yes”, although we don’t yet have any examples of rational agents yet other than humans

* in principle, most researchers believe there is nothing magical about human brains: a brain is just “meat that thinks”, and in principle a computer simulation of a brain would also think, and thus be a rational agent

* some people argue that computers don’t have emotions, but emotions don’t seem to be a requirement for rational thought; however, some researchers have certainly studied them in depth, and they can be simulated if necessary!

* some people (passionately!) argue that *consciousness* is important, and suggest that while maybe computers may one day be truly intelligent, they will never be truly conscious

  * e.g. as an analogy, if you made a computer simulation of water, it will never truly be wet, no matter how good the simulation is
* but a major problem with consciousness is that it is not clearly defined, and different scientists take it to mean different things
  * it is just not clear how consciousness helps with intelligence, and so we will have little to say about it in this course

## Major Approaches and Inspirations in AI

* **logic**: encode rationality as logical rules 将合理性编码为逻辑规则

* **mathematics**: use ideas and techniques from math, like probability theory, to model rationality

* **computer science**: computer science is the study of algorithms, and most people believe that rational agents use algorithms

* **economics**: use notions like utility, and maximizing payoffs; in particular, the fields of decision theory and game theory are precisely about making rational decisions in the face of real-world complexities (which mathematics and logic often abstract away)
* some of the most well-known early work in AI was done by researchers coming from economics: Herbert Simon and Allen Newell
  
* **neuroscience** 神经科学: study the human brain as a biological object, and try to simulate it

* **psychology**: how do humans (and animals) act? this is at a higher-level than neuroscience, and is where ideas like “belief”, “intention”, and “perception”; even the term “rational” is a psychological term

* **hardware engineering**: design a computer to be intelligent by carefully studying the actual components used to make computers; robotics is part of this — some researchers believe that intelligence needs to be *embodied* in something like a robot to truly rational
* it’s interesting to note that a significant impact in the recent success in “deep” neural networks was figuring out ways to increase the performance of basic neural network algorithms using things like GPUs, and other special-purpose hardware
  
* **linguistics**: how are language and thought related? human language is a very important part of their rationality, and the careful study of language has brought a lot of insight into understanding

we can’t cover all these areas of influence, and so we will focus on the areas closest to computer science

## A Brief History of AI

| Year           | event                                                        |
| -------------- | ------------------------------------------------------------ |
| 1943           | **Walter Pitts** and **Warren McCullock** propose first "artificial neuron"networks; here is [`a copy of their original paper`](https://www2.cs.sfu.ca/CourseCentral/310/tjd/_downloads/McCulloch.and.Pitts.pdf). 直到2010年才实现，中间隔了70年！ |
| 1948-1950      | **Alan Turing** (father of AI) wrote probably the first computer chess program (although never got it running on a computer) |
| 1950           | **Alan Turing** proposed the Turing Test as a test of general-purpose computer intelligence |
|                | **Alan Turing** also well known for his work in foundational computer science (Turing machines), and helping to crack the German Enigma code during WW2. |
| 1951           | **Marvin Minsky** created he first randomly wired neural net learning machine (hardware) |
| 1955           | **John McCarthy** coined the term Artificial intelligence.   |
| 1956           | Dartmouth 2-month summer workshop, where many of the early pioneers of AI met; their ideas approaches came to dominate AI for decades afterwards |
| 1958           | **John McCarthy** developed the LISP programming language (used in many early symbolic AI programs), to help implement AI-related programs that needed to do symbolic processing (which was very difficult to do in other languages of the day). He involved in much foundational AI research, in particular applications of logic. |
| 1960s          | some success in *microworlds*, i.e. problem-solving in carefully limited domains |
| 1965 - onwards | Edward Feigenbaum helped create the influential expert system Dendral (for identifying unknown organic molecules), and other expert systems. |
|                | Edward Feigenbaum proponent of heuristics and rule-based AI  |
| 1966-1973      | (“a dose of reality”) initial optimism about the pace of AI decreased, when, for example, the intractability of many of the problems they were trying to solve was understood (thanks to computer science!); many early AI programs were doing simple syntactic manipulations, and clearly had no real understanding of their domains |
| **1969**       | **Marvin Minsky** and **Seymour Papert** published the book *Perceptrons* that showed fundamental limitations of early neural nets, and they famously proved that the simple neural-network learning algorithms that were popular at the time were not powerful enough to learn many extremely simple functions |
| 1969           | **Marvin Minsky** along with John McCarthy, one of the major leaders of early AI work. |
| 1970s          | (“knowledge-based systems”): many interesting approaches to storing and processing “knowledge” were explored, including expert systems (which were once thought to be the crowning success of AI) |
| 1978-onwards   | Geoffrey Hinton, one of a small group of enthusiastic neural net researchers. Involved in a lot of fundamental modern work on neural nets. |
| 1980s          | Edward Feigenbaum expert-system shells for adding rule-based AI to programs were available. |
| 1986 onwards   | neural networks regained popularity thanks to new, and better, methods for learning with them; work has progressed since this time until now, where so-called “deep neural nets” are considered by many to be the pinnacle of AI achievement, able to solve useful hard problems like image recognition |
| 2000 onwards   | large data sets started to become available (thanks to the computerization of most data, including the web), and so this inspired a lot more interest in machine-learning techniques |
| 2011 - onwards | major success with neural net model, achieving best performance in applications such as image recognition and speech understanding. |

### Examples of heuristic rules from the MYCIN expert system

(have to write rules by hand)

```algorithm
RULE037
IF: 1) The identity of the organism is not known with certainty, and 
	2) The stain of the organism is gramneg, and 
	3) The morphology of the organism is rod, and 
	4) The aerobicity of the organism is aerobic
THEN: There is strongly suggestive evidence (.8) that the class of the organism is enterobacteriaceae.
```

```algorithm
RULE145
IF: 1) The therapy under consideration is one of: cephalothin clindamycin erythromycin lincomycin vancomycin, and 
	2) Meningitis is an infectious disease diagnosis for the patient
THEN: It is definite (1) the therapy under consideration is not a potential therapy for use against the organism. 
```

```
RULE060
IF: The identity of the organism is bacteroides
THEN: I recommend therapy chosen from among the following frugs:
		1 - clindamycin		(.99)
		2 - chloramphenicol	(.99)
		3 - erythromycin	(.57)
		4 - tetracycline	(.28)
		5 - carbenicillin	(.27)
```



#### Video

<video><source src="https://youtu.be/18SXA-G2peY" type="video/mp4"></source></video>

* The "strong AI" and "weak AI" he used is created by him, no other people using them. 
* He doesn't distinguish between hardware and software. But CS people know that anything is a software could just be easily to put into a hardware, verse vice. 
* You can simulate a mind just like you can simulate water in a video game. But it never actually been a mind.
* He said the person (the CPU) is not a mind, it's true, the program is simulating the mind, not CPU.
* He made a mistake here. He looked at the wrong thing. He's confusing the program with CPU. He said the CPU does not understand anything, it never does. But the program, the CPU and the database as a whole system understanding. 
  * e.g., A engine in a car, the engine itself only cannot go anywhere. Therefore the car cannot move. He's mistake is like this.
* Mental content 
  * promise 1 - mind has at least two things. A mind must be manipulate symbols, and it must have mental content. 
  * promise 2 - computers can only manipulate symbols. Computer don't have mental content.
  * Therefore, computers are not mental.
  * (But why the promises are true? He didn't provide evidence, he think they are obvious.)


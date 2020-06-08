# preview

- area 
  - The area problem is the central problem in the branch of calculus called integral calculus.
- tangent line
  - The tangent problem has given rise to the branch of calculus called differential calculus.
- the area problem and the tangent problem are inverse problems in a sense.
- velocity of a car 
- limit of a sequence
  - a sequence {a_n} is a set of numbers written in a definite order.
- sum of infinite series
- summary: we could define calculus as the part of mathematics that deals with limits.

## Functions & Models

### Functions & Models

- functions - the fundamental objects that we deal with in calculus are functions.

  - 4种表示函数的方法

    - verbally 自然语言描述

    - numerically 表格表示

    - visually 图像

    - algebraically 公式

  - 判断一个图像是否为函数图像 The vertical line test
    - A curve in the xy-plane is the graph of a function of x if and only if no vertical line intersects the curve more than once.

  - 种类
    - piecewise defined functions
      - step functions

  - 奇偶性

    - 奇函数 - 关于原点对称 f(-x) = -f(x)

    - 偶函数 - 关于y轴对称 f(-x) = f(x)

  - 增减性 x1<x2, if f(x1)<f(x2) 增； if f(x1)>f(x2) 减

### mathematical model 

- a mathematical model is a mathematical description (often by means of a function or an equation) of a real-world phenomenon.

- the purpose of the model is to understand the phenomenon and perhaps to make predictions about future behavior.

- real-world problem -(formulate)-> Mathematical model -(solve)-> Mathematical conclusions -(interpret)-> real-world predictions -(test)-> real-world problem.

- a mathematical model is never a completely accurate representation of a physical situation - it is an idealization.

- 种类

  - Linear model
    - empirical model 经验模型 - if there is no physical law or principle to help us formulate a model, we construct an empirical model, which is based entirely on collected data.

  - polynomials

    - the domain of any polynomial is R.

    - quadratic function 二次函数

    - cubic function 三次函数

  - power function 

    - 幂函数 f(x) = x^n (n is a constant)

    - n 为正整数时，定义域是R

    - n为分数时，就是root function

    - n为-1时，是raciprocal function 反比例函数

  - rational functions 

    - a ratio of two polynomials f(x) = P(x) / Q(x)

    - domain consists of all values of x such that Q(x) ≠ 0

  - algebraic functions
    - if it can be constructed using algebraic operations (such as addition, subtraction, multiplication, division, and taking roots) starting with polynomials. 

  - trigonometric functions

  - exponential functions 

    - 指数函数

    - f(x) = b^x 

    - 对比power functions: f(x) = x^n

    - domain: R

    - range: (0, +∞)

  - logarithmic functions

    - domain: (0, +∞)

    - range: R

- family of function
  - a collection of functions whose equations are related. 

### Transformations of functions

- 平移 transformation 
  - 上加下减

- 伸缩 stretching

  - y=f(x) -> y=cf(x) 垂直拉伸 （变长）

  - y=f(x) -> y=1/c f(x) 垂直压缩 （变短）

  - y=f(x) -> y=f(cx) 水平拉伸（变宽）

  - y=f(x) -> y=f(1/c x) 水平压缩（变瘦）

- 对称 reflecting 

  - 关于x轴对称：y=f(x) -> y=-f(x)

  - 关于y轴对称：y=f(x) -> y=f(-x)

- combinations of functions

  - (f+g)(x) = f(x) + g(x)

  - (f-g)(x) = f(x) - g(x)

  - (fg) (x) = f(x)g(x)

  - (f/g)(x) = f(x)/g(x)

  - (f○g)(x) = f(g(x))
    - in general, f○g ≠ g○f

- Exponential functions

  - f(x) = b^x , b is a positive constant

  - if x = positive integer, b^n = b·b·b ····· b 

  - if x = 0, b ^ 0 = 1

  - if x = negative integer, b^-n = 1/(b^n)

  - if x = p/q, a rational number, b^x = b ^ (p/q) 

  - if x = irrational numbers, b^x就是填补了上述情况没有覆盖到的点，从而保证了图像是连续的

  - 性质

    - all exponential function passes through (0,1) since b^0 = 1 for b ≠ 0. 

    - b越大，图像增长越快，在y轴左边时在下方，在y轴右边时在上方。

  - 公式

    - b^(x+y) = (b^x)(b^y)

    - b^(x-y) = (b^x)/(b^y)

    - (b^x)^y = b^(xy)

    - (ab)^x = (a^x)(b^x)

  - The number e
    - The natural exponential function y = e^x 在点(0,1)处的切线斜率 m=1

- Logarithmic functions

  - y = log_b(x) <=> b^y = x

  - domain (0, ∞)

  - range R

  - laws of logarithms

    - If x and y are positive numbers, then 

      - log_b(xy) = log_b(x) + log_b(y)

      - log_b(x/y) = log_b(x) - log_b(y)

      - log_b(x^r) = rlog_b(x) (where r is any real number)

      - ln(e^x) = x (x∈R)

      - e^(lnx) = x (x > 0)

      - lne=1

      - change of base formula: log_b(x) = ln(x)/lnb

  - Although lnx is an increasing function, it grows very slowly when x>1. In fact, lnx grows more slowly than any positive power of x. (e.g. sqrt(x) < ln x)

  - 

- Inverse function

  - ono-to-one function: if the function never takes on the same value twice;
    - f(x1) ≠ f(x2) whenever x1 ≠ x2

  - Horizontal Line Test: a function is one-to-one if and only if no horizontal line intersectes its graph more than once.

  - inverse function: let f be a one-to-one function with domain A and range B. Then its inverse function f^(-1) (y) = x <=> f(x) = y for any y in B. 

    - domain of f^(-1) = range of f

    - range of f^(-1) = domain of f

    - cancellation equation
      - f^(-1)(f(x)) = x 

  - How to find the inverse function of a one-to-one function f

    - write y = f(x)

    - solve this equation for x in terms of y (if possible)

    - to express f^(-1) as a function of x, interchange x and y. 

    - the resulting equation is y = f^(-1)(x).

  - The graph of f^(-1) is obtained by reflecting the graph of f about the line y = x.

  - 三角函数的inverse就是反三角函数 (arcsin之类的)
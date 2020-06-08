# OOP Design Reference Parameters, Constant Modifiers, this Pointer and Operator Overloading 

### Design of Classes

以有理数class为例：

* rational number = $a/b$  ($b \ne 0$)
* 一般会有如下几个member functions:
  * constructors
  * getters
  * setters
  * other member functions to work with the numerators and denominators of rational numbers

```c++
class RationalNumber {
    /*
    This class is designed to represent Rational Number objects.
    A rantional number is a number of the form a/b with integers 
    a and b such that b is different from 0.
    */
private:
    int a, b;
    
public:
    // Constructors
    RationalNumber();
    RationalNumber(int, int);
    
    // Getters
    int getNumerator();
    int getDenominator();
    
    // Setters 
    void setNumerator(int num);
    void setDenominator(int denom);
    
    // Additional member functions
    double toDouble();
    void standardize();
    void reduce();
    void print();
};

// member functions 的实现

// Constructors
RationalNumber::RationalNumber(){
    // As a default object, let us construct the rational number: 0/1
    a = 0;
    b = 1;
}

RationalNumber::RationalNumebr(int num, int denom){
    // If the denominator parameter is 0, ignore it and use 1
    a = num;
    b = denom != 0? denom : 1;
    
    // Now that the object is created, standardize and reduce it
    standardize();
    reduce();
}

// Getters
int RationalNumber::getNumerator(){
    return a;
}
int RationalNumber::getDenominator(){
    return b;
}

// Setters
void RationalNumber::setNumerator(int num){
    a = num;
    
    // Now that numerator of an existing object is modified, 
    // standardize it and reduce it
    standardize();
    reduce();
}
void RationalNumber::setDenominator(int denom){
    // If the denominator is 0, ignore it and use 1
    b = denom != 0? denom: 1;
    
    // Now that denominator of an existing object is modified, 
    // standardize it and reduce it
    standardize();
    reduce();
}

// Additional member functions 
double RationalNumber::toDouble(){
    return static_cast<double>(a) / b  // 讲a的数据类型从int转换为double
}
void RationalNumebr::standardize(){
    if (b<0){
        a *= -1;
        b *= -1;
    }
}
void RationalNumber::reduce(){
    if (a == 0){
        b = 1;
        return;
    } else {
        // Remember that the denominator is NEVER zero by design
        // Therefore here both numertor and denominator are non-zero
        int m = abs(a);
        int n = abs(b);
        int gcd = m < n? m:n;
        while (gcd > 0){
            if (m % gcd == 0 && n % gcd == 0)
                break;
            gcd--;
        }
        a /= gcd;
        b /= gcd;
    }
}
void RationalNumber::print(){
    cout << a << "/" << b;
}

int main() {
    // Test constructors
    RationalNumber r1, r2(-5, 6);
    RationalNumber *r3 = new RationalNumber(); // *r3是一个pointer, 必须用 new 来申请内存空间
    RationalNumber *r4; // r3, r4 在内存中被放到了heap上
    r4 = new RationalNumber(4, -6);
    
    // Test getters
    cout << "r1 numberator is " << r1.getNumerator() << endl;
    cout << "r3 denominator is " << r3->getDenomitor() << endl;
    
    // Test setters, standardize, reduce and print member functions
    r2.setDenominator(-10);
    cout << "r2 is now "; r2.print(); cout << endl;
    
    // Print all the objects
   	cout << "r1 = "; r1.print(); cout << endl;
    cout << "r2 = "; r2.print(); cout << endl;
    cout << "r3 = "; r3.print(); cout << endl;
    cout << "r4 = "; r4.print(); cout << endl;
    
    // Test toDouble member function
    cout << "In double format, r4 = " << r4->toDouble() << endl;
    
    // Delete objects created on heap
    delete r3;
    delete r4;
    
    return 0;
}

```

`static_cast\<type-id>(expression)`  - 将表达式`expression`的类型转换为`type-id`。类似于C语言中的强制转换`(double)a`



为了使代码更高效，参数应使用引用传递（pass by reference）

改动后的代码如下：

```c++
class RationalNumber{
    /*
    This class is designed to represent Rational Number objects. 
    A rational number is a number of the form a/b with integers 
    a and b such that b is defferent from 0.
    */
private:
    int a, b;
    
public:
    // Constructors
    RationalNumber();
    RationalNumber(int&, int&);
    
    // Getters
    int getNumerator();
    int getDenominator();
    
    // Setters 
    void setNumerator(int& num);
    void setDenominator(int& denom);
    
    // Additional member functions
    double toDouble();
    void standardize();
    void reduce();
    void print();
};
```


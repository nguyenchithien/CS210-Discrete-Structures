# Chapter 2 Extra Credit: Modulus

Using any language, create a program that will divide `a` by `b` and give the quotient `q` and remainder `r`...

## Steps

### Creating variables

1. Create the following **integer** variables: a, b, q, and r.
2. Create the following **float** or **double** variable: result.

### Getting user input

3. Display the program header, `"Program to divide a / b..."`.
4. Display `"Enter a: "`.
5. Get the user's input and store it in the `a` variable
6. Display `"Enter b: "`.
7. Get the user's input and store it in the `b` variable

### Calculating result

8. Do the operation `q = a / b`.
9. Do the operation `r = a % b`.
10. Do the operation `result = float(a) / float(b)` (in C++)

### Displaying result

Display the results like this:

```
Quotient: 2      Remainder: 1
Result (Fraction): 2+1/2
Result (Decimal): 2.5
```

Quotient is `q`, Remainder is `r`.

The result fraction is `q` + `r`/`b`. The C++ output will look like:

```c++
cout << "Result (Fraction): " << q << "+" << r << "/" << b << endl;
```

The result decimal is `result`.

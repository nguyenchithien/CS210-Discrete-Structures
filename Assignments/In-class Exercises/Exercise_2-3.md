Chapter 2.3 In-class Exercises

CS 210, Spring 2017

**Rules:** 

* In-class exercises are given each class period for every chapter.
* Work with your groupmate(s) on this exercise.
* You will keep your own work. Make sure your attendance is counted so you get credit for this assignment.
* We will share our work at the end of class

---

## Section 1: Review predicates

<blockquote>

A **Predicate** is a function *P(x)* that results in either a
*true* or *false* value when some input *x* is given.

**Example:**

*P(x)* is the predicate, *"x is greater than 10"*.

Whether the output of *P(x)* is true or false depends
on the input *x*. *P(2)* is false, but *P(11)* is true.
 
</blockquote>

### Exercise 1

For the given predicates, write the results for each of the inputs specified.
The solution should be either *true* or *false*.

a. *P(n)* is *"n is an even integer."*

1. *P(1) =*
1. *P(2) =*
1. *P(3) =*
1. *P(2m) =*
1. *P(2m+1) =*

b. *P(n)* is *"n<sup>2</sup> + 1 is prime."*

1. *P(1) =*
1. *P(2) =*
1. *P(3) =*
1. *P(m-1) =*

---

## Section 2: Providing equivalence between a Recursive formula and a Closed formula

<blockquote>
Now we're getting into our heavier proofs. 
Chapters 2.3 and 2.4 have the main proofs that we are working on for this chapter. 
Once you learn the steps, they're not hard, 
but it can be difficult to keep them all straight. 
Make sure to get plenty of practice. 

The best way to illustrate how to prove a 
**recursive-closed formula equivalence**
is probably just to show an example with the steps highlighted. 

**Example:**

Show that the sequence defined by the recursive formula

*a<sub>k</sub> = a<sub>k-1</sub> + 4*, where *a<sub>1</sub> = 1*, for *k ≥ 2</sub>

is equivalently described by the closed formula *a<sub>n</sub> = 4n - 3*.

<table>

<tr>

<th> Step 1: </th>

<td>

**Check the results of a<sub>1</sub> for both the recursive and closed formula:**

* Recursive: *a<sub>1</sub> = 1* (Already provided)
* Closed: *a<sub>1</sub>* = 4(1) - 3 = 1

They match, so we can continue...

</td>

</tr>

<tr>
<th> Step 2: </th>
<td>

**Rewrite the recursive formula in terms of m:**

*a<sub>m</sub> = a<sub>m-1</sub> + 4*

</td>
</tr>

<tr>
<th> Step 3: </th>
<td>

**Find the equation for a<sub>m-1</sub> through the closed formula:**

* *a<sub>n</sub> = 4n-3*
* *a<sub>m-1</sub> = 4(m-1) - 3*
* *a<sub>m-1</sub> = 4m - 7*

</td>
</tr>

<tr>
<th> Step 4: </th>
<td>

**Plug a<sub>m-1</sub> into the recursive formula from step 2 and simplify:**

* *a<sub>m</sub> = a<sub>m-1</sub> + 4*
* *a<sub>m</sub> = (4m - 7) + 4*
* *a<sub>m</sub> = 4m - 3*

</td>
</tr>

<tr>
<th> PROOF: </th>
<td>

Our result *a<sub>m</sub> = 4m-3* and the closed formula
*a<sub>n</sub> = 4n-3* match, so the closed formula
and the recursive formula are equivalent.

</td>
</tr>

</table>

</blockquote>

### Exercise 2

Prove the following statement. Go through each step as in the example above,
and label each step as you work through it.

Show that the sequence defined by 
*b<sub>k</sub> = 4 · b<sub>k-1</sub> + 3*, 
with *b<sub>1</sub> = 3*
for *k ≥ 2*,
is equivalently described by 
*b<sub>n</sub> = 2<sup>2n</sup> - 1*.

Note: You may need an overview of exponent rules for this one!

<blockquote>

1. x<sup>a</sup> / x<sup>b</sup> = x<sup>a - b</sup>

2. x<sup>a</sup> · x<sup>b</sup> = x<sup>a+b</sup>

3. x<sup>4</sup> / x<sup>2</sup> = x<sup>2</sup> 

</blockquote>

### Exercise 3

Prove the following statement. Go through each step as in the example above.

Show that the sequence defined by 
*a<sub>n</sub> = a<sub>n-1</sub> + 2*
with *a<sub>1</sub> = 5*
for *n ≥ 2*,
is equivalently described by 
*a<sub>n</sub> = 2n + 3*.

### Exercise 4

Prove the following statement. Go through each step as in the example above.

Show that the sequence defined by 
*a<sub>k</sub> = 2 · a<sub>k-1</sub> + 1*
with *a<sub>1</sub> = 1*
for *k ≥ 2*,
is equivalently described by 
*a<sub>n</sub> = 2<sup>n</sup> - 1*.

--- 

## Section 3: Proving equivalence between a Summation and a Closed formula

<blockquote>
With a **summation-formula equivalence proof**, we also have a series of
steps to follow, and another example will help out more than anything.

**Example:**

Use induction to prove each of the following. As part of your proof,
write and verify each statement for at least *n = 1*, *n = 2*, *n = 3*,
and *n = 4*.

Proposition:

![sum](images/sum_1_to_n_small.png) *(2i - 1) = n<sup>2</sup>* for each *n ≥ 1*.

<table>

<tr>

<th> Step 1: </th>

<td>

**Check the results of a<sub>1</sub> for both the recursive and closed formula:**

* Recursive: *a<sub>1</sub> = 1* (Already provided)
* Closed: *a<sub>1</sub>* = 4(1) - 3 = 1

They match, so we can continue...

</td>

</tr>

<tr>
<th> Step 2: </th>
<td>

**Rewrite the recursive formula in terms of m:**

*a<sub>m</sub> = a<sub>m-1</sub> + 4*

</td>
</tr>

<tr>
<th> Step 3: </th>
<td>

**Find the equation for a<sub>m-1</sub> through the closed formula:**

* *a<sub>n</sub> = 4n-3*
* *a<sub>m-1</sub> = 4(m-1) - 3*
* *a<sub>m-1</sub> = 4m - 7*

</td>
</tr>

<tr>
<th> Step 4: </th>
<td>

**Plug a<sub>m-1</sub> into the recursive formula from step 2 and simplify:**

* *a<sub>m</sub> = a<sub>m-1</sub> + 4*
* *a<sub>m</sub> = (4m - 7) + 4*
* *a<sub>m</sub> = 4m - 3*

</td>
</tr>

<tr>
<th> PROOF: </th>
<td>

Our result *a<sub>m</sub> = 4m-3* and the closed formula
*a<sub>n</sub> = 4n-3* match, so the closed formula
and the recursive formula are equivalent.

</td>
</tr>

</table>

</blockquote>





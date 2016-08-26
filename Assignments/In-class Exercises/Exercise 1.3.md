# Exercise 1.3

Your Name:

Team Name:

---

#### Review

    ¬ = NOT (Negation)
        Highest precedence
    ∧ = AND (Conjugation)
        Second highest precedence
    ∨ = OR (Compound)
        Third highest precedence

--- 

## Problem 1

Fill in the following truth table:

<table>
	<tr>
		<th>p</th><th>q</th><th>¬p ∧ q</th>
	</tr>

	<tr>
		<td>_</td><td>_</td><td>_</td>
	</tr>

	<tr>
		<td>_</td><td>_</td><td>_</td>
	</tr>

	<tr>
		<td>_</td><td>_</td><td>_</td>
	</tr>

	<tr>
		<td>_</td><td>_</td><td>|</td><td>_</td>
	</tr>
</table>

## Problem 2

Build a truth table for the following statement:

	p ∧ ( q ∨ r )

Hint: Remember to break down the problem by charting out ( q ∨ r ) first, then the entire proposition.


## Problem 3

Translate the following from English into logical terms, using the propositions provided.

	a = The class has more than 10 students
	
	b = The class has less than 20 students

1. The class has more than 10 students and less than 20 students

2. The class has does not have more than 10 students

3. The class has 10 students or less

4. The class has 20 students or more


## Problem 4

> There are two men. One of them is wearing a red shirt, and one is wearing a blue shirt. The two men are named Andrew and Bob, but we do not know which is Andrew and which is Bob.

> The guy in the blue shirt says, “I am Andrew.”
> The guy in the red shirt says, “I am Bob.”

> If we know that at least one of them lied, then what color shirt is Andrew wearing?

###### ([Truth-Tellers and Liars. Brilliant.org. Retrieved from https://brilliant.org/wiki/truth-tellers-and-liars/](https://brilliant.org/wiki/truth-tellers-and-liars/))

Fill out the following truth table to analyze the situation:

<table>
    <tr>
	<th>Blue is telling the truth</th>
	<th>Red is telling the truth</th>
	<th>At least one lied</th>
	<th>1 Bob AND 1 Andrew AND 1 Lie</th>
    </tr>
    
    <tr>
	<td>_</td><td>_</td><td>_</td><td>_</td>
    </tr>
    
    <tr>
	<td>_</td><td>_</td><td>_</td><td>_</td>
    </tr>
    
    <tr>
	<td>_</td><td>_</td><td>_</td><td>_</td>
    </tr>
    
    <tr>
	<td>_</td><td>_</td><td>_</td><td>_</td>
    </tr>
</table>

## Problem 5

> There are 3 boxes, exactly one of which has a car. You can keep the car if you pick the correct box!

> On each box there is a statement, exactly one of which is true.

> Box A: The car is in this box.

> Box B: The car is not in this box.

> Box C: The car is not in box A.

> Which box has the car?

###### ([Truth-Tellers and Liars. Brilliant.org. Retrieved from https://brilliant.org/wiki/truth-tellers-and-liars/](https://brilliant.org/wiki/truth-tellers-and-liars/))

Think of this problem in terms of the propositions:

    1. p: A (car in box A)
    
    2. q: ¬B (car not in box B)
    
    3. r: ¬A (car not in box A)
    
Since there is only one car, we will test only these statements:

    1. A: Car is in box A
    
    2. B: Car is in box B
    
    3. C: Car is in box C
    
And since only one note can be true, we will write each scenario in terms
of the each note assuming it is true, and the others are false:

    4. p ∧ ¬ ( q ∨ r )
    (p is true, but q and r are not)
    
    5. q ∧ ¬ ( p ∨ r )
    (q is true, but p and r are not)
     
    6. r ∧ ¬ ( p ∨ q )
    (r is true, but p and q are not)
    
Fill out the following truth table to figure out which box the car is in.


<table>
    <tr>
	<th>A<br>Car in box A</th>
	<th>B<br>Car in box B</th>
	<th>C<br>Car in box C</th>
	<th>p<br>p = A</th>
	<th>q<br>q = ¬B</th>
	<th>r<br>r = ¬A</th>
	<th>p ∧ ¬ ( q ∨ r )</th>
	<th>q ∧ ¬ ( p ∨ r )</th>
	<th>r ∧ ¬ ( p ∨ q )</th>
    </tr>
    
    <tr>
	<td>T</td>
	<td>F</td>
	<td>F</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
    </tr>
    
    <tr>
	<td>F</td>
	<td>T</td>
	<td>F</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
    </tr>
    
    <tr>
	<td>F</td>
	<td>F</td>
	<td>T</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
	<td>_</td>
    </tr>
</table>

Which box has the car in it?

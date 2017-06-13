# Sequences

We will be looking at Sequences, and how to find a pattern between
sequences of numbers in order to build Closed and Recursive formulas
for them.

We will also look at building and evaluating sums using the summation notation.

## Definitions

### Closed Formula

With a closed formula, you can derive a specific element of the sequence
based on its index in the list.

Example: a<sub>n</sub> = n + 1

* a<sub>1</sub> = 1 + 1 = 2
* a<sub>2</sub> = 2 + 1 = 3
* a<sub>3</sub> = 3 + 1 = 4
* a<sub>4</sub> = 4 + 1 = 5

### Recursive Formula

With a recursive formula, you must first specify the first value of the 
list, at position 1...

* a<sub>1</sub> = 2

And then also define the formula for each subsequent number, referencing
previous elements (such as a<sub>n-1</sub>) in the formula.

Example: a<sub>1</sub> = 2; a<sub>n</sub> = a<sub>n-1</sub> + 1

* a<sub>1</sub> = 2
* a<sub>2</sub> = a<sub>1</sub> + 1 = 2 + 1 = 3
* a<sub>3</sub> = a<sub>2</sub> + 1 = 3 + 1 = 4
* a<sub>4</sub> = a<sub>3</sub> + 1 = 4 + 1 = 5

### Summation Notation

We can use a formula to define a sequence of numbers that will be
added together to get a single number (the sum) as a result.

We use the Sigma letter Σ, with:

* The starting value below the sigma (e.g., "k=1")
* The final value above the sigma (e.g., "4")
* And the formula to the right of the sigma (e.g., "a<sub>k</sub>")

It would be read as, "The sum from (beginning) to (end) of (formula)"

It is also similar to a for-loop in programming. For example:

	// The sum from 1 to 4 of 2k
	int sum = 0;
	for ( int k = 1; k <= 4; k++ )
	{
		sum += ( 2 * k );
	}

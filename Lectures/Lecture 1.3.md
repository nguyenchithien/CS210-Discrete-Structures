# Prepositional Logic

## Definitions

### Propositional Variables

> In mathematical logic, a propositional variable (also called a sentential variable or sentential letter) is a variable which can either be true or false. Propositional variables are the basic building-blocks of propositional formulas, used in propositional logic and higher logics.

-[Propositional variable / Wikipedia](https://en.wikipedia.org/wiki/Propositional_variable)

### Propositions

A proposition in logical is a statement that is either true or false, and it cannot be both.

### Logical Connectives

We use symbols called **logical connectives** to build a proposition...:

* ¬ = NOT (Negation)
	* Highest precedence
* ∧ = AND (Conjugation)
	* Second highest precedence
* ∨ = OR (Compound)
	* Third highest precedence

*Use parenthesis to keep your propositions easy to read!* 

### Logically Equivalent

> In logic, statements p and q are logically equivalent if they have the same logical content. This is a semantic concept; two statements are equivalent if they have the same truth value in every model (Mendelson 1979:56). The logical equivalence of p and q is sometimes expressed as p ≡ q {\displaystyle p\equiv q} p \equiv q, Epq, or p ⇔ q {\displaystyle p\Leftrightarrow q} p \Leftrightarrow q.

- [Logical equivalence / Wikipedia](https://en.wikipedia.org/wiki/Logical_equivalence)

In other words, if two propositions' truth table breakdown is the same, then they are logically equivalent.

### Tautology

> A formula of propositional logic is a tautology if the formula itself is always true regardless of which valuation is used for the propositional variables.

- [Tautology (logic) / Wikipedia](https://en.wikipedia.org/wiki/Tautology_(logic))

In other words, when building the truth table, all outcomes result to *True*.

### Contradiction

> In classical logic, a contradiction consists of a logical incompatibility between two or more propositions. It occurs when the propositions, taken together, yield two conclusions which form the logical, usually opposite inversions of each other. 

- [Contradiction / Wikipedia](https://en.wikipedia.org/wiki/Contradiction)

In other words, when building the truth table, all outcomes result to *False*.

---

## Example

If you've had a programming class, you've probably dealt with statements with ANDs, ORs, and NOTs...

	// If the rating is PG13, and either
	// a parent is attending or age is above 13.
	if ( rating == "PG13" && ( parentAttending || age >= 13 ) )
		Admit();
	
	// If not on a diet.
	if ( !onDiet )
		BuyPopcorn();


In Discrete Math, we write the same kind of statements, using the logical symbols listed above:

	P ∧ ( Q ∨ R )

	P = Rating is PG13
	Q = Parent attending
	R = Age is greater than or equal to 13

Instead of writing out a full conditional statement like (rating == "PG13"), our symbol *P* represents the condition.

---

## Truth Tables

We can then use a **truth table** to graph out all possible outcomes based on the conditions that we are checking.

For the given formal proposition:

	P = Ordered popcorn
	Q = Not on diet
	
	Get buttered popcorn = ( P ∧ Q )

*If I ordered popcorn, and I am not on a diet, then I should get buttered popcorn.*

We can build a table, where we fill in all the possible **states** of the conditions **P** and **Q**.

Once these states are filled in, we fill in the result for the proposition "P and Q?"

<table>
	<tr>
		<th>P</th>
		<th>Q</th>
		<th>Get buttered popcorn? <br>( P ∧ Q )</th>
	</tr>

	<tr>
		<td>T</td>
		<td>T</td>
		<td>T</td>
	</tr>

	<tr>
		<td>T</td>
		<td>F</td>
		<td>F</td>
	</tr>

	<tr>
		<td>F</td>
		<td>T</td>
		<td>F</td>
	</tr>

	<tr>
		<td>F</td>
		<td>F</td>
		<td>F</td>
	</tr>
</table>

With a simple AND statement, all of the **propositional variables** are true. If any of them are false, then the entire proposition is false.

---

Truth tables become more useful, given more complex propositions.  Using a truth table, we can break up a large proposition into its separate parts, and analyze them separately.

	P = Rating is PG13
	Q = Parent attending
	R = Age is greater than or equal to 13

	Admitted to movie = P ∧ ( Q ∨ R )

First, we fill out all the possible states of P, Q, and R:

<table>
	<tr>
		<th>P</th>
		<th>Q</th>
		<th>R</th>
	</tr>

	<tr><td>T</td><td>T</td><td>T</td></tr>

	<tr><td>T</td><td>T</td><td>F</td></tr>

	<tr><td>T</td><td>F</td><td>T</td></tr>

	<tr><td>T</td><td>F</td><td>F</td></tr>

	<tr><td>F</td><td>T</td><td>T</td></tr>

	<tr><td>F</td><td>T</td><td>F</td></tr>

	<tr><td>F</td><td>F</td><td>T</td></tr>

	<tr><td>F</td><td>F</td><td>F</td></tr>
</table>

Then, we can begin to add columns to analyze one statement at a time. For ( Q ∨ R ), we are only looking at the *Q* and *R* column - *P* doesn't affect the outcome of this portion.

<table>
	<tr>
		<th>P</th>
		<th>Q</th>
		<th>R</th>
		<th>( Q ∨ R )</th>
	</tr>

	<tr><td>T</td><td><strong>T</strong></td><td><strong>T</strong></td>
	<td>T</td>
	</tr>

	<tr><td>T</td><td><strong>T</strong></td><td><strong>F</strong></td>
	<td>T</td>
	</tr>

	<tr><td>T</td><td><strong>F</strong></td><td><strong>T</strong></td>
	<td>T</td>
	</tr>

	<tr><td>T</td><td><strong>F</strong></td><td><strong>F</strong></td>
	<td>F</td>
	</tr>

	<tr><td>F</td><td><strong>T</strong></td><td><strong>T</strong></td>
	<td>T</td>
	</tr>

	<tr><td>F</td><td><strong>T</strong></td><td><strong>F</strong></td>
	<td>T</td>
	</tr>

	<tr><td>F</td><td><strong>F</strong></td><td><strong>T</strong></td>
	<td>T</td>
	</tr>

	<tr><td>F</td><td><strong>F</strong></td><td><strong>F</strong></td>
	<td>F</td>
	</tr>
</table>

Remember that, for an OR statement, if at least one of the propositional variables is *true*, then the entire proposition is true. The proposition can only be *false* if all propositional variables are false.

Now that we have analyzed the sub-proposition, we can compare it to the last piece of our total proposition to figure out the big picture.

<table>
	<tr>
		<th>P</th>
		<th>Q</th>
		<th>R</th>
		<th>( Q ∨ R )</th>
		<th>P ∧ ( Q ∨ R )</th>
	</tr>

	<tr><td><strong>T</strong></td><td>T</td><td>T</td>
	<td><strong>T</strong></td>
	<td>T</th>
	</tr>

	<tr><td><strong>T</strong></td><td>T</td><td>F</td>
	<td><strong>T</strong></td>
	<td>T</th>
	</tr>

	<tr><td><strong>T</strong></td><td>F</td><td>T</td>
	<td><strong>T</strong></td>
	<td>T</th>
	</tr>

	<tr><td><strong>T</strong></td><td>F</td><td>F</td>
	<td><strong>F</strong></td>
	<td>F</th>
	</tr>

	<tr><td><strong>F</strong></td><td>T</td><td>T</td>
	<td><strong>T</strong></td>
	<td>F</th>
	</tr>

	<tr><td><strong>F</strong></td><td>T</td><td>F</td>
	<td><strong>T</strong></td>
	<td>F</th>
	</tr>

	<tr><td><strong>F</strong></td><td>F</td><td>T</td>
	<td><strong>T</strong></td>
	<td>F</th>
	</tr>

	<tr><td><strong>F</strong></td><td>F</td><td>F</td>
	<td><strong>F</strong></td>
	<td>F</th>
	</tr>
</table>

We can ignore columns *Q* and *R* while figuring out *P ∧ ( Q ∨ R )*, because we've already analyzed *( Q ∨ R )*. We only need to look at columns 1 and 4 to figure out the proposition.

---

## Negating Propositions

What happens if we have a negation like one of these?

	¬( A ∧ B )

	¬( A ∨ B )


Let's think of these in English terms...

<table>
	<tr>
		<td>A</td>
		<td>Bob is a cat<br>( cat )</td>
		<td>¬A</td>
		<td>Bob is not a cat<br>( !cat )</td>
	</tr>

	<tr>
		<td>B</td>
		<td>Bob is more than 10 years old<br>( age > 10 )</td>
		<td>¬B</td>
		<td>Bob is 10 years old or less<br>( age <= 10 )</td>
	</tr>

</table>

First, notice that the *opposite* of "greater than" is "less than or equal to", and vice versa - the opposite of "greater than or equal to" is "less than".

When we have propositions combined with AND or OR, then the negation is distributed...

1. ( A ∧ B ) = Bob is a cat AND Bob is more than 10 years old. (cat AND age >= 10)
2. ¬( A ∧ B ) = It is false that... (cat AND age >= 10)
3. ¬A ∨ ¬B = NOT ( cat ) OR NOT ( age >= 10 )

We can see this more clearly through a truth table. Let's start just by analyzing ( A ∧ B ):

<table>
	<tr>
		<th>A</th><th>B</th><th>( A ∧ B )</th>
	</tr>
	<tr>
		<td>T</td><td>T</td><td>T</td>
	</tr>
	<tr>
		<td>T</td><td>F</td><td>F</td>
	</tr>
	<tr>
		<td>F</td><td>T</td><td>F</td>
	</tr>
	<tr>
		<td>F</td><td>F</td><td>F</td>
	</tr>
</table>

If we look at **¬( A ∧ B )** simply as **the opposite of the result of ( A ∧ B )**, then we can easily figure out the outcomes in our truth table:

<table>
	<tr>
		<th>A</th><th>B</th><th>( A ∧ B )</th><th>¬( A ∧ B )</th>
	</tr>
	<tr>
		<td>T</td><td>T</td>
		<td>T</td>
		<td>F</td>
	</tr>
	<tr>
		<td>T</td><td>F</td>
		<td>F</td>
		<td>T</td>
	</tr>
	<tr>
		<td>F</td><td>T</td>
		<td>F</td>
		<td>T</td>
	</tr>
	<tr>
		<td>F</td><td>F</td>
		<td>F</td>
		<td>T</td>
	</tr>
</table>

And if we *distribute* the negation through the entire preposition, it becomes **( ¬A ∨ ¬B )**, which we can see are logically equivalent:

<table>
	<tr>
		<th>A</th><th>B</th><th>( A ∧ B )</th><th>¬( A ∧ B )</th>

		<th>¬A</th>
		<th>¬B</th>
		<th>( ¬A ∨ ¬B )</th>
	</tr>
	<tr>
		<td>T</td><td>T</td>
		<td>T</td>
		<td>F</td>
		<td><strong>F</strong></td><td><strong>F</strong></td>
		<td>F</td>
	</tr>
	<tr>
		<td>T</td><td>F</td>
		<td>F</td>
		<td>T</td>
		<td><strong>F</strong></td><td><strong>T</strong></td>
		<td>T</td>
	</tr>
	<tr>
		<td>F</td><td>T</td>
		<td>F</td>
		<td>T</td>
		<td><strong>T</strong></td><td><strong>F</strong></td>
		<td>T</td>
	</tr>
	<tr>
		<td>F</td><td>F</td>
		<td>F</td>
		<td>T</td>
		<td><strong>T</strong></td><td><strong>T</strong></td>
		<td>T</td>
	</tr>
</table>

### Truth Tables for Negation

So remember to keep these in mind when dealing with negation:

#### ¬( A ∧ B ) ≡ ( ¬A ∨ ¬B )

<table>
	<tr>
		<th>A</th><th>B</th><th>( A ∧ B )</th><th>¬( A ∧ B )</th><th>( ¬A ∨ ¬B )</th>
	</tr>

	<tr>
		<td>T</td><td>T</td><td>T</td><td>F</td><td>F</td>
	</tr>

	<tr>
		<td>T</td><td>F</td><td>F</td><td>T</td><td>T</td>
	</tr>

	<tr>
		<td>F</td><td>T</td><td>F</td><td>T</td><td>T</td>
	</tr>

	<tr>
		<td>F</td><td>F</td><td>F</td><td>T</td><td>T</td>
	</tr>
</table>

####  ¬( A ∨ B ) ≡ ( ¬A ∧ ¬B )

<table>
	<tr>
		<th>A</th><th>B</th><th>( A ∨ B )</th><th>¬( A ∨ B )</th><th>( ¬A ∧ ¬B )</th>
	</tr>

	<tr>
		<td>T</td><td>T</td><td>T</td><td>F</td><td>F</td>
	</tr>

	<tr>
		<td>T</td><td>F</td><td>T</td><td>F</td><td>F</td>
	</tr>

	<tr>
		<td>F</td><td>T</td><td>T</td><td>F</td><td>F</td>
	</tr>

	<tr>
		<td>F</td><td>F</td><td>F</td><td>T</td><td>T</td>
	</tr>
</table>

These two negations are known as [DeMorgan's Law](https://en.wikipedia.org/wiki/De_Morgan%27s_laws).
# Predicates

## Definitions

### Predicate

> In mathematics, a predicate is commonly understood to be a Boolean-valued function P: X→ {true, false}, called the predicate on X.

> Informally, a predicate is a statement that may be true or false depending on the values of its variables.[1] It can be thought of as an operator or function that returns a value that is either true or false.[2]

([Predicate (mathematical logic) / Wikipedia](https://en.wikipedia.org/wiki/Predicate_%28mathematical_logic%29))

A proposition is more of a static statement that does not change,
while a predicate is more like a *function*, where you can plug in some value
and it will give a different result based on the input.

F(t) is the predicate "t is greater than 100".

### Quantified Statement

> A quantified statement is a simple statement in predicate logic whose subject is qualified by either the universal quantifier or the existential quantifier.

([Definition: Quantified Statement / ProofWiki](https://proofwiki.org/wiki/Definition:Quantified_Statement))

Think of the entire "There exists x in D such that ..." or "∀ x ∈ X, P(x)" as the quantified statement.

### Domain

> In mathematics, and more specifically in naive set theory, the domain of definition (or simply the domain) of a function is the set of "input" or argument values for which the function is defined. That is, the function provides an "output" or value for each member of the domain.

([Domain of a function / Wikipedia](https://en.wikipedia.org/wiki/Domain_of_a_function))

### Symbols

* ∈ = Is an element of
* ∃ = There exists
* ∀ = For all

### Counterexample

> In logic, and especially in its applications to mathematics and philosophy, a counterexample is an exception to a proposed general rule or law.

> More precisely, a counterexample is a specific instance of the falsity of a universal quantification (a "for all" statement).

([Counterexample / Wikipedia](https://en.wikipedia.org/wiki/Counterexample))

### Set

> A set is a well defined collection of distinct objects.

> Sets are conventionally denoted with capital letters. Sets A and B are equal if and only if they have precisely the same elements.

> An extensional definition is denoted by enclosing the list of members in curly brackets:

>    C = {4, 2, 1, 3}

>    D = {blue, white, red}. 

([Set (mathematics) / Wikipedia](https://en.wikipedia.org/wiki/Set_%28mathematics%29#Definition))

---

## Negations

We can apply DeMorgan's laws towards predicates as well as propositions.

* Propositions
	* ¬( A ∧ B ) ≡ ( ¬A ∨ ¬B )
	* ¬( A ∨ B ) ≡ ( ¬A ∧ ¬B )
	
* Predicates
	* The negation of **∀ x ∈ X, P(x)** is **∃ x ∈ X, ¬P(x)**
		* "For all x in X, such that P(x)." --> "There exists x in X, such that not-P(x)"
		* ([Universal quantification / Wikipedia](https://en.wikipedia.org/wiki/Universal_quantification#Negation))
	* The negation of **∃ x ∈ X, P(x)** is **∀ x ∈ X, ¬P(x)**
		* ([Existential quantification / Wikipedia](https://en.wikipedia.org/wiki/Existential_quantification#Negation))

### Example

	What is the negation of: ∀ x ∈ X, x > 32

1. ¬( ∀ x ∈ X, x > 32 )
2. ∃ x ∈ X, ¬( x > 32 )
3. ∃ x ∈ X, x <= 32

Think of it as distributing the ¬ between each *part* of the quantified statement.

---


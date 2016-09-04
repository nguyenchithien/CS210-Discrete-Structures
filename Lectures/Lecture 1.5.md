# Implications

## Definitions

### Implication

An Implication is when we write an "if, else" statement in Discrete Math, such as
"if p is true, then q is true".

We can write implications for both propositions and for predicates.

### Implies

We use the arrow operator ➝ to symbolize "implies". 

So for "if p is true, then q is true", we would write **p ➝ q**.

### Hypothesis

For the statement **p ➝ q**, p is the hypothesis.

### Conclusion

For the statement **p ➝ q**, q is the conclusion.

In order to prove an implication to be false, we must have a case where
the hypothesis is true and the conclusion is false.

### Negating Implications

The negation of the implication **p ➝ q** is **p ∧ ¬q** (p and not q).

### Contrapositive

> In logic, contraposition is a law that says that a conditional statement is logically equivalent to its contrapositive. 
The contrapositive of the statement has its antecedent and consequent inverted and flipped: 
the contrapositive of P → Q is thus ¬ Q → ¬ P. For instance, the proposition "All bats are mammals" can be restated as the conditional "If something is a bat, then it is a mammal". Now, the law says that statement is identical to the contrapositive "If something is not a mammal, then it is not a bat."

([Contraposition / Wikipedia](https://en.wikipedia.org/wiki/Contraposition))

In predicate terms, if **∀ x ∈ D, P(x) → Q(x)**, then the contrapositive is **∀ x ∈ D, ¬Q(x) → ¬P(x)**.

### Converse

> Conversion (the converse), Q → P 
    "If something is a mammal, then it is a bat." 
    The converse is actually the contrapositive of the inverse and so always has the same truth value as the inverse, 
    which is not necessarily the same as that of the original proposition.

([Contraposition / Wikipedia](https://en.wikipedia.org/wiki/Contraposition))

In predicate terms, if **∀ x ∈ D, P(x) → Q(x)**, then the converse is **∀ x ∈ D, Q(x) → P(x)**.

### Inverse

> Inversion (the inverse), ¬ P → ¬ Q
    "If something is not a bat, then it is not a mammal." 
    Unlike the contrapositive, the inverse's truth value is not at all dependent on whether or not the original proposition was true, as evidenced here. 
    The inverse here is clearly not true.

([Contraposition / Wikipedia](https://en.wikipedia.org/wiki/Contraposition))

In predicate terms, if **∀ x ∈ D, P(x) → Q(x)**, then the converse is **∀ x ∈ D, ¬P(x) → ¬Q(x)**.

---

## Truth Tables of Implications

The truth table for **p → q** is:

<table>
<tr>
<th>p</th><th>q</th><th>p → q</th>
</tr>
<tr>
<td>T</td><td>T</td><td>T</td></tr><tr>
<td>T</td><td>F</td><td>F</td></tr><tr>
<td>F</td><td>T</td><td>T</td></tr><tr>
<td>F</td><td>F</td><td>T</td>
</tr>
</table>

([Material conditional / Wikipedia](https://en.wikipedia.org/wiki/Material_conditional#Truth_table))

The statement **p → q** means only "if p is true, then q is also true", and doesn't give a result for if p is false; therefore, the *validity* of p → q is still intact if **p is false**, because p being false doesn't have an effect on q; the only time the statement "if p is true then q is true" is invalid is if p is true, but then q is false.

--

## Negation of implications

Remember that, "In order to prove an implication false, we must have a case where the hypothesis is true and the conclusion is false."

**¬(p → q)** is logically equivalent to **p ∧ ¬q**.



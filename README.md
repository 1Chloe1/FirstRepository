# 1Chloe1/FirstRepository

[comment]: # Chloe J. Xi starts her lessons on 05/12/2025!

A collection of sessions of Chloe J. Xi learning programming

## Baisic Programming Concepts

Functional programming originates from Alonzo Church's
lambda-calculus, which is a computational model based on
the notion of substitution. Church's lambda-calculus is
often referred to as pure lambda-calculus.

A (functional) program is a lambda-expression (in some extended
lambda-calculus), and computation is defined as a process that turns a
program into a value, which is an expression of some special forms.

### Integers (or Ints)
  
Integers are a special form of values. We have integers like
0,1,-1,2,-2, etc.  We use `int` as the type for integers. Sometime,
we use `sint` for `int` to emphasize that the integers are signed.

### Booleans (or Bools)

There are two boolean values: true and false. The type for these two
values is `bool`.

### Characters (or Chars)

Characters are essentially small integers.
For instance, the character `'a'` refers to its ascii code 97.
The type for characters is `char`.

### Strings (or Strns)

A string is a sequence of characters. For instance, "Chloe" and "Xi"
are two strings. The type for strings is `string` or `strn` (as a
shorthand).

### Built-in Functions

We have some built-in functions defined ints, bools, chars, and strns.

<!--
How can one define integer maximum in terms of integer negation and
integer minimum?

def int_max(x, y):
  return -int_min(-x, -y)
-->

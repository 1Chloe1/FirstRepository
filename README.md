# 1Chloe1/FirstRepository

[comment]: # Chloe J. Xi starts her lessons on 05/12/2025!

A collection of sessions of Chloe J. Xi learning programming

## Basic Programming Concepts

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

There are two boolean values: `true` and `false`. The type for these two
values is `bool`.

### Characters (or Chars)

Characters are essentially small integers.  For instance, the
character `'a'` refers to its ascii (american standard code for
information interchange) code 97.  The type for characters is `char`.

### Strings (or Strns)

A string is a sequence of characters. For instance, "Chloe" and "Xi"
are two strings. The type for strings is `string` or `strn` (as a
shorthand).

### Built-in Functions

We have some built-in functions defined on ints, bools, chars, and
strns.

<!--
How can one define integer maximum in terms of integer negation and
integer minimum?

def int_max(x, y):
  return -int_min(-x, -y)
-->

#### Boolean coding:

- Boolean decode: `i2b`: (`int`) -> `bool`
- Boolean encode: `b2i`: (`bool`) -> `int`

#### Character coding:

- Character decode: `chr`: (`int`) -> `char`
- Character encode: `ord`: (`char`) -> `int`

#### Logic operations

- Boolean negation `not`: (`bool`, `bool`) -> `bool`
- Boolean disjunction `or`: (`bool`, `bool`) -> `bool`
- Boolean conjunction `and`: (`bool`, `bool`) -> `bool`

#### Arithmetic operations

- Integer addition `+`: (`int`, `int`) -> `int`
- Integer subtraction `-`: (`int`, `int`) -> `int`
- Integer multiplication `-`: (`int`, `int`) -> `int`
- Integer division `*`: (`int`, `int`) -> `int`
- Integer modulo `%`: (`int`, `int`) -> `int`

#### Integer Comparisons

- Integer equal-to `=`: (`int`, `int`) -> `bool`
- Integer less-than `<`: (`int`, `int`) -> `bool`
- Integer greater-than `>`: (`int`, `int`) -> `bool`
- Integer not-equal-to `!=`: (`int`, `int`) -> `bool`
- Integer less-than-or-equal-to `<=`: (`int`, `int`) -> `bool`
- Integer greater-than-or-equal-to `>=`: (`int`, `int`) -> `bool`
- Integer comparison `intcmp`: (`int`, `int`) -> `int`

<!--
########################(end-of-[README.md])########################
-->

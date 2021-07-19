# Coding Challenge

**What you will need**
- Python 3+ interpreter

**How to use**
1. Make sure you have Python 3+ installed
2. Clone this repository
3. Execute the following command:
  `python3 challenge.py [-level1|level2|level3] <input_string>`

**Running unit tests**
`python3 -m unittest tests/<test_suite>.py`

**Running all unit tests**
`python3 -m unittest discover tests -p "*.py"`

---

### Technical Brief

#### Level 1
Level 1 is pretty simple, start comparison check on both ends of the string, as checks succeed, move inward until the the checkers meet.

###### Example

```
racecar
r <-> r | success
a <-> a | success
c <-> c | success
e <-> e | success
racecar is a palindrome!
```

```
racedar
r <-> r | success
a <-> a | success
c <-> d | fail
racedar is not a palindrome :(
```

**Time Complexity**

This solution runs in O(n/2) or simply O(n) time since we fold the string in half and start comparing the characters inwards

**Space complexity**

We only need to store the input itself, so it's O(1).

---

#### Level 2
Level 2 just does Level 1, but on each character in the input, since we don't really want to know if the whole input is a palindrome, rather we wanna know all palindromes present in the input and see who's the longest.

To further optimize, the approach skips to the end of a previous palindrome if the current palindrome is part of the previous palindrome.

###### Example
`racecarmadamhjn`

The _start marker_ starts with `r` and the _end marker_ starts from the end which is `n`.

The start and end are compared, they don't match, the _end marker_ goes to the next character, which is `j`, they still don't match; this process continues until start and end match.

**Fast-forward >>>**

The _end marker_ is now at the second `r`, start and end match, it is a palindrome candidate, we check further...

The _start marker_ moves to the next character, which is `a`, same for the _end marker_, they still match; this process repeats until the two _markers_ match and meet.

If during the process, there was a mismatch, we backtrack -- which we will explore on the step: **Inside a Palindrome**. For now, we know that our markers will find our first palindrome, which is `racecar`

We save `racecar` as the longest palindrome; it is the current holder of the title :cool:.

**Short commercial: Overlaps**

Yay, we found our first palindrome, but we don't really wanna skip ahead, since there could be overlapping palindromes we might miss e.g., `aracecar`, after finding `ara`, skipping ahead means not finding `racecar`.

Let's discuss overlaps later, for now we'll proceed to the next character.

**Inside a Palindrome**

The _start marker_ proceeds to `a` and the _end marker_ starts again from the end, it reaches the first `a` from the end.

The _start marker_ and _end marker_ move inwards, _start marker_ is now at `c` and _end marker_ at `d`, they don't match, what do we do? We give up.
_start marker_ goes back to `a` but _end marker_ carries on to another `a`

Repeat the process until _end marker_ meets the third `a` from the end, the `a` inside `racecar`

However, at this point, the solution detects that both _start marker_ and _end marker_ are currently residing in the previous palindrome, we don't need to check further, there's no use.

_start marker_ now proceeds to the next character, which is `c`

**Rinse, Repeat**

These process repeats until the whole input is scanned.

If in the process, another palindrome is found, we check if it's longer than the current title holder, if yes, we give them title :)

**Time Complexity**

Since we check each character, and in each character, we scan from the end for a palindrome, this solution runs in O(n<sup>2</sup>) time.

**Space Complexity**

We only really store the current longest palindrome, nothing else. So it's O(1)

---

#### Level 3
This is where everything gets dirty.

For this solution, the function actually returns the string with the `|` representing split markers, to make validation easier.

The solution builds on top of the logic that Level 2 does.

For _Happy Path_ inputs, it's simple, we find the palindromes, and since we can already find as small as one character palindromes, this should be easy.

###### Example
`noonabbadd`

Starting from `n`, we do the Level 2 logic until it finds `noon`, done.

We still proceed to `o` next, since there could be overlaps, but let's not worry about it right now, we'll skip past `noon`.

We're not at `a`, and we find `abba`, finally, we found `dd`.

Now to count the minimum number of split count, we just count all the palindromes, minus 1. So 3 - 1 = 2
`2 // noon|abba|dd`

To make it simple, the first step in this solution is to extract all palindromes from the string.

**Overlapping Palindromes**

These palindromes are a pain...

E.g., we have `aracecar`

We have two options for splitting this string:
1. `ara|cec|a|r`
2. `a|racecar`

In this solution, whenever we find overlapping palindromes, we group them up, so later we can determine that they are indeed overlapping, and then act accordingly.

Obviously, we want the second option, since we only have a single split, over the triple split of the first option.

To be able to compute the lesat amount of split counts, the solution needs to recognize overlapping palindromes.

It sees that `ara` and `racecar` are palindromes that overlap with each other, so what do we do?

We check both and weigh their products.

First we check `ara`, if we choose to split after `ara`, we're left with `cecar`
`cecar` when splitted further, will give us `cec|a|r`, so by choosing `ara`, we got a split count of 2 for the remaining `cecar`

Now we check `racecar`, if we choose to split before `racecar`, we're left with `a`, which is already a palindrome on its own, so we don't need to split further, so by choosing `racecar`, we got a split count of 0 for the remaining `a`

In this solution, this process was done by recursion, the _"remainders"_ are passed as input _(to the same function)_ to count their individual split counts.

Now it is obvious that we want `racecar` over `ara`, we choose it.

**The Terror of Overlapping Palindromes**

Unfortunately, there's a case where we have triple overlapping palindromes.

The solution is able to handle _some_ of it.

`abaracecar` has triple overlapping palindromes: `aba`, `ara`, and `racecar`

The split which has the least count for this text is `aba|racecar`

In this situation, the solution finds these triple overlaps early in the palindrome extraction phase, once it finds one, it tries to act immediately; deciding which of the palindromes it should keep and which ones to drop.

**Time Complexity**

This solution builds on top of the logic in Level 2, but does another round of recursions when faced with overlapping palindromes.

Though I'd say it should still run in O(n<sup>2</sup>) time


**Space Complexity**

In this solution, we store all palindromes in a string, we can assume that, at worst, a string can have N palindromes where N is the length of the string.

E.g., `abcd` has four palindromes: `a`, `b`, `c`, `d`

We also store overlapping palindromes, and create temporary stores to resolve those overlapping palindromes. I'd say that this solution will hog O(n) of space.

**Incorrectly Handled Inputs**

:(
I wasn't able to figure out what's wrong when trying to split `aabaracecar`
It always outputs:
```
a|aba|a|racecar
3
```
I'm not quite sure if there's any more edge cases this solution misses, but that's one edge case I'm well aware of.

I'm pretty sure, my approach is one factor as to why I'm having trouble catching this edge case, because I kinda worked on most edge cases in isolation, meaning, I tried to fix edge cases one by one, whenever one comes out.

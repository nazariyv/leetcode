# Pseudocode

((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()

Can I remove all the (*) or is there a case where I actually need a bracket in there?
Yes, there is, for example (*))

Can I simplify the problem first by removing the matched brackets? Yes, I can
(((((*(((((*)*(**))))))))))) ((((*))))) (((**(*)))(*)
This can be solved with stacks in O(n) time and O(n) space

Now, what do I do? I see three subproblems that can each be solved on their own.
These subproblems are defined by having adjacent )( brackets. The subproblems are

1. (((((*(((((*)*(**)))))))))))
2. ((((*)))))
3. (*)

Note that a subproblem may have subproblems too, for example 1. So this needs recursion until base case is achieved, like either in 3 or simply everything balances out

But first need to now try out different combinations of brackets for the subproblems. This is where it gets hairy. Is there a way to avoid this?

Some heuristics are:

1. If there is a single star in the subproblem, check if balance is either -1 or +1. Do not check if brackets are valid, they are, because by definition the subproblem does not contain )(, i.e. is valid
2. If there is balance and there, it does not matter how many stars there are, this subproblem is valid
3. If there is more than one star, and the subproblem is not balanced, we have to brute force, right?

Is it possible that I cannot balance the brackets when stars >= brackets?
Yes, for example, )*, *(, )**( and so on. But these can be weeded out with the check for the first and last char

The stopping conditions of having the stars at least as many as the absolute value of the balance is incorrect, consider this situation:
()))))))******
But, we are reducing the problem initially, so the above is equivalent to: ))))))****, which would get discarded. Similarly
*******((((()
would reduce to something that is false: ******((((((,
however, something like this:
(((*(*))))*))) would pass currently but is definitely (balance=-3, stars=3)
false:
(((((()))))))) -> it has two extra brackets

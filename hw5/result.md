Below are the output of all the sentences in blue after parsing.

1. (S (NP (Det A) (N fish)) (VP (V is) (NP (Det an) (N animal))))
2. (S (NP (Det A) (N bird)) (VP (V is) (NP (Det an) (N animal))))
3. (S (NP (Det A) (N fish)) (VP (V has) (NP (N gills))))
4. (S (NP (Det A) (N fish)) (VP (V swims)))
5. (S (NP (Det A) (N bird)) (VP (V flies)))
6. (S (NP (PRON What)) (VP (V is) (NP (N fish))))
7. (S (VP (V Is)) (NP (Det a) (N fish)) (NP (Det an) (N animal)))
8. (S (Aux Does) (NP (Det a) (N fish)) (VP (V swim)))
9. (S (Aux Does) (NP (Det a) (N bird)) (VP (V have) (NP (N gills))))
10. (S (Aux Does) (NP (Det a) (N bird)) (VP (V fly)))

Below are three additional sentences accepted by my program.

* Dogs swim.
(S (NP (N Dogs)) (VP (V swim)))
* This dog swims.
(S (NP (Det This) (N dog)) (VP (V swims)))
* Who swims?
(S (NP (PRON Who)) (VP (V swims)))

Below are three additional sentences rejected by my prgram.

* Snoopy is a dog that swims.
* Is Socrates a dog that swims?
* Does fish bite birds that fly?

My program recognizes all of the sentences in the extended test suite given.

Reflection:

The cruicial part of the exercise is to convert all non-terminals to terminals and come up with grammar rules that work on as many given sentences as possible.

Here is how I arrived at ths solutions:

1. Use a tagger to find out all the taggings for the terminals.

2. Rewrite grammar rules based on the terminals.

3. Recognize the grammar rules of the sentences not recognized by the program.

4. Update grammer rules so that the program can recognize more sentences.

5. Come up with three additional sentences that the program can recognize and test with the program.

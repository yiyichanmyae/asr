
Probabilities and Likelihoods with Bigrams

Recall from a previous video that the probability of a series of words can be calculated from the chained probabilities of its history:


The probabilities of sequence occurrences in a large textual corpus can be calculated this way and used as a language model to add grammar and contectual knowledge to a speech recognition system. However, there is a prohibitively large number of calculations for all the possible sequences of varying length in a large textual corpus.

To address this problem, we use the Markov Assumption to approximate a sequence probability with a shorter sequence:


In the bigram case, the equation reduces to a series of bigram probabilities multiplied together to find the approximate probability for a sentence. A concrete example:

\qquad \qquad P("I\: Iove\: language\: models") \approxP("IIovelanguagemodels")≈
\qquad \qquad \qquad \qquad P("love"|"I")P("language"|"love")P("models"|"language")P("love"∣"I")P("language"∣"love")P("models"∣"language")

We can calculate the probabilities by using counts of the bigramsand individual tokens. The counts are represented below with the c()c() operator:


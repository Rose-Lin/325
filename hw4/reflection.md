Assignment 4

Rose Lin

* The exercise helps me get more familiar with the tagging methods of nltk, and the two tutorials are really helpful.

* The tagging system is designed as follows:

  * Train hmm Tagger on all nltk brown corpus tagged sentences, with category news and tagset as universal, so that the tagged sentences from hmm Tagger would be the golden standard.
  
  * Tag all four texts with Unigram Tagger.

  * Examine through the tagged sentences, find out all the `None` tags and change them to the corresponding tags from hmm tagger. Unigram tagging will produce `None` tag for some nouns like computer. This is the main source of the inaccuracy.

  * Use the hmm Tagger to evaluate the outcome of Unigram Tagger.
 
* For the regular expression tagger, some special cases are taken into consideration for the two provided test text. For example, `bite` is tagged as `VERB`, `Polly` is tagged as `NOUN` instead of `ADJ`, which is implied by the more general rules.

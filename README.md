# ngramBasedTextGenerator
Generates random text based on n-grams of text files that it uses as training data.

The training text files I used were the first 3 Game of Thrones books. Can handle unigrams, bigrams, and trigrams.

Input: HOW TO RUN

The first three game of thrones books are passed in as textfiles to be parsed.	

./talker.py 3 10 001ssb.txt 002ssb.txt 003ssb.txt	

3 is the n in ngram, 10 is the number of sentences to be generated.

Algorithm:

	PreProcess passed text files. 
	
		Tokenize text files so they're split on spaces and punctuation.
		
		Create separate token lists of tokenized sentences, split on punctuation.
		
		Add both sets of word and sentence tokens to respective master list,
		
			which holds all texts token lists.
			
		Create frequency distributions for all sets of word tokens.
		
		Frequency distributions tell us how often a word is used.

	Calculate Total Word Count and Unique Word Count.

	Call corresponding ngram function related to passed in sys.argv[1]

	Unigrams:
		Create a wordMap. Every key in wordMap can have multiple values.
		Values represent ranges. 
			In text 1, the word 'the' was used n times, so it has a range of
			current to current+n. If text 2 also has the word 'the'
			a second different range is added as a value. All ranges are checked
			when trying to figure out what our randomly generated number
			corresponds to.
		
		Compute x sentences, where x is argument 2.
			randomly generate numbers from 0 to highest range.
			So long as the number isn't in the range of the '.' key,
			keep adding keys onto the sentence. Terminates when it
			comes across punctuation.
			Print sentence.

	Bigrams:
		Create a list to store bigrams.
		Create a map that maps bigram pairs to ranges.
		Uses sentence tokens generated in preprocessing.
		For word in every sentence in every text in sentenceTokenList,
			check if its at the beginning of a sentence
			if it is, set its partner to a space.
			else set its main value to current word, and partner to previous word
			do this for remaining elements in sentence, with punctuation being last
		
		Calculate frequency distribution of bigram pairs.
		Use frequency distribution numbers to assign ranges to bigram pairs
		
		Compute x sentences, where x is argument 2
			randomly generates numbers from 0 to highest range.
			Finds which bigram has the range that number falls in
			Adds bigram words into sentence
			Continues until punctuation
			Prints sentence

	Trigrams:
  		Create a list to store trigrams.
                 Create a map that maps trigram pairs to ranges.
                 Uses sentence tokens generated in preprocessing.
                 For word in every sentence in every text in sentenceTokenList,
                         check if its at the beginning of a sentence
                         if it is, set both partners to a space.
			 else if its the 2nd word in a sentence
			 if it is, set first partner to space, second to word 1
                         else set its main value to current word, and partners to previous words
                         do this for remaining elements in sentence, with punctuation being last
                 
                 Calculate frequency distribution of trigram pairs.
                 Use frequency distribution numbers to assign ranges to trigram pairs
                 
                 Compute x sentences, where x is argument 2
                         randomly generates numbers from 0 to highest range.
                         Finds which trigram has the range that number falls in
                         Adds trigram words into sentence
                         Continues until punctuation
                         Prints Sentence

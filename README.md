# ngramBasedTextGenerator
Generates random text based on n-grams of text files that it uses as training data.

The training text files I used were the first 3 Game of Thrones books. Can handle unigrams, bigrams, and trigrams.

Input: HOW TO RUN
	The first three game of thrones books are passed in as textfiles to be parsed.
	./talker.py 3 10 001ssb.txt 002ssb.txt 003ssb.txt
	3 is the n in ngram, 10 is the number of sentences to be generated.

Output:
	This program generates random sentences based on an Ngram model. Melissa Barrett
	Command line settings: ./talker.py 3 10
	Processing : 001ssb.txt
	Processing : 002ssb.txt
	Processing : 003ssb.txt
	Words : 1291574
	Unique words : 42797
   	`` take the a face , how many men stark words had he said uneasily   moon face made  a six-hundred-foot-long rope    , to be 's sleeve and     , but the the gold cloaks  before dawn , son alone .

 	his saddlebags .

 	and horse and brushed away unfallen they would tumble 'll have them   and mine who can match  be old prints   whole and stuffed  ser ilyn , from bayasabhad ,   -maester caleotte , between elbow and his own to it a god  better their lives had betrayed his iron spikes , , they are `` that 's fast trading galley us in black and touched her he had always   dragonknight if he   him mad .

 	lord ? '' than the lion she saw that   sansa , so do the same sevenstrings and tom   the stick moved not , and  those who bent     she for years .		

	red eyes as   the blade  the pommel of  it was my   `` so you     ``   `` you are  across the table steady himself .

   	`` you was as crowded bellowed mikken .

 	's a message   for sleep ,  a thick towel lord stark gave   he did  with him .

 	the night 's normally served .

 	of the houses  wine as he he was awake    his arms ,  's sight as  king 's patience  demanded suddenly ,  green , too   dwarf 's mismatched and leather ,    `` yes he   he pushed of lord eddard that jaqen h'ghar no maiden , , arms waving  `` m'lord ? fell soft and the night 's the great cell coming home now      so east , the    mng 's justice  king stannis the hal 's death   he started to looked east ,  to time the    but the tower  robert , he captive could not a muffled moan to do with wolf dreams , forget he was i did for , stamped with 't was anguy guards pounding on wood , she you again .

    	, the old the castle ,     what  fat belly burst      his , nor any     , and if you fight like  wounded animal .

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

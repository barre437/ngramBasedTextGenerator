#!/usr/bin/python

'''
Title: Text generator using N-grams

Author: Melissa Barrett
email: barre437@d.umn.edu

Date: 10/6/2017

Goal:
	Generate text, using passed in text files as training material.
	3 different levels of training thoroughness.

	Unigrams: Picks single words randomly, based on their probability.
	Bigrams: Picks sets of two words randomly, based on the probability of 
		those two words appearing together.
	Trigrams: Picks sets of three words randomly, based on the probability of
		those three words appearing together.
	
	The generated text is more readable with the higher value ngrams.

	Tasks include lowercasing all words, tokenizing words so they're by themselves,
	Splitting up sentences, and calculating frequency and probability of words
	and of sets of consecutive words.

	Makes significant use of NLTK toolkit functions.

'''

import random
import sys
import nltk

#Variable declaration
ngram = sys.argv[1]
sentences = sys.argv[2]
textTokens = []
textFDists = []
textSent = []

#randomly selects single words based on their frequency compared to total words
def unigram(n):
	currCount = 0
	wordMap = {}
	for dist in textFDists:
		for word in dist:
			if word not in wordMap:#adds word to map, adds range
				wordMap[word] = [xrange(currCount, currCount + dist[word])]
				currCount = currCount+ dist[word] + 1
			else:#Add second range to check. Could be 45-56, 78-90, not continuous range
				wordMap[word].append(xrange(currCount, currCount + dist[word]))
				currCount = currCount + dist[word] + 1
	#generates y sentences
	for y in range(0, int(n)):
		sent = ""
		while not sent.endswith(".") or sent.endswith("?") or sent.endswith("!"):
			sent = sent + " "
			rand = random.randint(0, wordCount)
			for k in wordMap:
				for v in wordMap[k]:
					if rand in v:
						sent = sent + k
		print str(y) + ": " + sent + "\n"
	return

#Randomly selects pairs of words based on their frequency compared to total amount of doubles
def bigram(n):
	#list to hold bigrams
	bgs = []
	#map to map bigrams to ranges
	bgMap = {}
	#counter that increments our range
	currCount = 0
	#Splits sentences into bigrams, adds all of them to bigram list
	for text in textSent:
		for sent in text:
			sentWords = nltk.word_tokenize(sent)
			for x in range(0, len(sentWords)):
				if(len(sentWords) < 2):
					continue
				if x == 0:
					bgs.append((sentWords[0], ' '))
				else:
					bgs.append((sentWords[x], sentWords[x-1])) 
	#calculates freqDist of bigrams
	bgFreqDist = nltk.FreqDist(bgs)
	#Assigns ranges to bigrams
	for bg in bgFreqDist:
		if bg not in bgMap:
			bgMap[bg] = [xrange(currCount, currCount + bgFreqDist[bg])]
			currCount = currCount + bgFreqDist[bg] + 1
		else:
			bgMap[bg].append(xrange(currCount, currCount + bgFreqDist[bg]))
			currCount = currCount + bgFreqDist[bg] + 1
	#Generates y sentences with bigrams
	for y in range(0, int(n)):
		sent = ""
		while not sent.endswith("."):
			sent = sent + " "
			rand = random.randint(0, currCount)
			for k in bgMap:
				for v in bgMap[k]:
					if rand in v:
						sent = sent + k[1] + " " + k[0]
		print str(y) + ": " + sent + "\n"
	return

#Ranomly selects triples of words based on their frequency compared to total amount of triples
def trigram(n):
	#holds trigrams
	tgs = []
	#maps trigrams to ranges
	tgMap = {}
	currCount = 0
	#Splits sentences into trigrams, ignores sentences less than 3 words long
	for text in textSent:
		for sent in text:
			sentWords = nltk.word_tokenize(sent)
			for x in range(0, len(sentWords)):
				if(len(sentWords) < 3):
					continue
				if x == 0:
					tgs.append((sentWords[0], ' ', ' '))
				elif x == 1:
					tgs.append((sentWords[1], sentWords[0], ' '))
				else:
					tgs.append((sentWords[x], sentWords[x-1], sentWords[x-2]))
	#Calculates frequncy distribution of trigrams
	tgFreqDist = nltk.FreqDist(tgs)
	#maps every trigrams to set of ranges
	for tg in tgFreqDist:
		if tg not in tgMap:
			tgMap[tg] = [xrange(currCount, currCount + tgFreqDist[tg])]
			currCount = currCount + tgFreqDist[tg] + 1
		else:
			tgMap[tg].append(xrange(currCount, currCount + tgFreqDist[tg]))
			CurrCount = currCount + tgFreqDist[tg] + 1
	#generates n sentences using trigrams
	for y in range(0, int(n)):
		sent = ""
		while not sent.endswith("."):
			sent = sent + " "
			rand = random.randint(0, currCount)
			for k in tgMap:
				for v in tgMap[k]:
					if rand in v:
						sent = sent + k[2] + " " + k[1] + " " + k[0]
		print str(y) + ": " + sent + "\n"
	
	return

print "This program generates random sentences based on an Ngram model. Melissa Barrett"

print "Command line settings: " + str(sys.argv[0]) + " " + str(sys.argv[1]) + " " + str(sys.argv[2])

#Preprocessing
#Opens files, tokenizes on words and sentences, stores them in lists, creates freqdists
#The decoding is only because some of the text files I was using were encoded weirdly.
#I used all of the NLTK functions I could find that could automate the work of tokenizing.
#word_tokenize, sent_tokenize, Text(objects), FreqDist, automated a lot of the busy work
for x in range(3, len(sys.argv)):
	print "Processing : " + str(sys.argv[x])

	f = open(sys.argv[x], 'rU')
	raw = f.read().decode('latin2')

	tokens = nltk.word_tokenize(raw)
	tokens = [w.lower() for w in tokens]
	sentTokens = nltk.sent_tokenize(raw)
	sentTokens = [w.lower() for w in sentTokens]

	textSent.append(nltk.Text(sentTokens))
	textTokens.append(nltk.Text(tokens))

	fdist = nltk.FreqDist(w for w in tokens)
	textFDists.append(fdist)

wordCount = 0
uniqueWordCount = 0

#Calculates total words and unique words
for x in range(0, len(textTokens)):
	wordCount = wordCount + len(textTokens[x])
	uniqueWordCount = uniqueWordCount + len(set(textTokens[x]))

print "Words : " + str(wordCount)
print "Unique words : " + str(uniqueWordCount)

#main, looks to arguments to figure out which function to run
def main():
	if int(ngram) == 1:
		unigram(sentences)
	if int(ngram) == 2:
		bigram(sentences)
	if int(ngram) == 3:
		trigram(sentences)
	return

if __name__ == '__main__':
	main()

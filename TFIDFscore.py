
from __future__ import division
import re
from stemming import porter2
import math
import json
import os
from operator import itemgetter

import nltk
import tweetcollector

def tokenize(text):
	"""
    Take a string and split it into tokens on word boundaries.
      
    A token is defined to be one or more alphanumeric characters,
    underscores, or apostrophes.  Remove all other punctuation, whitespace, and
    empty tokens.  Do case-folding to make everything lowercase. This function
    should return a list of the tokens in the input string.
	"""
	tokens = re.findall("[\w']+", text.lower())
	return [porter2.stem(token) for token in tokens]

class TFIDF(object):
	""" A search engine for tweets. """
	def __init__(self, ranker=None, classifier=None):
		"""
		purpose: Create the search engine for tweets
		parameters:
			database - store tweets information
		"""
        # database will be used to store tweets
		self.mytweets = []
		self.nltk_tweets = []
		
		twitter_user = 'badgerslkehoney'
		
		tweet_collect = tweetcollector.TweetCollector()
		tweets = tweet_collect.CollectTweets(twitter_user)
		self.mytweets = tokenize(tweets)
		
		for word, tag in nltk.pos_tag(nltk.word_tokenize(tweets)):
			self.nltk_tweets.append(tag)
		
		
		# dictionary to store script info
		self.scripts = {}
		self.nltk_scripts = {}
		
		f_harry = open('harry_lines.txt', 'r')
		harry_lines = f_harry.read()
		self.scripts['harry']= tokenize(harry_lines)
		#print nltk.pos_tag(nltk.word_tokenize(harry_lines))
		self.nltk_scripts['harry'] = []
		for word, tag in nltk.pos_tag(nltk.word_tokenize(harry_lines)):
			self.nltk_scripts['harry'].append(tag)
		
		f_hermione = open('hermione_lines.txt', 'r')
		hermione_lines = f_hermione.read()
		self.scripts['hermione']= tokenize(hermione_lines)
		self.nltk_scripts['hermione'] = []
		for word, tag in nltk.pos_tag(nltk.word_tokenize(hermione_lines)):
			self.nltk_scripts['hermione'].append(tag)
		
		f_ron = open('ron_lines.txt', 'r')
		ron_lines = f_ron.read()
		self.scripts['ron']= tokenize(ron_lines)
		self.nltk_scripts['ron'] = []
		for word, tag in nltk.pos_tag(nltk.word_tokenize(ron_lines)):
			self.nltk_scripts['ron'].append(tag)
		
		f_dumbledore = open('dumbledore_lines.txt', 'r')
		dumbledore_lines = f_dumbledore.read()
		self.scripts['dumbledore']= tokenize(dumbledore_lines)
		self.nltk_scripts['dumbledore'] = []
		for word, tag in nltk.pos_tag(nltk.word_tokenize(dumbledore_lines)):
			self.nltk_scripts['dumbledore'].append(tag)
		
		f_hagrid = open('hagrid_lines.txt', 'r')
		hagrid_lines = f_hagrid.read()
		self.scripts['hagrid']= tokenize(hagrid_lines)
		self.nltk_scripts['hagrid'] = []
		for word, tag in nltk.pos_tag(nltk.word_tokenize(hagrid_lines)):
			self.nltk_scripts['hagrid'].append(tag)
		
		f_draco = open('draco_lines.txt', 'r')
		draco_lines = f_draco.read()
		self.scripts['draco']= tokenize(draco_lines)
		self.nltk_scripts['draco'] = []
		for word, tag in nltk.pos_tag(nltk.word_tokenize(draco_lines)):
			self.nltk_scripts['draco'].append(tag)
		
		f_harry.close()
		f_hermione.close()
		f_ron.close()
		f_dumbledore.close()
		f_hagrid.close()
		f_draco.close()
		
		#print self.scripts['harry']
		
        # used to store the frequency of documents
		self.freq_docs = {}
        # you might need this which is used to store all terms/tokens in our documents
		self.word_list = []
		self.nltk_list = []
        # used to store inverted index information for all terms/tokens
		self.inverted_index = {}
		self.nltk_inverted_index = {}
		# member variable to store inverse doc frequency
		self.doc_tf_idf = {}
		self.nltk_doc_tf_idf = {}
		# 
		self.char_sim = {}
		self.nltk_sim = {}
	
	def _term_tf_idf(self, token, count):
		"""
		purpose: Calculate tf-idf for a token in the document
		parameters:
            token - 
            count - the number of occurrence of a term/token in one document
        return: term/token's tf-idf
		"""
		num_terms = len(self.word_list)
		df = len(self.inverted_index[token])
		idf = math.log(num_terms/df, 2)
		tf_idf = count * idf
        #print tf_idf
		return tf_idf
		
	def nltk_term_tf_idf(self, token, count):
		"""
		purpose: Calculate tf-idf for a token in the document
		parameters:
            token - 
            count - the number of occurrence of a term/token in one document
        return: term/token's tf-idf
		"""
		num_terms = len(self.nltk_list)
		df = len(self.nltk_inverted_index[token])
		idf = math.log(num_terms/df, 2)
		tf_idf = count * idf
        #print tf_idf
		return tf_idf	
		
               
	def CosineSim(self, vec_query, vec_doc):
		"""
        purpose: Calculate cosine similarity for two documents (vectors)
        parameters:
            vec_query - the vector with only raw term frequency for query
            vec_doc   - the vector of tf-idf for a document
        return: cosine similarity between the query and a document
		"""
		intersection = 0
		mag_query = 0
		mag_doc = 0
		for idx in range(0, len(vec_query)):
			intersection += vec_query[idx] * vec_doc[idx]
			mag_query += math.pow(vec_query[idx], 2)
			mag_doc += math.pow(vec_doc[idx], 2)
        
		mag_query = math.sqrt(mag_query)
		mag_doc = math.sqrt(mag_doc)

        #print intersection
        #print mag_query
        #print mag_doc
		
		cosine = intersection/(mag_query*mag_doc)
		return cosine
        
	def index_lines(self):
		"""
        purpose: process raw tweets and calculate tf-idf for all terms/tokens in tweets
        parameters:
          tweets - an iterator of tweet dictionaries
        returns: none
		"""
		for char in self.scripts.keys():
			lines = self.scripts[char]
			char_id = char
			tf = 1
			
			word_counter = {}
			
			for token in lines:
				if token not in self.word_list:
					self.word_list.append(token)
				if token not in self.inverted_index.keys():
					self.inverted_index[token] = []
					
				if token not in word_counter.keys():
					word_counter[token] = 1
				else:
					word_counter[token] += 1
				'''
				if [char_id] not in self.inverted_index[token]:
					self.inverted_index[token].append([char_id, tf])
				elif [char_id] in self.inverted_index[token]:
					print "Remove token"
					#self.inverted_index[token].remove([char_id, tf])
					tf += 1
					#self.inverted_index[token].append([char_id, tf])
				'''
			for word in word_counter.keys():
				self.inverted_index[word].append([char_id, word_counter[word]])
            
		print "lines indexed"
        #print self.word_list
		
		#print self.inverted_index
		
		num_terms = len(self.inverted_index)
		for token in self.inverted_index:
			t_list = self.inverted_index[token]
            
            #print term
            #print list
            #print idf
			for idx, count in t_list:
				#print idx
				if idx not in self.doc_tf_idf.keys():
					self.doc_tf_idf[idx] = []
				tf_idf = self._term_tf_idf(token, count)
				self.doc_tf_idf[idx].append([token, tf_idf])
		#print self.doc_tf_idf
		
	def index_nltk(self):
		"""
        purpose: process raw tweets and calculate tf-idf for all terms/tokens in tweets
        parameters:
          tweets - an iterator of tweet dictionaries
        returns: none
		"""
		for char in self.nltk_scripts.keys():
			lines = self.nltk_scripts[char]
			char_id = char
			tf = 1
			
			word_counter = {}
			
			for token in lines:
				if token not in self.nltk_list:
					self.nltk_list.append(token)
				if token not in self.nltk_inverted_index.keys():
					self.nltk_inverted_index[token] = []
					
				if token not in word_counter.keys():
					word_counter[token] = 1
				else:
					word_counter[token] += 1
			for word in word_counter.keys():
				self.nltk_inverted_index[word].append([char_id, word_counter[word]])
            
		print "nltk lines indexed"
        #print self.word_list
		
		#print self.inverted_index
		
		num_terms = len(self.nltk_inverted_index)
		for token in self.nltk_inverted_index:
			t_list = self.nltk_inverted_index[token]

			for idx, count in t_list:
				#print idx
				if idx not in self.nltk_doc_tf_idf.keys():
					self.nltk_doc_tf_idf[idx] = []
				tf_idf = self.nltk_term_tf_idf(token, count)
				self.nltk_doc_tf_idf[idx].append([token, tf_idf])

	def search_results(self):
		"""
        purpose: rank all tweets we have based on the query using 
                Vector Space Retrieval Model.
        preconditions: index_tweets() has already processed the corpus
        parameters:
                query - a string of terms
        returns: list of dictionaries containing the tweets which must have 
                the field "sim" in the data structure. 
		"""
		import operator
		docs = []
		#tokens = tokenize(query)
		
        #Make query vector from tweets
		query_vec = []
		for word in self.word_list:
			if word in self.mytweets:
				query_vec.append(self.mytweets.count(word))
			else:
				query_vec.append(0)

		#Make query vector from tweets for nltk
		nltk_query_vec = []
		for word in self.nltk_list:
			if word in self.nltk_tweets:
				nltk_query_vec.append(self.nltk_tweets.count(word))
			else:
				nltk_query_vec.append(0)		
				
		#print query_vec
		cosine_vals = []	
		cosine_nltk_vals = []
	
        #Make doc vectors for terms
		word_found = False
		for char in self.doc_tf_idf.keys():
			doc_vec = []
			for word in self.word_list:
				word_found = False
				for doc_word, tf_idf in self.doc_tf_idf[char]:
					if word == doc_word and not word_found:
						doc_vec.append(tf_idf)
						word_found = True
				if not word_found:
					doc_vec.append(0)
			cosine_vals.append([self.CosineSim(query_vec, doc_vec), char]) 	
			self.char_sim[char] = self.CosineSim(query_vec, doc_vec)
        
		
		#Make doc vectors for nltk
		word_found = False
		for char in self.nltk_doc_tf_idf.keys():
			doc_vec = []
			for word in self.nltk_list:
				word_found = False
				for doc_word, tf_idf in self.nltk_doc_tf_idf[char]:
					if word == doc_word and not word_found:
						doc_vec.append(tf_idf)
						word_found = True
				if not word_found:
					doc_vec.append(0)
			#cosine_nltk_vals.append([self.CosineSim(nltk_query_vec, doc_vec), char]) 	
			
			#print nltk_query_vec
			
			self.nltk_sim[char] = self.CosineSim(nltk_query_vec, doc_vec)
		
		
		character_sim = {}
		
		
		#print self.char_sim
		#print self
		
		for char1 in self.char_sim.keys():
			for char2 in self.nltk_sim.keys():
				val = self.char_sim[char1]+self.nltk_sim[char2]
				if char1 == char2:
					character_sim[char1] = val
					
		
		
		cosine_chars = sorted(character_sim.iteritems(), key=itemgetter(1), reverse = True)
		
		#cosine_chars = sorted(self.char_sim.iteritems(), key=itemgetter(1), reverse = True)
		#cosine_nltk_vals = sorted(self.nltk_sim.iteritems(), key=itemgetter(1), reverse = True)
		
		#print cosine_nltk_vals
		#print cosine_chars
        #print cosine_tweets[:5]		
		return cosine_chars[:6]
		
if __name__=="__main__":
	'''
    print "Test is starting..."
    _searcher = TweetSearch()                                                   # create our searcher
    tweets = read_data(os.path.join(os.getcwd(),'tamu_athletics_small.json'))   # read all tweets from json file
    _searcher.index_tweets(tweets)                                              # index tweets and calculate tf-idf
    #query = "johnny manziel"                                                    # example query
    query = "aggie football"
    output = _searcher.search_results(query)                                    # search query and get ranked tweets
    print "Starting to output ranked tweets-->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    for tweet in output:
        print str(tweet['sim']) + '\t' + tweet['text'].encode('utf-8')
	'''
	ranker = TFIDF()
	ranker.index_lines()
	ranker.index_nltk()
	print ranker.search_results()
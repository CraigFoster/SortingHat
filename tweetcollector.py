#!/usr/bin/env python
# -*- coding: utf-8  -*-
#encoding=utf-8

import tweepy
import json

class TweetCollector():
	def __init__(self):
		self.consumer_key = 'qrLjzRwU6p9roRlAZj8Q7g'
		self.consumer_secret = 'fKyVtYPo1vsPktDyGZTzzoI72j5CxC8WCcqViilqYlE'
		self.access_token_key = '754247172-o6vyiMZZGuz6N4dikOf22DzZtNID6S3LyV3rPu5o'
		self.access_token_secret = 'JUOlQSjU3fhoiq6UC0qQWFQqFz7mESzFflDXjqDU0'
		
		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token_key, self.access_token_secret)
		
		try:
			redirect_url = self.auth.get_authorization_url()
		except tweepy.TweepError:
			print 'Error! Failed to get request token.'

		self.api = tweepy.API(self.auth)
		

	def check_api_rate_limit(self, sleep_time):
		try:
			rate_limit_status = self.api.rate_limit_status()
		except Exception as error_message:
			if error_message['code'] == 88:
				print "Sleeping for %d seconds." %(sleep_time)
				print rate_limit_status['resources']['statuses']
				time.sleep(sleep_time)

			while rate_limit_status['resources']['statuses']['/statuses/user_timeline']['remaining'] < 10:
				print "Sleeping for %d seconds." %(sleep_time)
				print rate_limit_status['resources']['statuses']
				time.sleep(sleep_time)
				rate_limit_status = self.api.rate_limit_status()
			print rate_limit_status['resources']['statuses']['/statuses/user_timeline']
		
	def CollectTweets(self, username):
		#self.check_api_rate_limit(900)
		#print "Collecting"
		try:
			user = self.api.get_user(username)
			tweets = ""	
			
			for status in tweepy.Cursor(self.api.user_timeline,id=username).items(100): 
				tweets += status.__getstate__()['text'].encode("utf-8")
				#print status.__getstate__()['text'].encode("utf-8")+'\n'		
				
			return tweets
			
		except:
			#print 'error'
			return 'no user'		
			
		

if __name__ =='__main__':
	print "main"
	#TweetCollector()
	collector  = TweetCollector()
	collector.CollectTweets('feliciaday')
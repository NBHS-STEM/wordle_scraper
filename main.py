import tweepy
import os
import re
from collections import Counter


class WordleScraper(tweepy.StreamingClient):
    def __init__(self, bearer_token, puzzle):
        super().__init__(bearer_token)
        self.puzzle = puzzle
        self.data = Counter()
        if self.get_rules().data:
            self.delete_rules([rule.id for rule in self.get_rules().data])
        
    def scrape(self):
        self.add_rules(tweepy.StreamRule(f'Wordle {self.puzzle}'))
        self.filter(threaded=True)
    
    def on_tweet(self, tweet):
        print(tweet.text)

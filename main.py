from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time



class TwitterBot:
    def __init__(self):
        self.bot = webdriver.Firefox(executable_path=r"C:\Users\coryb\PycharmProjects\geckodriver.exe")

    def login(self, email, password):
        pass

    def grab_tweet_data(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=%23'+hashtag+'&f=live')
        time.sleep(4)
        tweet_data = []
        for i in range(0, 4):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(4)
            cells = bot.find_elements_by_xpath("//div[@data-testid='tweet']")
            for cell in cells:
                name = cell.find_element_by_xpath('.//span').text
                handle = cell.find_element_by_xpath("//span[contains(text(), '@')]").text
                content = cell.find_element_by_xpath('//div[2]/div[2]/div[2]/div').text
                likes = cell.find_element_by_xpath("//div[@data-testid='like']").text + ' likes'
                tweet = (name, handle, content, likes)
                tweet_data.append(tweet)
        bot.close()
        with open('tweet_dat.csv', 'w') as f:
            write = csv.writer(f)
            for tweet in tweet_data:
                write.writerow(tweet)

    def grab_elon_tweets(self):
        bot = self.bot
        bot.get('https://twitter.com/elonmusk')
        #check if its elon sending tweet if so
        # grab all tweet data and check for any keywords
        # search keywords against a list of stocks
        # if any matches return the stock name and current price
        time.sleep(4)
        tweet_data = []
        for i in range(0, 3):
            cells = bot.find_elements_by_xpath("//div[@data-testid='tweet']")
            for cell in cells:
                name = cell.find_element_by_xpath('.//span').text
                if name == 'Elon Musk':
                    content = cell.find_element_by_xpath('//div[2]/div[2]/div[2]/div').text
                    likes = cell.find_element_by_xpath("//div[@data-testid='like']").text + ' likes'
                    tweet = (name, content, likes)
                    tweet_data.append(tweet)
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(4)

        print(tweet_data)


musk = TwitterBot()
#musk.grab_tweet_data('bitcoin')
musk.grab_elon_tweets()
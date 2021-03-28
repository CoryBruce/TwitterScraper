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
        for i in range(0, 3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(4)
            cells = bot.find_elements_by_xpath("//div[@data-testid='tweet']")
            for cell in cells:
                name = cell.find_element_by_xpath('.//span').text
                handle = cell.find_element_by_xpath("//span[contains(text(), '@')]").text
                content = cell.find_element_by_xpath('*//div[2]/div[2]/div[1]').text
                likes = cell.find_element_by_xpath("//div[@data-testid='like']").text + ' likes'
                tweet = (name, handle, content, likes)
                tweet_data.append(tweet)
                #/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[7]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div

        bot.close()
        for tweet in tweet_data:
            print(tweet)



musk = TwitterBot()
musk.grab_tweet_data('bitcoin')
import time
import praw

r = praw.Reddit('Randomactofdogebot')
r.login("USERNAME","PASSWORD")
already_done = set()
prawWords = ['a', 'e', 'i', 'o', 'u']
# and sometimes Y. Including all the vowels makes the bot more random.
while True:
        def pick_random():
                subreddit = r.get_subreddit('dogecoin')
                subreddit_comments = subreddit.get_comments(limit=500)
                for comment in subreddit_comments:
                        op_text = comment.body
                        has_praw = any(string in op_text for string in prawWords)
                        if comment.id not in already_done and has_praw:
                                comment.reply('This is a random act of doge! +/u/dogetipbot 25 doge\n\nPlease consider tipping this bot to keep it running!\n\n[Bot Info](http://www.reddit.com/r/dogecoin/comments/1yi0s1/all_the_information_you_need_to_know_about_me/) ---- [Source Code](https://github.com/Healdb/random_act_of_doge_bot)')
                                already_done.add(comment.id)
                                break
                        
		
        pick_random()
        time.sleep(3600)

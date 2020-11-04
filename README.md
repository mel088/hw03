# Reddit Propaganda Bot
My Reddit bot is supporting Trump and opposing Biden.
I am apolitical so I wrote satirical comments.

[Here is a link to my favorite thread!](https://www.reddit.com/r/csci040temp/comments/jlwwob/trust_me_i_leaked_the_pentagon_papers_trump_is_an/gavehq9?utm_source=share&utm_medium=web2x&context=3)

Here is an image of my favorite thread:
![An image of my favorite thread](https://github.com/mel088/hw03/blob/main/Thread_Image.png)
This is my favorite thread because the comments are funny to me. One comment is mocking Trump calling him "Orange Man" while the other is kind of violent. My comment just says you should vote for trump because he has a big asset.

Here is the output of my `<bot_counter.py>`.
```
(base) Melanies-MacBook:hw3 melaniewilliamsmac$ /usr/local/bin/python3 /Users/melaniewilliamsmac/Documents/GitHub/mel088.github.io/.vscode/hw3/bot_counter.py
len(comments)= 1000
len(top_level_comments)= 19
len(replies)= 981
len(valid_top_level_comments)= 19
len(not_self_replies)= 913
len(valid_replies)= 548
========================================
valid_comments= 567
========================================
NOTE: the number valid_comments is what will be used to determine your extra credit
```
## 28/20
* 12 points - Successfully completed tasks 0-5.
* 2 points - Uploaded Github Repo.
* 2 points - Posted at least 100 comments.
* 1 point - Have your bot upvote any comment mentioning Trump. *I also had my bot downvote comments mentioning Biden.*
* 1 point - Have your bot upvote any submission mentioning Trump. *I also had my bot downvote submissions mentioning Biden.*
* 0-1 points - Make your bot reply to highly upvoted comments before replying to lower upvoted comments. *I'm not sure if I got this to work. I tried sorting comments by their score, but had trouble seeing if it was working or not since most of the comments are 1 point.*
* 1 point - If your bot writes more than 500 comments, you get this extra credit.
* 2 points - Have your bot post new submissions to the /r/csci040 subreddit.
* 2 points - Use the textblob library to measure the sentiment of every comment/submission.
* 4-5 points - Have the responses of your bot somehow depend on what the comment you are replying to is saying.

import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment functions from the week_07 lab here

def generate_comment_0():
    names = ['Donald', 'Trump', 'Mr. Trump', 'Trumppity Dumppity', 'Trumpty Dumpty', 'Lord Trump', 'Donald Trump']
    name = random.choice(names)

    jobs = ['president', 'leader of the free world', 'prez', 'king','supreme dictator']
    job = random.choice(jobs)

    gots = ['got', 'has', 'carries', 'posseses','is']
    got = random.choice(gots)

    assets = ['asset', 'kaboose', 'dumptruck', 'tonka truck','dumpy', 'cake']
    asset = random.choice(assets)

    deserves = ['deserves', 'gets', 'wants', 'should get','better get to']
    deserve = random.choice(deserves)

    text = name + " should be elected " + job + " because he " + got + " a " + asset + ". He " + deserve + " to sit it on the throne."
    return text

def generate_comment_1():
    names = ['Donald', 'Trump', 'Mr. Trump', 'Trumppity Dumppity', 'Trumpty Dumpty', 'Lord Trump', 'Donald Trump']
    name = random.choice(names)

    gots = ['got', 'has', 'carries', 'posseses','is']
    got = random.choice(gots)

    assets = ['asset', 'kaboose', 'dumptruck', 'tonka truck','dumpy', 'cake']
    asset = random.choice(assets)

    reallys = ['really', 'basically', 'practically', 'just','essentially']
    really = random.choice(reallys)

    nows = ['now', 'at this point', 'at this point in time', 'nowadays','these days']
    now = random.choice(nows)

    text = "You should vote for " + name + " because he " + got + " that " + asset + ". There's " + really + " no competition " + now + "."
    return text

def generate_comment_2():
    names = ['Donald', 'Lil Trump', 'Mr. Trump', 'Trumppity Dumppity', 'Trumpty Dumpty', 'Trumpy', 'Daddy Donald']
    name = random.choice(names)

    assets = ['asset', 'kaboose', 'dumptruck', 'tonka truck','dumpy', 'cake']
    asset = random.choice(assets)

    gots = ['got', 'has', 'carries', 'posseses','is']
    got = random.choice(gots)

    trumps = ['trump', 'win', 'dominate', 'destroy','crush']
    trump = random.choice(trumps)

    sees = ['see', 'watch', 'look at', 'observe','get to see']
    see = random.choice(sees)

    text = name + " is gonna " + trump + " this election because he " + got + " a valuable asset. Did you " + see + " him in the debate? He got that " + asset + ". He has my vote."
    return text

def generate_comment_3():
    names = ['Biden', 'Lil B', 'Baby Biden', 'J Biddy', 'Joe Star Biden', 'Joe', 'Joe Biden']
    name = random.choice(names)

    ews = ['too much', 'and it is weird', 'a little too much in my opinion', 'and it is getting on my nerves', 'and smelling them']
    ew = random.choice(ews)

    becauses = ['because', 'bc', 'cuz', 'since','cause']
    because = random.choice(becauses)

    loses = ['lose', 'fail', 'not win', 'get destroyed in','get only a few votes']
    lose = random.choice(loses)

    aints = ['aint having', 'aint gettin', 'wont get', 'cant have','does not get']
    aint = random.choice(aints)

    text = name + " is gonna " + lose + " this election " + because + " he likes kids " + ew + ". He " + aint + " my vote."
    return text

def generate_comment_4():
    names = ['Biden', 'Lil B', 'Baby Biden', 'J Biddy', 'Joe Star Biden', 'Joe', 'Joe Biden']
    name = random.choice(names)

    ews = ['old', 'aged', 'elderly', 'senile', 'senior']
    ew = random.choice(ews)

    wonts = ['wont', 'aint gone', 'aint gon', 'cant','will not']
    wont = random.choice(wonts)

    lives = ['live', 'last', 'survive', 'make it','be able to live']
    live = random.choice(lives)

    periods = ['.', '?', '!', '!!','!?']
    period = random.choice(periods)

    text = name + " is too " + ew + ". He " + wont + " " + live + " long enough to have a second term" + period
    return text

def generate_comment_5():
    names = ['Biden', 'Lil B', 'Baby Biden', 'J Biddy', 'Joe Star Biden', 'Joe', 'Joe Biden']
    name = random.choice(names)

    ews = ['old', 'aged', 'elderly', 'senile', 'senior']
    ew = random.choice(ews)

    gets = ['get', 'has', 'carries', 'possesses','is infected with']
    get = random.choice(gets)

    presidents = ['president', 'leader', 'prez', 'president of the US','dictator']
    president = random.choice(presidents)

    periods = ['.', '?', '!', '!!','!?']
    period = random.choice(periods)

    text = "I think " + name + " would be a bad " + president + " because he is too " + ew + ". If he " + get + " COVID, he won't make it" + period
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    #import random
    options = [0,1,2,3,4,5]
    choice = random.choice(options)
    if choice==0:
        return (generate_comment_0())
    if choice==1:
        return (generate_comment_1())
    if choice==2:
        return (generate_comment_2())
    if choice==3:
        return (generate_comment_3())
    if choice==4:
        return (generate_comment_4())
    if choice==5:
        return (generate_comment_5())
    text = ''
    return text

reddit = praw.Reddit('bot')

#def post_text(s):
    #choice = random.choice(['toplevel','reply'])
    #if choice=='toplevel':
       # pass
        #print('toplevel')
        #submission = reddit.submission(url='https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/')
        #submission.reply(s)
   # else:
        #print('reply')
       # comment = reddit.comment(url='https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/g9xdl0m/')
        #comment.reply(s)


#for i in range(10000):
   # generate_comment()
    #time.sleep(5)

# connect to reddit 
#reddit = praw.Reddit('bot')

# connect to the debate thread
#reddit_debate_url = 'https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/'
#reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhb20w/2020_debate_thread/'
#reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhmggg/from_hoangs_bot_1_how_sexist_abuse_of_women_in/'
#reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jhn4zb/from_hoangs_bot_1_trump_boasts_the_economy/'
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jn3fjq/mitch_mcconnell_just_adjourned_the_senate_until/'
submission = reddit.submission(url=reddit_debate_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
#start_time = datetime.datetime.now()
#CHANGE back to while
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    #comment = reddit.comment(url='https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/g8myvpc?utm_source=share&utm_medium=web2x&context=3')
    submission.comments.replace_more(limit=None)
    #change LIMIT to None
    all_comments = []
    #EXTRA CREDIT 3. Make your bot reply to highly upvoted comments before replying to lower upvoted comments.
    submission.comment_sort = "top"
    all_comments = submission.comments.list()
    #print(all_comments) - WORKS
    #all_comments.list()
    #all_comments.replace_more()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    my_bot = 'cs40-bot8'
    #for comment in submission.comments.list():
    for comment in all_comments:
        if str(comment.author) != 'cs40-bot8':
            not_my_comments.append(comment)
    print('not my comments =', len(not_my_comments))
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    ##print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    ###has_not_commented = len(not_my_comments) == len(all_comments)
    has_not_commented = len(not_my_comments) == len(all_comments)
    #if not has_commented:    
    #submission.reply(generate_comment())
    
    #if has_not_commented:
    if has_not_commented == True:
        try:
            submission.reply(generate_comment())
            print('commented')
        except praw.exceptions.RedditAPIException:
            print('time to sleep')
            time.sleep(15)
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over has_not_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not

        comments_without_replies = []
        score = comment.score
        #submission.comment_sort = "top"
        #comments = submission.comments.list()
        #sorted(comments_without_replies, key=score)
        print('The score of the comment is =', str(score))
        for comment in not_my_comments:
            response = False
            #if str(comment.author) != 'cs40-bot8':
                #response = False
            for reply in comment.replies:
                if str(reply.author) == 'cs40-bot8':
                    response = True
                else:
                    response = False
            if response == False:
                    #if str(submission.title) != '2020 Debate Thread':
                comments_without_replies.append(comment)
            else:
                pass
        
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
    try:
        comment = reddit.comment(id = random.choice(comments_without_replies))
        #score = comment.score
        #sorted(comments_without_replies, key=score)
        comment.reply(generate_comment())
        print('replied to a comment')
    except:
        pass
    
    
    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    top_submissions = reddit.subreddit('csci040temp').top(time_filter='month')

    if random.random() < 0.5:
        submission = reddit.submission(url=reddit_debate_url)
    else:
        submission = random.choice(list(top_submissions))
        print('top submission id =', submission)
    

    #EXTRA CREDIT
    '''
    #Textblob Sentiment Extra Credit
    protrump_comments= [generate_comment_0, generate_comment_1, generate_comment_2]
    pro_comment=random.choice(protrump_comments)
    protrump_comment=pro_comment()

    antibiden_comments= [generate_comment_3, generate_comment_4, generate_comment_5]
    anti_comment=random.choice(antibiden_comments)
    antibiden_comment=anti_comment()
    
    #rancom=random.choice(comments_without_replies)
    from textblob import TextBlob
    textblob = TextBlob(comment.body.lower())
    polarity = textblob.sentiment.polarity

    try:
        if 'trump' in comment.body.lower():
            if polarity <= 0:
                comment.reply(antibiden_comment)
            if polarity > 0:
                comment.reply(protrump_comment)
        if 'biden' in comment.body.lower():
            if polarity <= 0:
                comment.reply(protrump_comment)
            if polarity > 0:
                comment.reply(antibiden_comment)
        print('replied to random comment based on sentiment')
        #generate_comment()
    # else (meaning there is an error)
    except praw.exceptions.APIException:
        # this gets run if the try code fails;
        # python will not crash
        print('exception found')

        # python to wait 5 seconds before proceeding
        print('starting to sleep')
        time.sleep(15)
        print('done sleeping')
        if len(comments_without_replies) == 0:
            continue

#delete replies to my own comments
    for comment in all_comments:
        if str(comment.author) == 'cs40-bot8':
            response = True
            for reply in comment.replies:
                if str(reply.author) == 'cs40-bot8':
                    response = True
                    comment.delete()
                    print('deleted comment')

    #Upvote Comment Extra Credit
    for comment in all_comments:
        if 'trump' in comment.body.lower():
            comment.upvote()
    print('upvote comment')

    #Downvote Comment Extra Credit
    for comment in all_comments:
        if 'biden' in comment.body.lower():
            comment.downvote()
    print('downvote comment')


    #Upvote Submission Extra Credit
    for submission in reddit.subreddit("csci040temp").top("month"):
        if 'trump' in submission.title.lower():
            submission.upvote()
    print('upvote submission')

    #Downvote Submission Extra Credit
    for submission in reddit.subreddit("csci040temp").top("month"):
        if 'biden' in submission.title.lower():
            submission.downvote()
    print('downvote submission')
    
    #Create New Submission Extra Credit
    #top_submissions = reddit.subreddit('csci040temp').top(time_filter='month')
    
    for i in range(20):
        try:
            trump_top_submissions = reddit.subreddit('AskThe_Donald').top(time_filter='month')
            trump_submission = random.choice(list(trump_top_submissions))

            def generate_submission():
                text = str(trump_submission.title)
                return text
        
            reddit.subreddit('csci040temp').submit(generate_submission(), url=submission.url)
            print('trump submission =', trump_submission.title)
        except praw.exceptions.RedditAPIException:
            print('time to sleep')
            time.sleep(15)
    

#Have the responses of your bot somehow depend on what the comment you are replying to is saying. 
# For example, if you are writing a bot that supports Trump, you might detect if the previous comment 
# talks about Biden. If it does, you might reply Biden sucks, Trump is better. Alternatively, you might 
# detect that the previous comment mentioned Trump with a negative sentiment and reply I disagree, Trump 
# is actually really great. The amount of extra credit you get for this will vary depending on the 
# creativity of your idea.
    #Text Dependent Replies Extra Credit
    try:
        def generate_reply_covid():
            text = "Trump got covid and was fine. Now he understands it even more and can better help our nation."
            return text

        for comment in not_my_comments:
            if 'corona' or 'covid' or 'pandemic' or 'sick' in comment.body.lower():
                comment.reply(generate_reply_covid())
            else:
                pass
        print('replied covid')

        def generate_reply_smart():
            text = "Trump has a high IQ. He just says dumb things sometimes! We all make mistakes."
            return text

        for comment in not_my_comments:
            if 'smart' or 'intelligent' or 'stupid' in comment.body.lower():
                comment.reply(generate_reply_smart())
            else:
                pass
        print('replied smart')
    
    except praw.exceptions.APIException:
        # this gets run if the try code fails;
        # python will not crash
        print('exception found')

        # python to wait 5 seconds before proceeding
        print('starting to sleep')
        time.sleep(15)
        print('done sleeping')
        if len(comments_without_replies) == 0:
            continue
'''
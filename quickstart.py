"""
This template is written by @timgrossmann

What does this quickstart script aim to do?
- This script is automatically executed every 6h on my server via cron
"""
import itertools
import random
import time
from instapy import InstaPy
from instapy import smart_run
import logging

logging.basicConfig(filename="like_by_tag_log.txt",
                level=logging.INFO,
                format='%(levelname)s: %(asctime)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S')

# login credentials
insta_username = 'fantastic_nature_facts'
insta_password = 'quqqom-sobcyj-2zoGci'

dont_likes = ['sex', 'nude', 'naked', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy']

friends = ['list of friends I do not want to interact with']

like_tag_list = ['naturefacts','eco', 'sustainable', 'sustainability', 'ecofashion', 'bio',
                 'ethicalfashion', 'sustainablefashion', 'recycle']

accounts = ['accounts with similar content']

wait_time = random.randint(0, 200)
logging.log(logging.INFO, 'waiting for {} to start'.format(str(wait_time)))

time.sleep(wait_time)


# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=15000)

    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)

    session.set_user_interact(amount=1, randomize=True, percentage=95)
    session.set_do_follow(enabled=True, percentage=100)
    session.set_do_like(enabled=True, percentage=100)

    raw_comments = [
            ["This", "The", "Your"],
            ["photo", "picture", "pic", "shot", "snapshot"],
            ["is", "looks", "feels", "is really"],
            [
                "great",
                "super",
                "good",
                "very good",
                "good",
                "wow",
                "WOW",
                "cool",
                "GREAT",
                "magnificent",
                "magical",
                "very cool",
                "stylish",
                "beautiful",
                "so beautiful",
                "so stylish",
                "so professional",
                "lovely",
                "so lovely",
                "very lovely",
                "glorious",
                "so glorious",
                "very glorious",
                "adorable",
                "excellent",
                "amazing",
            ]
        ]

    comment_list_tuples = list(itertools.product(*raw_comments))
    comment_list = [' '.join(x) for x in comment_list_tuples]
    random.shuffle(comment_list)

    session.set_do_comment(enabled=True, percentage=90)
    session.set_comments(comment_list)

    # activity
    session.like_by_tags(like_tag_list, amount=random.randint(22, 28), interact=True, media='Photo',
                         skip_top_posts=False)
    session.unfollow_users(amount=200, nonFollowers=True,
                         style="RANDOM", sleep_delay=60)
    #session.unfollow_users(amount=random.randint(75, 150), nonFollowers=True, InstapyFollowed=(True, "all"), style="FIFO",
    #                       unfollow_after=42 * 60 * 60, sleep_delay=655)
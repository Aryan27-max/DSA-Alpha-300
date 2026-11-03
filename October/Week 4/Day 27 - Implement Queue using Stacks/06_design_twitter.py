# ============================================================
# Day 27 - VARIANT: Design Twitter  (LeetCode 355)
# ============================================================
# The question:
#   Build a mini Twitter:
#     postTweet(userId, tweetId)  - user posts a tweet
#     getNewsFeed(userId)         - the 10 most recent tweet ids from the
#                                   user AND everyone they follow, newest first
#     follow(followerId, followeeId), unfollow(followerId, followeeId)
#
# The big idea (each user's tweets are a stack; merge the stack tops):
#   Give every tweet an increasing time number. Each user's tweets go in
#   their own list - newest at the END (a stack: the top is the latest).
#   For a news feed, look at the TOP of every relevant user's stack,
#   take the newest one, move that user's pointer down one, repeat 10 times.
#   That's a k-way merge. The usual tool is a heap, but heapq is banned
#   until December, so we scan the k tops each time: O(10 * k) per feed.
# ============================================================


class TwitterBrute:
    # Brute force feed: collect every relevant tweet, insertion-sort by time, take 10.
    def __init__(self):
        self.time = 0
        self.tweets = {}        # user -> list of (time, tweetId)
        self.following = {}     # user -> set of followees

    def postTweet(self, userId, tweetId):
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        users = [userId]
        for f in self.following.get(userId, set()):
            users.append(f)
        everything = []
        for u in users:
            for t in self.tweets.get(u, []):
                everything.append(t)
        for i in range(1, len(everything)):          # insertion sort, newest first
            cur, j = everything[i], i - 1
            while j >= 0 and everything[j][0] < cur[0]:
                everything[j + 1] = everything[j]
                j -= 1
            everything[j + 1] = cur
        feed = []
        for i in range(len(everything)):
            if i == 10:
                break
            feed.append(everything[i][1])
        return feed

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            if followerId not in self.following:
                self.following[followerId] = set()
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}        # user -> list of (time, tweetId); newest at the end
        self.following = {}     # user -> set of followees

    def postTweet(self, userId, tweetId):
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))   # push onto the user's stack

    def getNewsFeed(self, userId):
        users = [userId]
        for f in self.following.get(userId, set()):
            users.append(f)

        pointer = {}                    # user -> index of their newest unread tweet
        for u in users:
            pointer[u] = len(self.tweets.get(u, [])) - 1

        feed = []
        while len(feed) < 10:
            best_user = None
            best_time = -1
            for u in users:             # look at the top of every stack
                p = pointer[u]
                if p >= 0 and self.tweets[u][p][0] > best_time:
                    best_time = self.tweets[u][p][0]
                    best_user = u
            if best_user is None:
                break                   # nobody has tweets left
            feed.append(self.tweets[best_user][pointer[best_user]][1])
            pointer[best_user] -= 1     # "pop" that tweet for this feed
        return feed

    def follow(self, followerId, followeeId):
        if followerId == followeeId:
            return
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)


if __name__ == "__main__":
    tw = Twitter()
    tw.postTweet(1, 5)
    print(tw.getNewsFeed(1))   # [5]
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    print(tw.getNewsFeed(1))   # [6, 5]
    tw.unfollow(1, 2)
    print(tw.getNewsFeed(1))   # [5]

# 355. Design Twitter

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-twitter/)

## Problem

Design a simplified Twitter:
* `postTweet(userId, tweetId)`;
* `getNewsFeed(userId)`: the 10 most recent tweet ids posted by the user or anyone they follow, newest first;
* `follow(followerId, followeeId)` and `unfollow(followerId, followeeId)`.

**Example**
```
postTweet(1,5); getNewsFeed(1) → [5]; follow(1,2); postTweet(2,6);
getNewsFeed(1) → [6,5]; unfollow(1,2); getNewsFeed(1) → [5]
```

**Constraints**
* At most `3 * 10^4` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-maps-k-way-merge](v1-hash-maps-k-way-merge/README.md) | Hash maps + k-way merge | `O(F log F)` | `O(T + E)` | [▶ animation](v1-hash-maps-k-way-merge/animation/index.html) |

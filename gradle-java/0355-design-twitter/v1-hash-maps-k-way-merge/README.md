# 355. Design Twitter — v1: Hash maps + k-way merge

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

## Approach: Hash maps + k-way merge

> Each user's tweets are a newest-first list; a news feed merges the lists of the user and their followees with a heap.

**Own hash maps.** `MyHashMap<user, List<tweet>>` (tweets stored with a global timestamp) and `MyHashMap<user, MyHashSet<followee>>`.
`getNewsFeed` pushes the newest tweet of each relevant user into a max-heap by time, then pops up to 10 times, each time pushing that user's
next-older tweet.

* Time: **O(F log F)** — per feed, where F is the number of followees (posting and following are O(1)).
* Space: **O(T + E)** — all tweets and follow links.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0355/v1/Twitter.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0355/v1/TwitterTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle 9.8.2 project. Only a JDK is needed to start Gradle; JDK 25 is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.

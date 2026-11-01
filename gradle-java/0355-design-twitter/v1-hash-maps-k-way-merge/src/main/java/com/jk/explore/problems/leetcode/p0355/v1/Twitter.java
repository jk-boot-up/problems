package com.jk.explore.problems.leetcode.p0355.v1;

import java.util.*;

public class Twitter {

    private record Tweet(int id, int time) { }

    private final MyHashMap<Integer, List<Tweet>> tweets = new MyHashMap<>();
    private final MyHashMap<Integer, MyHashSet<Integer>> follows = new MyHashMap<>();
    private int clock;

    public void postTweet(int userId, int tweetId) {
        tweets.computeIfAbsent(userId, k -> new ArrayList<>()).add(new Tweet(tweetId, clock++));
    }

    public List<Integer> getNewsFeed(int userId) {
        // heap entries: {time, userId, index into that user's list}
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        List<Integer> users = new ArrayList<>(List.of(userId));
        MyHashSet<Integer> f = follows.get(userId);
        if (f != null) for (int u : f) if (u != userId) users.add(u);
        for (int u : users) {
            List<Tweet> list = tweets.get(u);
            if (list != null && !list.isEmpty()) heap.add(new int[]{list.getLast().time(), u, list.size() - 1});
        }
        List<Integer> feed = new ArrayList<>();
        while (feed.size() < 10 && !heap.isEmpty()) {
            int[] top = heap.poll();
            List<Tweet> list = tweets.get(top[1]);
            feed.add(list.get(top[2]).id());
            if (top[2] > 0) heap.add(new int[]{list.get(top[2] - 1).time(), top[1], top[2] - 1});
        }
        return feed;
    }

    public void follow(int followerId, int followeeId) {
        follows.computeIfAbsent(followerId, k -> new MyHashSet<>()).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        MyHashSet<Integer> f = follows.get(followerId);
        if (f != null) f.remove(followeeId);
    }
}

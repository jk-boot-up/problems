package com.jk.explore.problems.leetcode.p0950.v1;

import java.util.*;

public class RevealCardsIncreasing {

    public int[] deckRevealedIncreasing(int[] deck) {
        int n = deck.length;
        int[] sorted = deck.clone(), out = new int[n];
        Arrays.sort(sorted);
        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) queue.add(i);
        for (int card : sorted) {
            out[queue.poll()] = card;
            if (!queue.isEmpty()) queue.add(queue.poll());
        }
        return out;
    }
}

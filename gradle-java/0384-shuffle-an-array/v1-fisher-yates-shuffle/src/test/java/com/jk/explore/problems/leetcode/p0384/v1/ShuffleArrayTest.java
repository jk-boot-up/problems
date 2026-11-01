package com.jk.explore.problems.leetcode.p0384.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ShuffleArrayTest {

    @Test
    void resetAndPermutation() {
        ShuffleArray s = new ShuffleArray(new int[]{1, 2, 3, 4, 5});
        int[] shuffled = s.shuffle();
        int[] sorted = shuffled.clone();
        Arrays.sort(sorted);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, sorted);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, s.reset());
    }

    @Test
    void allPermutationsEquallyLikely() {
        ShuffleArray s = new ShuffleArray(new int[]{1, 2, 3}, new Random(1));
        TreeMap<String, Integer> seen = new TreeMap<>();
        int draws = 60_000;
        for (int i = 0; i < draws; i++) seen.merge(Arrays.toString(s.shuffle()), 1, Integer::sum);
        assertEquals(6, seen.size());
        for (int c : seen.values()) assertEquals(draws / 6.0, c, draws * 0.01);
    }
}

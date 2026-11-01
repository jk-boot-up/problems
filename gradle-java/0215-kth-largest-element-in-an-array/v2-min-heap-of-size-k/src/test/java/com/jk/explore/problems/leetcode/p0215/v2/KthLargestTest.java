package com.jk.explore.problems.leetcode.p0215.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KthLargestTest {

    private final KthLargest solution = new KthLargest();

    @Test
    void examples() {
        assertEquals(5, solution.findKthLargest(new int[]{3, 2, 1, 5, 6, 4}, 2));
        assertEquals(4, solution.findKthLargest(new int[]{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4));
    }

    @Test
    void duplicates() {
        assertEquals(1, solution.findKthLargest(new int[]{1, 1, 1, 1}, 3));
    }

    @Test
    void randomAgainstSort() {
        Random rnd = new Random(3);
        int[] a = rnd.ints(2000, -100, 100).toArray();
        int[] s = a.clone();
        Arrays.sort(s);
        for (int k : new int[]{1, 7, 1000, 2000}) assertEquals(s[s.length - k], solution.findKthLargest(a, k));
    }
}

package com.jk.explore.problems.leetcode.p0315.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CountSmallerTest {

    private final CountSmaller solution = new CountSmaller();

    @Test
    void examples() {
        assertEquals(List.of(2, 1, 1, 0), solution.countSmaller(new int[]{5, 2, 6, 1}));
        assertEquals(List.of(0), solution.countSmaller(new int[]{-1}));
        assertEquals(List.of(0, 0), solution.countSmaller(new int[]{-1, -1}));
        assertEquals(List.of(2, 0, 0), solution.countSmaller(new int[]{2, 0, 1}));
    }

    @Test
    void matchesBruteForce() {
        Random rnd = new Random(3);
        int[] a = new int[300];
        for (int i = 0; i < a.length; i++) a[i] = rnd.nextInt(41) - 20;
        List<Integer> got = solution.countSmaller(a);
        for (int i = 0; i < a.length; i++) {
            int c = 0;
            for (int j = i + 1; j < a.length; j++) if (a[j] < a[i]) c++;
            assertEquals(c, got.get(i));
        }
    }
}

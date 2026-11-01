package com.jk.explore.problems.leetcode.p0912.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SortAnArrayTest {

    private final SortAnArray solution = new SortAnArray();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 2, 3, 5}, solution.sortArray(new int[]{5, 2, 3, 1}));
        assertArrayEquals(new int[]{0, 0, 1, 1, 2, 5}, solution.sortArray(new int[]{5, 1, 1, 2, 0, 0}));
    }

    @Test
    void random() {
        int[] a = new Random(5).ints(5000, -50000, 50000).toArray();
        int[] e = a.clone();
        Arrays.sort(e);
        assertArrayEquals(e, solution.sortArray(a));
    }
}

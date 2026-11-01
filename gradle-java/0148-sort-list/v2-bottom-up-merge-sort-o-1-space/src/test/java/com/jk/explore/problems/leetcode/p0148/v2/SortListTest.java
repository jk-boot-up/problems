package com.jk.explore.problems.leetcode.p0148.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SortListTest {

    private final SortList solution = new SortList();

    @Test
    void four() {
        assertArrayEquals(new int[]{1, 2, 3, 4}, ListNode.toArray(solution.sortList(ListNode.of(4, 2, 1, 3))));
    }

    @Test
    void withNegatives() {
        assertArrayEquals(new int[]{-1, 0, 3, 4, 5}, ListNode.toArray(solution.sortList(ListNode.of(-1, 5, 3, 4, 0))));
    }

    @Test
    void empty() {
        assertNull(solution.sortList(null));
    }

    @Test
    void random() {
        Random rnd = new Random(7);
        int[] values = rnd.ints(1000, -100, 100).toArray();
        int[] expected = values.clone();
        Arrays.sort(expected);
        assertArrayEquals(expected, ListNode.toArray(solution.sortList(ListNode.of(values))));
    }
}

package com.jk.explore.problems.leetcode.p0147.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class InsertionSortListTest {

    private final InsertionSortList solution = new InsertionSortList();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 2, 3, 4}, ListNode.toArray(solution.insertionSortList(ListNode.of(4, 2, 1, 3))));
        assertArrayEquals(new int[]{-1, 0, 3, 4, 5}, ListNode.toArray(solution.insertionSortList(ListNode.of(-1, 5, 3, 4, 0))));
    }
}

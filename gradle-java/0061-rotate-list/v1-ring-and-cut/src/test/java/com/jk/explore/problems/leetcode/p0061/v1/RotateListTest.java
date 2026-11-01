package com.jk.explore.problems.leetcode.p0061.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RotateListTest {

    private final RotateList solution = new RotateList();

    @Test
    void byTwo() {
        assertArrayEquals(new int[]{4, 5, 1, 2, 3}, ListNode.toArray(solution.rotateRight(ListNode.of(1, 2, 3, 4, 5), 2)));
    }

    @Test
    void kLargerThanLength() {
        assertArrayEquals(new int[]{2, 0, 1}, ListNode.toArray(solution.rotateRight(ListNode.of(0, 1, 2), 4)));
    }

    @Test
    void empty() {
        assertNull(solution.rotateRight(null, 3));
    }
}

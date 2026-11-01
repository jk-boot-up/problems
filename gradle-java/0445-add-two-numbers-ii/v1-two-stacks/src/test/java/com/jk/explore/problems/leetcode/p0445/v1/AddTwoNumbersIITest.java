package com.jk.explore.problems.leetcode.p0445.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AddTwoNumbersIITest {

    private final AddTwoNumbersII solution = new AddTwoNumbersII();

    @Test
    void examples() {
        assertArrayEquals(new int[]{7, 8, 0, 7}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(7, 2, 4, 3), ListNode.of(5, 6, 4))));
        assertArrayEquals(new int[]{8, 0, 7}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(2, 4, 3), ListNode.of(5, 6, 4))));
        assertArrayEquals(new int[]{0}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(0), ListNode.of(0))));
        assertArrayEquals(new int[]{1, 0}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(5), ListNode.of(5))));
        assertArrayEquals(new int[]{1, 0, 0, 0}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(9, 9, 9), ListNode.of(1))));
    }
}

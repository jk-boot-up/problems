package com.jk.explore.problems.leetcode.p0002.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AddTwoNumbersTest {

    private final AddTwoNumbers solution = new AddTwoNumbers();

    @Test
    void example1() {
        assertArrayEquals(new int[]{7, 0, 8}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(2, 4, 3), ListNode.of(5, 6, 4))));
    }

    @Test
    void zeros() {
        assertArrayEquals(new int[]{0}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(0), ListNode.of(0))));
    }

    @Test
    void carryOut() {
        assertArrayEquals(new int[]{8, 9, 0, 0, 1}, ListNode.toArray(solution.addTwoNumbers(ListNode.of(9, 9, 9, 9), ListNode.of(9, 9))));
    }
}

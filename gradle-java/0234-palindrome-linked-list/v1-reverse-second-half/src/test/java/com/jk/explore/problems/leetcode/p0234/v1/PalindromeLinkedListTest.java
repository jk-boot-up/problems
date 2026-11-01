package com.jk.explore.problems.leetcode.p0234.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PalindromeLinkedListTest {

    private final PalindromeLinkedList solution = new PalindromeLinkedList();

    @Test
    void examples() {
        assertTrue(solution.isPalindrome(ListNode.of(1, 2, 2, 1)));
        assertFalse(solution.isPalindrome(ListNode.of(1, 2)));
        assertTrue(solution.isPalindrome(ListNode.of(1, 2, 3, 2, 1)));
    }
}

package com.jk.explore.problems.leetcode.p0173.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BSTIteratorTest {

    @Test
    void example() {
        BSTIterator it = new BSTIterator(TreeNode.of(7, 3, 15, null, null, 9, 20));
        assertEquals(3, it.next());
        assertEquals(7, it.next());
        assertTrue(it.hasNext());
        assertEquals(9, it.next());
        assertEquals(15, it.next());
        assertEquals(20, it.next());
        assertFalse(it.hasNext());
    }

    @Test
    void single() {
        BSTIterator it = new BSTIterator(TreeNode.of(1));
        assertEquals(1, it.next());
        assertFalse(it.hasNext());
    }
}

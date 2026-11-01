package com.jk.explore.problems.leetcode.p0284.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PeekingIteratorTest {

    @Test
    void example() {
        PeekingIterator it = new PeekingIterator(List.of(1, 2, 3).iterator());
        assertEquals(1, it.next());
        assertEquals(2, it.peek());
        assertEquals(2, it.peek());
        assertEquals(2, it.next());
        assertEquals(3, it.next());
        assertFalse(it.hasNext());
        assertThrows(NoSuchElementException.class, it::next);
    }

    @Test
    void peekFirstAndEmpty() {
        PeekingIterator it = new PeekingIterator(List.of(7).iterator());
        assertTrue(it.hasNext());
        assertEquals(7, it.peek());
        assertEquals(7, it.next());
        assertFalse(it.hasNext());
        assertFalse(new PeekingIterator(new ArrayList<Integer>().iterator()).hasNext());
    }
}

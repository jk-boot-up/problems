package com.jk.explore.problems.leetcode.p0622.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MyCircularQueueTest {

    @Test
    void example() {
        MyCircularQueue q = new MyCircularQueue(3);
        assertTrue(q.enQueue(1));
        assertTrue(q.enQueue(2));
        assertTrue(q.enQueue(3));
        assertFalse(q.enQueue(4));
        assertEquals(3, q.Rear());
        assertTrue(q.isFull());
        assertTrue(q.deQueue());
        assertTrue(q.enQueue(4));
        assertEquals(4, q.Rear());
        assertEquals(2, q.Front());
    }

    @Test
    void emptyQueue() {
        MyCircularQueue q = new MyCircularQueue(1);
        assertTrue(q.isEmpty());
        assertEquals(-1, q.Front());
        assertEquals(-1, q.Rear());
        assertFalse(q.deQueue());
        assertTrue(q.enQueue(9));
        assertTrue(q.isFull());
        assertTrue(q.deQueue());
        assertTrue(q.isEmpty());
    }
}

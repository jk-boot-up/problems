package com.jk.explore.problems.leetcode.p0225.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MyStackTest {

    @Test
    void example() {
        MyStack s = new MyStack();
        s.push(1);
        s.push(2);
        assertEquals(2, s.top());
        assertEquals(2, s.pop());
        assertFalse(s.empty());
        s.push(3);
        assertEquals(3, s.pop());
        assertEquals(1, s.pop());
        assertTrue(s.empty());
    }
}

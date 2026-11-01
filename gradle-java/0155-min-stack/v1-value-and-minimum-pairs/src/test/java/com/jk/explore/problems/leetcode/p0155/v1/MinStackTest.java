package com.jk.explore.problems.leetcode.p0155.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinStackTest {

    @Test
    void example() {
        MinStack s = new MinStack();
        s.push(-2);
        s.push(0);
        s.push(-3);
        assertEquals(-3, s.getMin());
        s.pop();
        assertEquals(0, s.top());
        assertEquals(-2, s.getMin());
    }

    @Test
    void duplicatesOfMinimum() {
        MinStack s = new MinStack();
        s.push(1);
        s.push(1);
        s.pop();
        assertEquals(1, s.getMin());
    }
}

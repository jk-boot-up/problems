package com.jk.explore.problems.leetcode.p1381.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CustomStackTest {

    @Test
    void example() {
        CustomStack s = new CustomStack(3);
        s.push(1);
        s.push(2);
        assertEquals(2, s.pop());
        s.push(2);
        s.push(3);
        s.push(4);
        s.increment(5, 100);
        s.increment(2, 100);
        assertEquals(103, s.pop());
        assertEquals(202, s.pop());
        assertEquals(201, s.pop());
        assertEquals(-1, s.pop());
    }

    @Test
    void incrementOnEmptyAndReuse() {
        CustomStack s = new CustomStack(2);
        s.increment(3, 5);
        s.push(1);
        s.increment(1, 10);
        assertEquals(11, s.pop());
        s.push(7);
        assertEquals(7, s.pop());
    }
}

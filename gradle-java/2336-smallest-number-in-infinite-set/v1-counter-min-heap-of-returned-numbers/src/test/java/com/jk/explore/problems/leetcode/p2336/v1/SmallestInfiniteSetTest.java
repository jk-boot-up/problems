package com.jk.explore.problems.leetcode.p2336.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SmallestInfiniteSetTest {

    @Test
    void example() {
        SmallestInfiniteSet s = new SmallestInfiniteSet();
        s.addBack(2);
        assertEquals(1, s.popSmallest());
        assertEquals(2, s.popSmallest());
        assertEquals(3, s.popSmallest());
        s.addBack(1);
        s.addBack(1);
        assertEquals(1, s.popSmallest());
        assertEquals(4, s.popSmallest());
        assertEquals(5, s.popSmallest());
    }
}

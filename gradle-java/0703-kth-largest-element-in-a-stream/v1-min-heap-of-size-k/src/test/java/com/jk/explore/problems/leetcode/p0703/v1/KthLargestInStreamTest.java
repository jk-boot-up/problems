package com.jk.explore.problems.leetcode.p0703.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KthLargestInStreamTest {

    @Test
    void example() {
        KthLargestInStream s = new KthLargestInStream(3, new int[]{4, 5, 8, 2});
        assertEquals(4, s.add(3));
        assertEquals(5, s.add(5));
        assertEquals(5, s.add(10));
        assertEquals(8, s.add(9));
        assertEquals(8, s.add(4));
    }
}

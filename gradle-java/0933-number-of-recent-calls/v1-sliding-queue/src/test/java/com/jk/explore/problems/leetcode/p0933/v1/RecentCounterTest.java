package com.jk.explore.problems.leetcode.p0933.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RecentCounterTest {

    @Test
    void example() {
        RecentCounter r = new RecentCounter();
        assertEquals(1, r.ping(1));
        assertEquals(2, r.ping(100));
        assertEquals(3, r.ping(3001));
        assertEquals(3, r.ping(3002));
    }
}

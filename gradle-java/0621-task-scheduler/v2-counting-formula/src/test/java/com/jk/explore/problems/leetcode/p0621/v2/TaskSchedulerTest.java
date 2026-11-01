package com.jk.explore.problems.leetcode.p0621.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TaskSchedulerTest {

    private final TaskScheduler solution = new TaskScheduler();

    @Test
    void examples() {
        assertEquals(8, solution.leastInterval("AAABBB".toCharArray(), 2));
        assertEquals(6, solution.leastInterval("ACABDB".toCharArray(), 1));
        assertEquals(10, solution.leastInterval("AAABBB".toCharArray(), 3));
        assertEquals(6, solution.leastInterval("AAABBB".toCharArray(), 0));
    }
}

package com.jk.explore.problems.leetcode.p0752.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class OpenTheLockTest {

    private final OpenTheLock solution = new OpenTheLock();

    @Test
    void examples() {
        assertEquals(6, solution.openLock(new String[]{"0201", "0101", "0102", "1212", "2002"}, "0202"));
        assertEquals(1, solution.openLock(new String[]{"8888"}, "0009"));
        assertEquals(-1, solution.openLock(new String[]{"8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"}, "8888"));
        assertEquals(-1, solution.openLock(new String[]{"0000"}, "8888"));
        assertEquals(0, solution.openLock(new String[]{"1111"}, "0000"));
        assertEquals(20, solution.openLock(new String[]{}, "5555"));
    }
}

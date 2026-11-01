package com.jk.explore.problems.leetcode.p0319.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BulbSwitcherTest {

    private final BulbSwitcher solution = new BulbSwitcher();

    @ParameterizedTest
    @CsvSource({"0,0", "1,1", "3,1", "4,2", "10,3", "99,9", "100,10", "1000000000,31622"})
    void bulbs(int n, int expected) {
        assertEquals(expected, solution.bulbSwitch(n));
    }

    @Test
    void matchesSimulation() {
        for (int n = 0; n <= 60; n++) {
            boolean[] on = new boolean[n + 1];
            for (int i = 1; i <= n; i++) for (int k = i; k <= n; k += i) on[k] = !on[k];
            int c = 0;
            for (int k = 1; k <= n; k++) if (on[k]) c++;
            assertEquals(c, solution.bulbSwitch(n));
        }
    }
}

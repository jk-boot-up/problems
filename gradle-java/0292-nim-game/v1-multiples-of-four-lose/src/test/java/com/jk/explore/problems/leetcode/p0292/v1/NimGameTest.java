package com.jk.explore.problems.leetcode.p0292.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NimGameTest {

    private final NimGame solution = new NimGame();

    @ParameterizedTest
    @CsvSource({"1,true", "2,true", "3,true", "4,false", "5,true", "8,false", "2147483647,true", "2147483644,false"})
    void wins(int n, boolean expected) {
        assertEquals(expected, solution.canWinNim(n));
    }

    @Test
    void matchesGameTree() {
        boolean[] win = new boolean[60];
        for (int n = 1; n < 60; n++) for (int k = 1; k <= 3 && k <= n; k++) if (!win[n - k]) win[n] = true;
        for (int n = 1; n < 60; n++) assertEquals(win[n], solution.canWinNim(n));
    }
}

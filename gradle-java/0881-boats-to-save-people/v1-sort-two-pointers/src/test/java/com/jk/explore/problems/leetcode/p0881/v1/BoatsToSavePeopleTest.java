package com.jk.explore.problems.leetcode.p0881.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BoatsToSavePeopleTest {

    private final BoatsToSavePeople solution = new BoatsToSavePeople();

    @Test
    void examples() {
        assertEquals(1, solution.numRescueBoats(new int[]{1, 2}, 3));
        assertEquals(3, solution.numRescueBoats(new int[]{3, 2, 2, 1}, 3));
        assertEquals(4, solution.numRescueBoats(new int[]{3, 5, 3, 4}, 5));
    }
}

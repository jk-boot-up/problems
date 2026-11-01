package com.jk.explore.problems.leetcode.p0268.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MissingNumberTest {

    private final MissingNumber solution = new MissingNumber();

    @Test
    void examples() {
        assertEquals(2, solution.missingNumber(new int[]{3, 0, 1}));
        assertEquals(2, solution.missingNumber(new int[]{0, 1}));
        assertEquals(8, solution.missingNumber(new int[]{9, 6, 4, 2, 3, 5, 7, 0, 1}));
    }

    @Test
    void zeroMissing() {
        assertEquals(0, solution.missingNumber(new int[]{1}));
    }
}

package com.jk.explore.problems.leetcode.p0790.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DominoTrominoTilingTest {

    private final DominoTrominoTiling solution = new DominoTrominoTiling();

    @ParameterizedTest
    @CsvSource({"1,1", "2,2", "3,5", "4,11", "5,24", "30,312342182"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.numTilings(n));
    }
}

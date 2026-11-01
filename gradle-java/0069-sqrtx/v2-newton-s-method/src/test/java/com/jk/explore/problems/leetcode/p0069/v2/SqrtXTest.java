package com.jk.explore.problems.leetcode.p0069.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SqrtXTest {

    private final SqrtX solution = new SqrtX();

    @ParameterizedTest
    @CsvSource({"0,0", "1,1", "4,2", "8,2", "15,3", "16,4", "2147395599,46339", "2147483647,46340"})
    void roots(int x, int expected) {
        assertEquals(expected, solution.mySqrt(x));
    }
}

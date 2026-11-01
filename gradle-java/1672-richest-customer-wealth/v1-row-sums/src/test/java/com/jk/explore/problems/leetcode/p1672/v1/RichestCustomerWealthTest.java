package com.jk.explore.problems.leetcode.p1672.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RichestCustomerWealthTest {

    private final RichestCustomerWealth solution = new RichestCustomerWealth();

    @Test
    void examples() {
        assertEquals(6, solution.maximumWealth(new int[][]{{1, 2, 3}, {3, 2, 1}}));
        assertEquals(10, solution.maximumWealth(new int[][]{{1, 5}, {7, 3}, {3, 5}}));
        assertEquals(17, solution.maximumWealth(new int[][]{{2, 8, 7}, {7, 1, 3}, {1, 9, 5}}));
    }
}

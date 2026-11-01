package com.jk.explore.problems.leetcode.p0282.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ExpressionAddOperatorsTest {

    private final ExpressionAddOperators solution = new ExpressionAddOperators();

    private List<String> sorted(List<String> l) {
        List<String> c = new ArrayList<>(l);
        Collections.sort(c);
        return c;
    }

    @Test
    void examples() {
        assertEquals(List.of("1*2*3", "1+2+3"), sorted(solution.addOperators("123", 6)));
        assertEquals(List.of("2*3+2", "2+3*2"), sorted(solution.addOperators("232", 8)));
        assertEquals(List.of("1*0+5", "10-5"), sorted(solution.addOperators("105", 5)));
        assertEquals(List.of("0*0", "0+0", "0-0"), sorted(solution.addOperators("00", 0)));
        assertEquals(List.of(), solution.addOperators("3456237490", 9191));
    }

    @Test
    void bigNumberWithoutOverflow() {
        assertEquals(List.of("2147483647"), solution.addOperators("2147483647", Integer.MAX_VALUE));
    }
}

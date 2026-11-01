package com.jk.explore.problems.leetcode.p0779.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KthSymbolInGrammarTest {

    private final KthSymbolInGrammar solution = new KthSymbolInGrammar();

    @ParameterizedTest
    @CsvSource({"1,1,0", "2,1,0", "2,2,1", "3,3,1", "3,4,0", "4,5,1", "30,434991989,0"})
    void symbol(int n, int k, int expected) {
        assertEquals(expected, solution.kthGrammar(n, k));
    }

    @Test
    void matchesBuiltRows() {
        StringBuilder row = new StringBuilder("0");
        for (int n = 1; n <= 10; n++) {
            for (int k = 1; k <= row.length(); k++) assertEquals(row.charAt(k - 1) - '0', solution.kthGrammar(n, k));
            StringBuilder next = new StringBuilder();
            for (char c : row.toString().toCharArray()) next.append(c == '0' ? "01" : "10");
            row = next;
        }
    }
}

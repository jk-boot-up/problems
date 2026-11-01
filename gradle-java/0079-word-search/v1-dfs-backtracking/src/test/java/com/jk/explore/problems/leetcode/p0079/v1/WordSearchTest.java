package com.jk.explore.problems.leetcode.p0079.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class WordSearchTest {

    private final WordSearch solution = new WordSearch();

    private static char[][] board() {
        return new char[][]{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}};
    }

    @ParameterizedTest
    @CsvSource({"ABCCED,true", "SEE,true", "ABCB,false", "ASADFBCCEESE,true"})
    void searches(String word, boolean expected) {
        assertEquals(expected, solution.exist(board(), word));
    }
}

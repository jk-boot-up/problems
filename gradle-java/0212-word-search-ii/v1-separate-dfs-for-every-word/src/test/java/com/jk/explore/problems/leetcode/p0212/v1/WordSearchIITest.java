package com.jk.explore.problems.leetcode.p0212.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class WordSearchIITest {

    private final WordSearchII solution = new WordSearchII();

    private static char[][] board(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void example() {
        List<String> found = solution.findWords(board("oaan", "etae", "ihkr", "iflv"), new String[]{"oath", "pea", "eat", "rain"});
        assertEquals(Set.of("oath", "eat"), new HashSet<>(found));
        assertEquals(2, found.size());
    }

    @Test
    void cellUsedOnce() {
        assertEquals(List.of(), solution.findWords(board("ab", "cd"), new String[]{"abcb"}));
    }

    @Test
    void duplicatesReportedOnce() {
        assertEquals(List.of("aa"), solution.findWords(board("aa"), new String[]{"aa"}));
    }
}

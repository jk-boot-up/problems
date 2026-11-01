package com.jk.explore.problems.leetcode.p0211.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class WordDictionaryTest {

    @Test
    void example() {
        WordDictionary d = new WordDictionary();
        d.addWord("bad");
        d.addWord("dad");
        d.addWord("mad");
        assertFalse(d.search("pad"));
        assertTrue(d.search("bad"));
        assertTrue(d.search(".ad"));
        assertTrue(d.search("b.."));
        assertFalse(d.search("b."));
        assertFalse(d.search("...."));
    }
}

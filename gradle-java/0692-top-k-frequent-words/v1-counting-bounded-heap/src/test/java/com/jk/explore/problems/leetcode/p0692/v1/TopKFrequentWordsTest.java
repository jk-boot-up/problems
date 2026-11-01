package com.jk.explore.problems.leetcode.p0692.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TopKFrequentWordsTest {

    private final TopKFrequentWords solution = new TopKFrequentWords();

    @Test
    void examples() {
        assertEquals(List.of("i", "love"), solution.topKFrequent(new String[]{"i", "love", "leetcode", "i", "love", "coding"}, 2));
        assertEquals(List.of("the", "is", "sunny", "day"),
                solution.topKFrequent(new String[]{"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"}, 4));
    }
}

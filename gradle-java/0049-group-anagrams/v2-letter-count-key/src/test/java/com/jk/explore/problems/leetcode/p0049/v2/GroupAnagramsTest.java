package com.jk.explore.problems.leetcode.p0049.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class GroupAnagramsTest {

    private final GroupAnagrams solution = new GroupAnagrams();

    private static Set<Set<String>> normalize(List<List<String>> groups) {
        Set<Set<String>> out = new HashSet<>();
        for (List<String> g : groups) out.add(new HashSet<>(g));
        return out;
    }

    @Test
    void example1() {
        assertEquals(Set.of(Set.of("bat"), Set.of("nat", "tan"), Set.of("ate", "eat", "tea")),
                normalize(solution.groupAnagrams(new String[]{"eat", "tea", "tan", "ate", "nat", "bat"})));
    }

    @Test
    void emptyString() {
        assertEquals(List.of(List.of("")), solution.groupAnagrams(new String[]{""}));
    }

    @Test
    void single() {
        assertEquals(List.of(List.of("a")), solution.groupAnagrams(new String[]{"a"}));
    }
}

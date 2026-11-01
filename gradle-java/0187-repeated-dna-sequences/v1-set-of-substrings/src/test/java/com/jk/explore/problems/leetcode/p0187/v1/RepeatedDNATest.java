package com.jk.explore.problems.leetcode.p0187.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RepeatedDNATest {

    private final RepeatedDNA solution = new RepeatedDNA();

    @Test
    void examples() {
        assertEquals(List.of("AAAAACCCCC", "CCCCCAAAAA"), solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"));
        assertEquals(List.of("AAAAAAAAAA"), solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"));
        assertEquals(List.of(), solution.findRepeatedDnaSequences("ACGT"));
        assertEquals(List.of(), solution.findRepeatedDnaSequences("ACGTACGTAC"));
    }
}

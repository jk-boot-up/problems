package com.jk.explore.problems.leetcode.p0763.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PartitionLabelsTest {

    private final PartitionLabels solution = new PartitionLabels();

    @Test
    void examples() {
        assertEquals(List.of(9, 7, 8), solution.partitionLabels("ababcbacadefegdehijhklij"));
        assertEquals(List.of(10), solution.partitionLabels("eccbbbbdec"));
        assertEquals(List.of(1, 1, 1), solution.partitionLabels("abc"));
    }
}

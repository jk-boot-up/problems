package com.jk.explore.problems.leetcode.p0093.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RestoreIPAddressesTest {

    private final RestoreIPAddresses solution = new RestoreIPAddresses();

    @Test
    void examples() {
        assertEquals(List.of("255.255.11.135", "255.255.111.35"), solution.restoreIpAddresses("25525511135"));
        assertEquals(List.of("0.0.0.0"), solution.restoreIpAddresses("0000"));
        assertEquals(List.of("1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"), solution.restoreIpAddresses("101023"));
    }
}

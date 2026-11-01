package com.jk.explore.problems.leetcode.p0071.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SimplifyPathTest {

    private final SimplifyPath solution = new SimplifyPath();

    @ParameterizedTest
    @CsvSource({"/home/,/home", "/home//foo/,/home/foo", "/home/user/Documents/../Pictures,/home/user/Pictures", "/../,/", "/.../a/../b/c/../d/./,/.../b/d", "/a/./b/../../c/,/c"})
    void simplifies(String path, String expected) {
        assertEquals(expected, solution.simplifyPath(path));
    }
}

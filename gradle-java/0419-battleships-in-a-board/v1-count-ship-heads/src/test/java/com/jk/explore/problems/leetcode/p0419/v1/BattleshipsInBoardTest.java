package com.jk.explore.problems.leetcode.p0419.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BattleshipsInBoardTest {

    private final BattleshipsInBoard solution = new BattleshipsInBoard();

    private char[][] board(String... rows) {
        char[][] b = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) b[i] = rows[i].toCharArray();
        return b;
    }

    @Test
    void examples() {
        assertEquals(2, solution.countBattleships(board("X..X", "...X", "...X")));
        assertEquals(0, solution.countBattleships(board(".")));
        assertEquals(3, solution.countBattleships(board("XX.X", "...X", "X...")));
    }
}

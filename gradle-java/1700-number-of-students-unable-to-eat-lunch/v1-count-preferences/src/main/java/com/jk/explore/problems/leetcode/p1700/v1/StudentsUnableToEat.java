package com.jk.explore.problems.leetcode.p1700.v1;

import java.util.*;

public class StudentsUnableToEat {

    public int countStudents(int[] students, int[] sandwiches) {
        int[] want = new int[2];
        for (int s : students) want[s]++;
        for (int i = 0; i < sandwiches.length; i++) {
            if (want[sandwiches[i]] == 0) return sandwiches.length - i;
            want[sandwiches[i]]--;
        }
        return 0;
    }
}

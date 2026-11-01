package com.jk.explore.problems.leetcode.p0220.v1;

import java.util.*;

public class ContainsDuplicateIII {

    public boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
        for (int i = 0; i < nums.length; i++)
            for (int j = i + 1; j < nums.length && j - i <= indexDiff; j++)
                if (Math.abs((long) nums[i] - nums[j]) <= valueDiff) return true;
        return false;
    }
}

package com.jk.explore.problems;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * <a href="https://leetcode.com/problems/two-sum/">Two Sum</a>
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 */
@NoArgsConstructor
public class TwoSum {

    public Results getIndicesResults(List<Integer> numbers, Integer pairSumTarget) {
        Map<Integer, Integer> numberIndexMap = new HashMap<>();
        for(int i=0; i < numbers.size(); i++) {
            Integer number = numbers.get(i);
            if(!numberIndexMap.containsKey(number)) {
                numberIndexMap.put(number, i);
            }
            Integer target = pairSumTarget - number;
            Integer targetIndex = numberIndexMap.get(target);
            if(targetIndex != null && targetIndex != i) {
                return Results.builder().firstIndex(i < targetIndex ? i : targetIndex).secondIndex(targetIndex > i ? targetIndex : i).build();
            }
        }
        return null;
    }

    @Getter
    @Builder
    public static class Results {
        private int firstIndex;
        private int secondIndex;
    }

}

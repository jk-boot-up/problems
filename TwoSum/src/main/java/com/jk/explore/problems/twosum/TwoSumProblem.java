package com.jk.explore.problems.twosum;

import java.util.HashMap;
import java.util.Map;

public class TwoSumProblem {

    public int[] findIndices(int [] numbers, int twoSum) {
        // Space - O(n)
        Map<Integer, Integer> numbersIndexMap = new HashMap<>();
        // Time - O(n)
        for(int index=0; index < numbers.length; index++) {
            int firstNumber = numbers[index];
            int firstNumberIndex = index;
            int secondNumber = twoSum - firstNumber;
            if(numbersIndexMap.containsKey(secondNumber)) {
                int secondNumberIndex = numbersIndexMap.get(secondNumber);
                return new int[] {firstNumberIndex, secondNumberIndex};
            } else {
                numbersIndexMap.put(firstNumber, firstNumberIndex);
            }
        }
        // not found
        return null;
    }
}

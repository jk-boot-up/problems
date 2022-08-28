package com.jk.explore.problems.samples.numeric.level.a;

import java.util.*;
import java.util.function.IntPredicate;
import java.util.stream.IntStream;

public class FindIndicesForSum {

    public int[] getIndicesWhoseElementsSumsToTargetWithBruteForce(int[] nums, int target) {
        if(nums == null || nums.length == 0) {
            return null;
        }

        for(int i=0; (i+1) < nums.length; i++) {
            for(int j=i+1; j < nums.length; j++) {
                if(nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }

    public int[] getIndicesWhoseElementsSumsToTargetWithMap(int[] nums, int target) {
        if(nums == null) {
            return null;
        }
        HashMap<Integer, Integer> inputMapWithIndex = new HashMap<>();
        IntStream.range(0, nums.length).forEach(index -> inputMapWithIndex.put(nums[index], index));

        OptionalInt firstIndex = IntStream.range(0, nums.length).filter(value -> {
            if (inputMapWithIndex.containsKey(target - nums[value])) {
                return true;
            }
            return false;}).findFirst();


        if (firstIndex.isPresent()) {
            return new int[] {firstIndex.getAsInt(), inputMapWithIndex.get(target-nums[firstIndex.getAsInt()]).intValue()};
        }
        return null;
    }


    public int[] getIndicesForSum(List<Integer> numbers, Integer sum) {
        final Map<Integer, Integer> numberIndexMap = new HashMap<>();
        numbers.stream().forEach(i-> {
            int number1 = i;
            int number2 = sum - i;
            numberIndexMap.containsKey(number2) ;

        });

        return null;

    }


}

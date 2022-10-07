package com.jk.explore.problems.p1;

import lombok.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

/**
 * <p>
 * <br>
 <a href="https://leetcode.com/problems/3sum/">3sum</a>
 Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 Notice that the solution set must not contain duplicate triplets.
 </p>
 */
public class ThreeSum {

    public Set<Triplet> findTripletIndices(int[] numbers) {

        return null;
    }

    @Getter
    @ToString
    static class Triplet {
        private List<IndexedNumber> triplet = new ArrayList<>(3);

        public Triplet(IndexedNumber one, IndexedNumber two, IndexedNumber three) {
            triplet.add(one);
            triplet.add(two);
            triplet.add(three);
        }
    }

    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @EqualsAndHashCode
    static class IndexedNumber {
        int number;
        int index;

        @Override
        public String toString() {
            return "(" + number + ":" + index+ ")";
        }

    }
}

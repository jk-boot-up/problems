# 1700. Number of Students Unable to Eat Lunch

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Queue &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)

## Problem

Students in a queue each prefer circular (`0`) or square (`1`) sandwiches; sandwiches are in a stack (`sandwiches[0]` on top). The front
student takes the top sandwich if they like it, otherwise goes to the back of the queue. This stops when nobody in the queue wants the top
sandwich. Return how many students cannot eat.

**Example**
```
students = [1,1,0,0],     sandwiches = [0,1,0,1]     → 0
students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1] → 3
```

**Constraints**
* `1 <= n <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-count-preferences](v1-count-preferences/README.md) | Count preferences | `O(n)` | `O(1)` | [▶ animation](v1-count-preferences/animation/index.html) |

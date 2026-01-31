# UAS-Task-Round-2
this is my assignment for the round 2 of UAS(unmaned aerial systems)
This repository contains my solution approach for the Round 2 Software Task of
Unmanned Aerial Systems (UAS)
## Problem Statement
The task involves processing UAV images to:
- Segment land and water regions
- Detect casualties and rescue camps
- Assign casualties to rescue camps based on priority, distance, and capacity
- Compute rescue efficiency metrics

## Tools Used
- Python 3
- OpenCV
- NumPy

## Approach
1. Segment land and water using color-based thresholding.
2. Detect rescue camps and casualties using contour analysis.
3. Assign priority scores based on age group and medical condition.
4. Allocate casualties to rescue camps using a distance-aware  algorithm.


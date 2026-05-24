class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # Sorting is essential to ensure overlapping intervals are adjacent
        intervals.sort(key=lambda x: x[0])
        ans = []
        # Initialize with the first interval
        current_interval = intervals[0]
        ans.append(current_interval)
        
        for next_interval in intervals[1:]:
            # If the current interval's end is >= the next interval's start, they overlap
            if current_interval[1] >= next_interval[0]:
                # Merge by updating the end time to the maximum of both
                current_interval[1] = max(current_interval[1], next_interval[1])
            else:
                # No overlap, move to the next interval
                current_interval = next_interval
                ans.append(current_interval)
        return ans
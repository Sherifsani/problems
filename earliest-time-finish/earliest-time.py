class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        #1. determine the land ride that finishes earliest 
        min_land_finish = float('inf')
        for start, duration in zip(landStartTime, landDuration):
            min_land_finish = min(min_land_finish, start + duration)

        #2. check what water ride would end earliest after the min land finishes
        seq_1 = float('inf')
        for start, duration in zip(waterStartTime, waterDuration):
            total_time = max(min_land_finish, waterStartTime) + duration
            seq_1 = min(seq_1, total_time)

        #3. now repeat the steps but water first -> land second
        min_water_finish = float('inf')
        for start, duration in zip(waterStartTime, waterDuration):
            min_water_finish = min(min_water_finish, start + duration)

        #4. check the second sequence
        seq_2 = float('inf')
        for start, duration in zip(landStartTime, landDuration):
            total_time = max(min_water_finish, landStartTime) + duration
            seq_2 = min(total_time, seq_2)

        return min(seq_2, seq_1)

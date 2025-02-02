class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        sorted_list = sorted(intervals, key=lambda x: x[0])
        result = []

        check = sorted_list[0]

        for i in range(1, len(sorted_list)):

            if check[1] >= sorted_list[i][0]:
                check[1] = max(check[1], sorted_list[i][1])
            else:
                result.append(check)
                check = sorted_list[i]

        result.append(check)

        print(result)
        return result

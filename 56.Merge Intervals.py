class Solution(object):
    def merge(self, intervals):  # 跳过定义interval，直接使用list；
        if len(intervals) == 0:
            return []
        intervals.sort()
        s = [intervals.pop(0)]
        for i in range(len(intervals)):
            if intervals[i][0] > s[-1][1]:
                s.append(intervals[i])
            else:
                if intervals[i][1] <= s[-1][1]:
                    continue
                else:
                    s[-1] = [s[-1][0], intervals[i][1]]
        return s


class Interval(object):  # Definition for an interval.
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge1(self, intervals):
        if len(intervals) == 0:
            return []
        # intervals.sort(key = lambda x:start)  #应当掌握sort()所有用法:list.sort()对原列表进行操作，list=sorted(list)保留原list生成新list
        intervals.sort(key=lambda oj: oj.start)
        s = [intervals.pop(0)]
        for i in range(len(intervals)):
            if intervals[i].start > s[-1].end:
                s.append(intervals[i])
            else:
                if intervals[i].end <= s[-1].end:
                    continue
                else:
                    #s[-1] = [s[-1].start, intervals[i].end]
                    s[-1] = Interval(s[-1].start, intervals[i].end)
        return s


# intervals==[obj1,obj2,obj3,obj4],obj1=Interval(start,end)
obj1 = Interval(2, 4)
obj2 = Interval(1, 3)
obj3 = Interval(3, 7)
obj4 = Interval(8, 9)
intervals = [obj1, obj2, obj3, obj4]
a = Solution()
print(a.merge1(intervals))

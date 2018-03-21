import re


class Solution(object):
    def calculate(self, s):
        if type(s) == str:
            s1 = re.split(r'[\+\-\*\/\s+]+', s)
            j = 1
            for i in s:
                if i == '+' or i == '-' or i == '*' or i == '/':
                    s1.insert(j, i)
                    j = j + 2
            s = s1
        if len(s) == 1:
            return int(s[0])
        if '*' not in s and '/' not in s:
            if s[1] == '+':
                m = int(s[0]) + int(s[2])
            elif s[1] == '-':
                m = int(s[0]) - int(s[2])
            s.pop(0)
            s.pop(0)
            s.pop(0)
            s.insert(0, str(m))
            return self.calculate(s)
        for i in range(len(s) - 1):
            if s[i] == '*':
                m = int(s[i - 1]) * int(s[i + 1])
                s.pop(i - 1)
                s.pop(i - 1)
                s.pop(i - 1)
                s.insert(i - 1, str(m))
                break
            elif s[i] == '/':
                m = int(s[i - 1]) // int(s[i + 1])
                s.pop(i - 1)
                s.pop(i - 1)
                s.pop(i - 1)
                s.insert(i - 1, str(m))
                break
        return self.calculate(s)

    def calculate1(self, s):
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = s[i]
                num = 0
        return sum(stack)


a = Solution()
print(a.calculate('123 +  2- 4* 54/   9'))
print(a.calculate1("123 +  2- 4* 54/   9"))

class Solution(object):
    def exist(self, board, word):  # backtracking 回溯思想
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    # 采用两个函数 exist与 dfs是因为思路是分两个步骤1：找到第一个符合的位置，接下来分析该位置的上下左右的值是否符合。
    # check whether can find word, start at (i,j) position

    def dfs(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) or self.dfs(
            board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        # 4个or表达式是回溯的精髓
        board[i][j] = tmp
        return res


a = Solution()
print(a.exist([['a', 'b', 'c'], ['d', 'e', 'f'],
               ['g', 'h', 'i']], ['a', 'b', 'c', 'f']))

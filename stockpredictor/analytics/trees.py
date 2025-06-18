class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def range_max(self, l, r):
        # Find max in range [l, r)
        l += self.n
        r += self.n
        result = float('-inf')
        while l < r:
            if l % 2:
                result = max(result, self.tree[l])
                l += 1
            if r % 2:
                r -= 1
                result = max(result, self.tree[r])
            l //= 2
            r //= 2
        return result

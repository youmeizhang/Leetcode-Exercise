class SnapshotArray:

    def __init__(self, length: int):
        self.l = [0] * length
        self.dic = {}
        self.idx = 0
        self.length = length
        self.temp_dic = {}
        

    def set(self, index: int, val: int) -> None:
        self.l[index] = val
        self.temp_dic[index] = val

    def snap(self) -> int:
        self.dic[self.idx] = self.temp_dic.copy()
        self.idx += 1
        return self.idx - 1

    def get(self, index: int, snap_id: int) -> int:
        temp_dic = self.dic[snap_id]
        if index in temp_dic:
            return temp_dic[index]
        else:
            return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

#对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2+=sorted(set(arr1)-set(arr2))#将多余先按升序排到arr2后
        arr1.sort(key=arr2.index)#arr2元素对应的下标顺序进行排序
        return arr1

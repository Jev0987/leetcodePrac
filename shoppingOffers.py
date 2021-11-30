from functools import lru_cache
from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        #商品数量n
        n = len(price)

        # 过滤不需要计算的大礼包，只保留需要计算的大礼包
        filter_special = []
        for sp in special:
            #有效大礼包（里头有商品）  and   大礼包有优惠，原价购买相同数量商品时，大礼包价格低于原价购买
            #python 数组中的-1表示最后一个数值
            if sum(sp[i] for i in range(n)) > 0 and sum(sp[i] * price[i] for i in range(n)) > sp[-1]:
                filter_special.append(sp)

        # 记忆化搜索计算满足购物清单所需花费的最低价格
        @lru_cache(None)
        def dfs(cur_needs):
            # 不购买任何大礼包，原价购买购物清单中的所有物品
            min_price = sum(need * price[i] for i, need in enumerate(cur_needs))
            #查看大礼包内容
            for cur_special in filter_special:
                #记录大礼包价格
                special_price = cur_special[-1]
                nxt_needs = []
                #查看对应礼包数量和当前所需商品数量
                for i in range(n):
                    if cur_special[i] > cur_needs[i]:  # 不能购买超出购物清单指定数量的物品
                        break
                    #当前所需商品数-礼包内对应商品数
                    nxt_needs.append(cur_needs[i] - cur_special[i])

                if len(nxt_needs) == n:  # 大礼包可以购买
                    min_price = min(min_price, dfs(tuple(nxt_needs)) + special_price)
            return min_price

        return dfs(tuple(needs))







price = [2,5]
special = [[3,0,5], [1,2,10]]
needs = [3,2]
s = Solution()
print(s.shoppingOffers(price, special, needs))

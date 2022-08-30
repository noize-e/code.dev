"""
You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

>>> change(coins=[1,2,5], amount=11)
3

>>> change(coins=[1,2,5], amount=20)
4

>>> change(coins=[2], amount=3)
-1

>>> change(coins=[1], amount=0)
0

>>> change(coins=[1], amount=1)
1

>>> change(coins=[1], amount=2)
2
"""

def calculate_remain(max_coin:int, amount:int) -> int:
	fewest_coins = amount//max_coin #= 2
	remaining = amount - (fewest_coins * max_coin) #= 1
	return (fewest_coins, remaining)


def change(coins:list, amount:int):
	# amount: 11
	fewest_coins, remaining = calculate_remain(max(coins), amount)

	if fewest_coins != 0:
		next_coin_index = coins.index(max_coint) - 1 # index=1

		for x in range(0, next_coin_index, -1):
			if coins[x] =< remaining: # 1
				results = calculate_remain(coins[x], amount)
				fewest_coins += results[0]
				remaining = results[1]

	return fewest_coins




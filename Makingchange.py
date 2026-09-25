n = int(input("Enter number of coins: "))
coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))
dp = [float('inf')] * (amount + 1)
dp[0] = 0
for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], 1 + dp[i - coin])
if dp[amount] == float('inf'):
    print("Change not possible")
else:
    print("Minimum coins:", dp[amount])

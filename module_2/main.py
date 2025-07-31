from crypto_utilis  import wallet
my_wallet = wallet('dan')
my_wallet.deposit('ETH' , 0.7)
print(my_wallet.view_balance())
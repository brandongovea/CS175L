#CS175L
#Brandon Govea
#stocks

commission_rate_p = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
commission_rate_s = float(input("Enter commission rate percentage (ex 0.03 on stock sale: "))
num_shares_p = int(input("Enter number of shares purchased: "))
num_shares_s = int(input("Enter number of shares shold: "))
purchase_pps = int(input("Enter purchase price per share: "))
sell_pps = float(input("Enter sell price per share: "))

amountPaidForStock = num_shares_p * purchase_pps
purchaseCommission = commission_rate_p * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = num_shares_s * sell_pps
sellingCommission = commission_rate_s * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid

print(f"Amount paid for stock: ${amountPaidForStock:,.2f}")
print(f"Commission paid on the purchase: ${purchaseCommission:,.2f}")
print(f"Amount the stock sold for: ${stockSoldFor:,.2f}")
print(f"Commission paid on the sale: ${sellingCommission:,.2f}")
print(f"Profit (or loss if negative): ${profitOrLoss:,.2f}")

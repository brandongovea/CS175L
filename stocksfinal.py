Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:38) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

=============== RESTART: /Users/brandongovea/Downloads/stocks.py ===============
Enter commission rate percentage (ex 0.03) on stock purchase: .03
Enter commission rate percentage (ex 0.03 on stock sale: .03
Enter number of shares purchased: 2000
Enter number of shares shold: 2000
Enter purchase price per share: 40
Enter sell price per share: 42.75
Amount paid for stock: $ 80000
Commission paid on the purchase: $ 2400.0
Amount the stock sold for: $ 85500.0
Commission paid on the sale: $ 2565.0
Profit (or loss if negative): $ 535.0
>>> 
=========== RESTART: /Users/brandongovea/Downloads/fStringExample.py ===========

=============== RESTART: /Users/brandongovea/Downloads/stocks.py ===============
Enter commission rate percentage (ex 0.03) on stock purchase: ,03
Traceback (most recent call last):
  File "/Users/brandongovea/Downloads/stocks.py", line 5, in <module>
    commission_rate_p = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
ValueError: could not convert string to float: ',03'
>>> 
=============== RESTART: /Users/brandongovea/Downloads/stocks.py ===============
Enter commission rate percentage (ex 0.03) on stock purchase: .03
Enter commission rate percentage (ex 0.03 on stock sale: .03
Enter number of shares purchased: 2000
Enter number of shares shold: 2000
Enter purchase price per share: 40
Enter sell price per share: 42.75
Amount paid for stock: $80,000.00
Commission paid on the purchase: ${purchaseCommission:,.2f}
Amount the stock sold for: ${stockSoldFor:,.2f}
Commission paid on the sale: ${sellingCommission:,.2f}
Profit (or loss if negative): ${profitOrLoss:,.2f
>>> 
=============== RESTART: /Users/brandongovea/Downloads/stocks.py ===============
Enter commission rate percentage (ex 0.03) on stock purchase: .03
Enter commission rate percentage (ex 0.03 on stock sale: .03
Enter number of shares purchased: 2000
Enter number of shares shold: 2000
Enter purchase price per share: 40
Enter sell price per share: 42.75
Amount paid for stock: $80,000.00
Commission paid on the purchase: $2,400.00
Amount the stock sold for: $85,500.00
Commission paid on the sale: $2,565.00
Profit (or loss if negative): $535.00

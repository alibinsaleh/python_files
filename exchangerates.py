#!/usr/bin/env python
from blockchain import exchangerates

ticker = exchangerates.get_ticker()

print("Bitcoin Prices in various currencies:")
for k in ticker:
    print(k, ticker[k].p15min)


btc = exchangerates.to_btc('USD', 63000)
print("\n63000 dollars in Bitcoin: %s " % btc)


import ccxtpro
import asyncio
import time

exchange = ccxtpro.poloniex({'enableRateLimit': True})
exchange_2 = ccxtpro.binance({'enableRateLimit': True})
exchange_3 = ccxtpro.ftx({'enableRateLimit': True})
    
async def main():

	a = []
	b = []
	c = []
	while True:
		start_time = time.time()
		orderbook = await exchange.watch_order_book('ETH/BTC')
		print(f"Parse time EXCHANGE_1 {time.time() - start_time} sec")
		a.append(time.time() - start_time)
		print(f"Average parse time {sum(a) / len(a)} sec")
		start_time = time.time()
		orderbook = await exchange_2.watch_order_book('ETH/BTC')
		print(f"Parse time EXCHANGE_2 {time.time() - start_time} sec")
		b.append(time.time() - start_time)
		print(f"Average parse time {sum(b) / len(b)} sec")
		start_time = time.time()
		orderbook = await exchange_3.watch_order_book('ETH/BTC')
		print(f"Parse time EXCHANGE_3 {time.time() - start_time} sec")
		c.append(time.time() - start_time)
		print(f"Average parse time {sum(c) / len(c)} sec")


asyncio.get_event_loop().run_until_complete(main())
from HttpMD5Util import httpGet
import os
import datetime


class OneFox:
    def __init__(self, api_token):
        self.api_token = api_token
        self.url_base = "https://1fox.com"
        self.resource_header = "/api/v1/"

    def error_check(self, result):
        if result['warning']:
            string = source + " warning: " + str(result['warning_message'])
            print(string)
        if result['error']:
            string = source + " error[" + str(result['error_code']) + "]: " + str(result['error_message'])
            print(string)

    def user_get(self, currency='BTC'):
        resource = self.resource_header + "user/get.php"
        params = {
            "token": self.api_token,
            "currency": currency
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def user_overview(self, currency='BTC'):
        resource = self.resource_header + "user/overview.php"
        params = {
            "token": self.api_token,
            "currency": currency
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def user_dead_man_switch(self, symbols, stop=False):
        resource = self.resource_header + "user/dead_man_switch.php"
        params = {
            "token": self.api_token,
            "symbols": ','.join([symbols]),
            "stop": stop
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def user_deposit(self, currency='BTC'):
        resource = self.resource_header + "user/deposit.php"
        params = {
            "token": self.api_token,
            "currency": currency
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def user_transactions(self, currency='BTC', limit=None, offset=None, type=None, date_start=None, date_end=None):
        resource = self.resource_header + "user/transactions.php"
        params = {
            "token": self.api_token,
            "currency": currency,
            "limit": limit,
            "offset": offset,
            "type": type,
            "date_start": date_start,
            "date_end": date_end
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def market_list(self):
        resource = self.resource_header + "market/list"
        result = httpGet(self.url_base, resource, params=None)
        self.error_check(result)
        return result['response']

    def market_get(self, symbol):
        resource = self.resource_header + "market/get.php"
        params = {
            "symbol": symbol
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def market_bars(self, symbol, resolution, limit=None, date_start=None, date_end=None):
        resource = self.resource_header + "market/bars.php"
        params = {
            "symbol": symbol,
            "resolution": resolution,
            "limit": limit,
            "date_start": date_start,
            "date_end": date_end
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def market_orderbook(self, symbol, depth=None):
        resource = self.resource_header + "market/orderbook.php"
        params = {
            "symbol": symbol,
            "depth": depth
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def market_ticker(self, symbols):
        resource = self.resource_header + "market/ticker.php"
        params = {
            "symbols": ','.join([symbols])
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def market_funding_history(self, symbol, limit=None, offset=None):
        resource = self.resource_header + "market/funding_history.php"
        params = {
            "symbol": symbol,
            "limit": limit,
            "offset": offset
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def market_index_history(self, symbol, limit=None, offset=None):
        resource = self.resource_header + "market/index_history.php"
        params = {
            "symbol": symbol,
            "limit": limit,
            "offset": offset
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def market_trades(self, symbol, limit=None):
        resource = self.resource_header + "market/trades.php"
        params = {
            "symbol": symbol,
            "limit": limit
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def market_slippage(self, symbol, type, volume=None, contracts=None):
        resource = self.resource_header + "market/trades.php"
        params = {
            "symbol": symbol,
            "type": type,
            "volume": volume,
            "contracts": contracts
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def order_create(self, symbol, margin, direction, leverage, order_type, limit_price, stop_entry_price, stop_loss=None, take_profit=None, post_only=None):
        resource = self.resource_header + "order/create.php"
        params = {
            "token": api_token,
            "symbol": symbol,
            "margin": margin,
            "direction": direction,
            "leverage": leverage,
            "order_type": order_type,
            "limit_price": limit_price,
            "stop_entry_price": stop_entry_price,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "post_only": post_only,
            "referral_id": "1cv"
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def order_close(self, order_id):
        resource = self.resource_header + "order/close.php"
        params = {
            "token": self.api_token,
            "order_id": order_id
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def position_edit(self, position_id, stop_loss=None, take_profit=None):
        resource = self.resource_header + "position/edit.php"
        params = {
            "token": self.api_token,
            "position_id": position_id,
            "stop_loss": stop_loss,
            "take_profit": take_profit
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def position_history(self, currency, limit=None, offset=None, hide_zero_profits=None):
        resource = self.resource_header + "position/history.php"
        params = {
            "token": self.api_token,
            "currency": currency,
            "limit": limit,
            "offset": offset,
            "hide_zero_profits": hide_zero_profits
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def position_close(self, position_id):
        resource = self.resource_header + "position/close.php"
        params = {
            "token": self.api_token,
            "position_id": position_id
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def position_trades(self, position_id, limit=None, offset=None):
        resource = self.resource_header + "position/trades.php"
        params = {
            "token": self.api_token,
            "position_id": position_id,
            "limit": limit,
            "offset": offset
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def position_fees(self, position_id, limit=None, offset=None):
        resource = self.resource_header + "position/fees.php"
        params = {
            "token": self.api_token,
            "position_id": position_id,
            "limit": limit,
            "offset": offset
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

    def position_merge(self, position_ids):
        resource = self.resource_header + "position/merge.php"
        params = {
            "token": self.api_token,
            "position_ids": ','.join(position_ids)
        }
        result = httpGet(self.url_base, resource, params)
        self.error_check(result)
        return result['response']

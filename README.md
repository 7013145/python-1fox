# python-1fox
A python implementation of the [1Fox](https://1fox.com/?t=1cv) API.

## usage

```
onefox_client = OneFox('APIKEY')

user_btc = onefox_client.user_get() # BTC by default
user_bch = onefox_client.user_get('BCH') # explicitly BCH 

user_overview_btc = onefox_client.user_overview(currency='BTC')
user_overview_bch = onefox_client.user_overview(currency='BCH')

user_dead_man_switch = onefox_client.user_dead_man_switch(['BTCUSD', 'ETHUSD'], stop=False)
```

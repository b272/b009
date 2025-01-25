import time
import hashlib
import hmac
import requests
import json
import logging
from utils.config import Config

logger = logging.getLogger(__name__)

class BybitBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = "https://api-demo.bybit.com" if testnet else "https://api.bybit.com"
        logger.info(f"Initialized BybitBot with {'testnet' if testnet else 'mainnet'} mode")

    def get_available_pairs(self):
        """Get list of available trading pairs"""
        endpoint = "/v5/market/instruments-info"
        params = "category=linear"
        return self._make_request('GET', endpoint, params)

    def check_api_access(self):
        """Verify API access and permissions"""
        logger.info("\n=== CHECKING API ACCESS ===")
        
        try:
            # Check balance first
            balance = self.get_balance()
            logger.info(f"Balance check response code: {balance.get('retCode')}")
            
            if balance.get('retCode') == 0:
                logger.info("[+] Balance API access: OK")
                logger.info("\nCurrent Balance:")
                for coin in balance['result']['list'][0]['coin']:
                    logger.info(f"{coin['coin']}: {coin['walletBalance']}")
                    
                # Test market data access
                klines = self.get_available_pairs()
                if klines.get('retCode') == 0:
                    logger.info("[+] Market data access: OK")
                    
                # Test order permissions with minimal values    
                test_order = self.place_order(
                    symbol="BTCUSDT",
                    side="Buy",
                    order_type="Limit",
                    qty=0.001,
                    price=1
                )
                logger.info(f"Test order response code: {test_order.get('retCode')}")
                
                # Consider both successful order and "insufficient balance" as valid responses
                valid_codes = [0, 110003]
                if test_order.get('retCode') in valid_codes:
                    logger.info("[+] Order placement permissions: OK")
                    return True
                    
            logger.info("\n=== API CHECK COMPLETE ===")
            return False
            
        except Exception as e:
            logger.error(f"API check error: {str(e)}")
            return False


    def generate_signature(self, params, timestamp):
        """Generate signature for API authentication"""
        param_str = str(timestamp) + self.api_key + "5000" + params
        return hmac.new(
            self.api_secret.encode('utf-8'),
            param_str.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def get_balance(self):
        """Get account balance"""
        endpoint = "/v5/account/wallet-balance"
        params = "accountType=UNIFIED"
        return self._make_request('GET', endpoint, params)

    def place_order(self, symbol, side, order_type, qty, price=None):
        """Place trading order"""
        endpoint = "/v5/order/create"
        
        params = {
            "category": "linear",
            "symbol": symbol,
            "side": side,
            "orderType": order_type,
            "qty": str(qty),
            "timeInForce": "GTC"
        }
        
        if price:
            params["price"] = str(price)
            
        # Convert params to JSON string
        params_json = json.dumps(params)
        
        return self._make_request('POST', endpoint, params_json)


    def get_position(self, symbol):
        """Get current position for symbol"""
        endpoint = "/v5/position/list"
        params = f"category=linear&symbol={symbol}"
        return self._make_request('GET', endpoint, params)

    def close_position(self, symbol, side, qty):
        """Close existing position"""
        return self.place_order(
            symbol=symbol,
            side="Sell" if side == "Buy" else "Buy",
            order_type="Market",
            qty=qty
        )

    def get_order_history(self, symbol):
        """Get order history"""
        endpoint = "/v5/order/history"
        params = f"category=linear&symbol={symbol}"
        return self._make_request('GET', endpoint, params)

    def _make_request(self, method, endpoint, params):
        """Make API request with authentication"""
        timestamp = str(int(time.time() * 1000))
        signature = self.generate_signature(params, timestamp)
        
        headers = {
            "X-BAPI-API-KEY": self.api_key,
            "X-BAPI-SIGN": signature,
            "X-BAPI-TIMESTAMP": timestamp,
            "X-BAPI-RECV-WINDOW": "5000",
            "Content-Type": "application/json"
        }
        
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(f"{url}?{params}", headers=headers)
            else:
                response = requests.post(url, headers=headers, data=params)
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            return {"retCode": -1, "error": str(e)}

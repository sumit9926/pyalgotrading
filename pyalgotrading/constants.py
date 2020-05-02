from enum import Enum


# TODO: 1. Sort this file
# TODO: 2. Use only Enums
# TODO: 3. See how values of constants can be maintained across this project and other projects

class BrokerOrderTypeConstants(Enum):
    BROKER_ORDER_TYPE_REGULAR = 'ORDER_TYPE_REGULAR'
    BROKER_ORDER_TYPE_BRACKET = 'ORDER_TYPE_BRACKET'
    BROKER_ORDER_TYPE_COVER = 'ORDER_TYPE_COVER'


class BrokerOrderCodeConstants(Enum):
    BROKER_ORDER_CODE_INTRADAY = 'ORDER_CODE_INTRADAY'
    BROKER_ORDER_CODE_DELIVERY = 'ORDER_CODE_DELIVERY_T0'
    BROKER_ORDER_CODE_DELIVERY_T1 = 'ORDER_CODE_DELIVERY_T1'
    BROKER_ORDER_CODE_DELIVERY_T2 = 'ORDER_CODE_DELIVERY_T2'


class BrokerOrderVarietyConstants(Enum):
    BROKER_ORDER_VARIETY_MARKET = 'ORDER_VARIETY_MARKET'
    BROKER_ORDER_VARIETY_LIMIT = 'ORDER_VARIETY_LIMIT'
    BROKER_ORDER_VARIETY_STOPLOSS_MARKET = 'ORDER_VARIETY_STOPLOSS_MARKET'
    BROKER_ORDER_VARIETY_STOPLOSS_LIMIT = 'ORDER_VARIETY_STOPLOSS_LIMIT'


class BrokerOrderTransactionTypeConstants(Enum):
    BROKER_ORDER_TRANSACTION_TYPE_BUY = 'BUY'
    BROKER_ORDER_TRANSACTION_TYPE_SELL = 'SELL'


class TradingType(Enum):
    TRADING_TYPE_BACKTESTING = 0
    TRADING_TYPE_PAPERTESTING = 1
    TRADING_TYPE_REALTRADING = 2


class StrategyMode(Enum):
    INTRADAY = 0
    DELIVERY = 1


VERSION_3_1_0 = '3.1.0'


class StrategyType(Enum):
    STRATEGY_TYPE_CUSTOMER_PYTHON = 1


# TODO: This enum is taken from algobulls_backend_web.constants file. Find a way to keep the definitions common & sourced from the same constants file
class TradingReportType(Enum):
    TRADING_REPORT_TYPE_PNL_TABLE = 0
    TRADING_REPORT_TYPE_STATS_TABLE = 1
    TRADING_REPORT_TYPE_ORDER_HISTORY = 2
    TRADING_REPORT_TYPE_LOGS = 3


class JobStatusEnum(Enum):
    JOB_RUNNING = 'RUNNING'
    JOB_STOPPED = 'STOPPED'


class ResponseEnum(Enum):
    RESPONSE_SUCCESS = 'Success'
    RESPONSE_ERROR = 'Error'
    RESPONSE_JOB_NOT_RUNNING = 'Job not running'


class CandleIntervalEnum(Enum):
    CANDLE_INTERVAL_MINUTE = 'minute'
    CANDLE_INTERVAL_3MINUTES = '3minutes'
    CANDLE_INTERVAL_5MINUTES = '5minutes'
    CANDLE_INTERVAL_10MINUTES = '10minutes'
    CANDLE_INTERVAL_15MINUTES = '15minutes'
    CANDLE_INTERVAL_30MINUTES = '30minutes'
    CANDLE_INTERVAL_60MINUTES = '60minutes'
    CANDLE_INTERVAL_DAY = 'day'

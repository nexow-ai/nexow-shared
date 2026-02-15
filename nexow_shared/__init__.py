"""Nexow Shared - Common code for Nexow microservices."""

__version__ = "0.1.0"

from nexow_shared.broker.models import Candle
from nexow_shared.db import get_supabase_client, SupabaseClient
from nexow_shared.rules.schema import Condition, RuleGroup, TradingRules, CONDITION_CATALOG
from nexow_shared.rules.interpreter import MarketSnapshot, MultiSnapshot, evaluate_rules

__all__ = [
    "Candle",
    "get_supabase_client",
    "SupabaseClient",
    "Condition",
    "RuleGroup",
    "TradingRules",
    "CONDITION_CATALOG",
    "MarketSnapshot",
    "MultiSnapshot",
    "evaluate_rules",
]

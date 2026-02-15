"""Database layer — Supabase client."""

from nexow_shared.db.client import SupabaseClient, db


def get_supabase_client() -> SupabaseClient:
    """Get the shared Supabase client instance."""
    return db


__all__ = ["SupabaseClient", "db", "get_supabase_client"]

# nexow-shared

Shared Python package for Nexow microservices.

## Installation

With uv (recommended):
```bash
uv pip install git+ssh://git@github.com/nexow-ai/nexow-shared.git@main
```

Or add to `pyproject.toml`:
```toml
dependencies = [
    "nexow-shared @ git+ssh://git@github.com/nexow-ai/nexow-shared.git@main"
]
```

## Contents

- **db/** - Supabase database client and utilities
- **broker/** - Broker data models and interfaces
- **risk/** - Risk management and guardrails
- **rules/** - Trading rules and validators
- **config/** - Configuration management
- **utils/** - Common utilities (logging, time, etc.)

## Usage

```python
from nexow_shared import get_supabase_client
from nexow_shared.broker.models import Instrument, Trade
from nexow_shared.risk import validate_position_size

# Get Supabase client
db = get_supabase_client()

# Use shared models
trade = Trade(symbol="EUR_USD", quantity=1000, price=1.0850)
```

## Development

```bash
# Install with uv (10-100x faster!)
uv sync

# Run tests
uv run pytest

# Lint
uv run ruff check .
```

## Version

0.1.0

## Benefits of uv

- ⚡ 10-100x faster than pip
- 🔒 Lock files for reproducible builds
- 🎯 Better dependency resolution
- 🚀 Works great with Railway deployment

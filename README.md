# nexow-shared

Shared Python package for Nexow microservices.

## Installation

```bash
pip install git+ssh://git@github.com/nexow-ai/nexow-shared.git@main
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
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Lint
ruff check .
```

## Version

0.1.0

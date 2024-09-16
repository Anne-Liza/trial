# migrations/env.py

from __future__ import annotations
import sys
from pathlib import Path
from alembic import context
from sqlalchemy import engine_from_config, pool
from database import Base, engine

# Set up Alembic configuration
config = context.config

# Set up target metadata
target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    # Run migrations in offline mode
    context.configure(url=config.get_main_option("sqlalchemy.url"))
    with context.begin_transaction():
        context.run_migrations()
else:
    # Run migrations in online mode
    run_migrations_online()

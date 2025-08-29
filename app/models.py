from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class CounterSession(SQLModel, table=True):
    """Persistent model to track counter sessions for testing purposes."""

    __tablename__ = "counter_sessions"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    final_value: int = Field(default=0, description="Final counter value when session ended")


class Counter(SQLModel, table=False):
    """Non-persistent counter model for in-memory state management."""

    value: int = Field(default=0, description="Current counter value")

    def increment(self) -> "Counter":
        """Increment counter by 1 and return new counter instance."""
        return Counter(value=self.value + 1)

    def decrement(self) -> "Counter":
        """Decrement counter by 1 and return new counter instance."""
        return Counter(value=self.value - 1)

    def reset(self) -> "Counter":
        """Reset counter to 0 and return new counter instance."""
        return Counter(value=0)


class CounterUpdate(SQLModel, table=False):
    """Schema for counter update operations."""

    operation: str = Field(description="Operation to perform: 'increment', 'decrement', or 'reset'")
    value: Optional[int] = Field(default=None, description="Optional value for direct counter setting")

from contextlib import asynccontextmanager
import asyncio

@asynccontextmanager
async def database_connection():
    """
    Async context manager that simulates database connection handling.
    Ensures proper connection setup and cleanup.
    """
    print("Connecting to database...")
    await asyncio.sleep(1)  # Simulate connection
    try:
        yield "Connection"
    finally:
        print("Closing database connection...")
        await asyncio.sleep(0.5)

async def main():
    """Demonstrates usage of async context manager."""
    async with database_connection() as conn:
        print(f"Using {conn}")
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
"""
Minimal MCP stdio server for demo.

Exposes two tools:
- add(a, b) -> a+b
- mul(a, b) -> a*b
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP


app = FastMCP(name="math-demo")


@app.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""

    return a + b


@app.tool()
def mul(a: int, b: int) -> int:
    """Multiply two integers."""

    return a * b


if __name__ == "__main__":
    app.run(transport="stdio")


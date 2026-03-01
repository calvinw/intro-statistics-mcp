"""
Intro Statistics MCP Server

Serves chapters of the Intro Statistics book as markdown with embedded images.
"""

import os
import glob
from fastmcp import FastMCP

BASE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(BASE, 'docs')

mcp = FastMCP("Intro Statistics")


@mcp.tool
def list_chapters() -> str:
    """List all available chapters of the Intro Statistics book."""
    md_files = sorted(glob.glob(os.path.join(DOCS, '*.md')))
    chapters = [os.path.splitext(os.path.basename(f))[0] for f in md_files]
    return "\n".join(chapters)


@mcp.tool
def get_chapter(chapter: str) -> str:
    """Get a chapter of the Intro Statistics book as markdown with embedded images.

    Args:
        chapter: The chapter name (e.g. 'barplots'). Use list_chapters() to see available chapters.
    """
    md_path = os.path.join(DOCS, f'{chapter}.md')
    if not os.path.exists(md_path):
        return f"Chapter '{chapter}' not found. Use list_chapters() to see available chapters."
    with open(md_path, 'r', encoding='utf-8') as f:
        return f.read()

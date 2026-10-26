"""Evaluation commands for CHAP CLI."""

from __future__ import annotations

def evaluate_boosting(model, data, params):
    pass


def register_commands(app):
    """Register evaluate commands with the CLI app."""
    app.command(name="evaluate-boost")(evaluate_boosting)
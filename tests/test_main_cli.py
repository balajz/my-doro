"""Tests for the mydoro CLI argument parsing."""

import sys

import pytest

from mydoro.main import parse_arguments


def test_negative_pomodoro_rejected(monkeypatch):
    """Zero/negative durations must be rejected, not silently accepted."""
    monkeypatch.setattr(sys, "argv", ["mydoro", "--pomodoro", "-5"])
    with pytest.raises(SystemExit) as exited:
        parse_arguments()
    assert exited.value.code == 2


def test_zero_cycles_rejected(monkeypatch):
    """A zero cycle count must be rejected, not silently accepted."""
    monkeypatch.setattr(sys, "argv", ["mydoro", "--cycles", "0"])
    with pytest.raises(SystemExit) as exited:
        parse_arguments()
    assert exited.value.code == 2


def test_positive_durations_accepted(monkeypatch):
    """Sane positive values must keep working."""
    monkeypatch.setattr(
        sys, "argv", ["mydoro", "--pomodoro", "25", "--cycles", "4"]
    )
    args = parse_arguments()
    assert args.pomodoro == 25
    assert args.cycles == 4

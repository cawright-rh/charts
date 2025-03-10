# -*- coding: utf-8 -*-
"""Utility class for storing test specific settings."""

from dataclasses import dataclass

@dataclass
class E2ETestSecret:
    # common secrets between one-shot and recursive tests
    test_repo: str = ''
    bot_name: str = ''
    bot_token: str = ''
    pr_number: int = -1
    vendor_type: str = ''
    owners_file_content: str = ''
    test_chart: str = ''
    test_report: str = ''
    chart_name: str = ''
    chart_version: str = ''

@dataclass
class E2ETestSecretOneShot(E2ETestSecret):
    # one-shot testing
    base_branch: str = ''
    pr_branch: str = ''
    pr_number: int = -1
    vendor: str = ''
    bad_version: str = ''

@dataclass
class E2ETestSecretRecursive(E2ETestSecret):
    # recursive testing
    software_name: str = ''
    software_version: str = ''
    pr_base_branch: str = ''
    base_branches: list = None
    pr_branches: list = None
    dry_run: bool = True
    notify_id: list = None
    submitted_charts: list = None
    release_tags: list = None

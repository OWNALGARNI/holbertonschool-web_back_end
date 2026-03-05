#!/usr/bin/env python3
"""
Simple pagination module.

Provides helper utilities and a Server class to paginate the
Popular_Baby_Names.csv dataset.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start and end indexes for a given pagination parameters."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset loaded from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return the requested page of the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        return self.dataset()[start_index:end_index]

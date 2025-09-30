from swap_meet.item import Item
from swap_meet.vendor import Vendor

def test_get_item_by_id():
    test_id = "12345"
    item_custom_id = Item(id=test_id)
    vendor = Vendor(
        inventory=[item_custom_id]
    )

    result_item = vendor.get_by_id(test_id)
    assert result_item is None

import pytest

def test_id_not_int():
    test_id = "abc"

    with pytest.raises(ValueError):
        Item(id=test_id)

from __future__ import (
    absolute_import, division, print_function, unicode_literals)

from operator import itemgetter
from ..utils import convert_amount
from decimal import Decimal
from types import SimpleNamespace
import uuid


def get_transaction_type(tr):
    if tr.get(Fields.check_num):
        return "CHECK"
    if convert_amount(tr.get(Fields.amount)) < 0:
        return "DEBIT"
    return "CREDIT"


Fields = SimpleNamespace(
    account="Account",
    amount="Amount",
    balance="Balance",
    category="Category",
    check_num="Check #",
    date="Date",
    id="id",
    memo="Memo/Notes",
    payee="Payee",
    split="Split",
)


mapping = {
    'has_header': True,
    'is_split': False,
    'balance': lambda tr: convert_amount(tr.get(Fields.balance)),
    'class': itemgetter(Fields.category),
    'currency': 'USD',
    'account': 'Towne Bank',
    'date': itemgetter(Fields.date),
    'type': get_transaction_type,
    'amount': itemgetter(Fields.amount),
    'payee': itemgetter(Fields.payee),
    'check_num': itemgetter(Fields.check_num),
    'memo': itemgetter(Fields.memo),
    'bank_id': itemgetter(Fields.account),
    'account_id': itemgetter(Fields.category),
}

"""Команда"""

from datetime import datetime
from enum import Enum
from pathlib import Path
from sys import path


class Operation(Enum):
    DEPOSIT = 110
    WITHDRAW = 220
    
    
class Logger:
    default_log_path: str | Path = Path(path[0]) / 'command1.log'
    
    @classmethod
    def append_log(cls, data: str, log_path: str | Path = None):
        if not log_path:
            log_path = cls.default_log_path
        with open(log_path, 'a', encoding='utf-8') as fileout:
            fileout.write(f'{datetime.now():%Y-%m-%d %H:%M:%S} - {data}')


class BankAccount:
    """Адресат"""
    overdraft: int = -500
    
    def __init__(self, initial_amount: int = 0):
        self.balance: int = initial_amount

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if (result := self.balance - amount) >= self.overdraft:
            self.balance = result
            return True
        return False

    def __repr__(self):
        return f'{self.balance}'
    

class BACommand:
    """Команда"""
    def __init__(
            self,
            bank_account: BankAccount,
            operation: Operation,
            amount: int
    ):
        self.account = bank_account
        self.operation = operation
        self.amount = amount
        self.succes: bool = False
    
    def __log(self, *, undo: bool = False):
        if undo:
            data = 'UNDO'
        else:
            data = 'OK' if self.succes else 'FAIL'
        data += f' - {self.operation.name}: {self.amount} - {self.account!r}'
        # Logger.append_log(data)
        print(data)

    def execute(self) -> None:
        if not self.succes:
            if self.operation is Operation.DEPOSIT:
                self.account.deposit(self.amount)
                self.succes = True
            elif self.operation is Operation.WITHDRAW:
                self.succes = self.account.withdraw(self.amount)
            self.__log()

    def undo(self) -> None:
        if self.succes:
            if self.operation is Operation.DEPOSIT:
                self.account.withdraw(self.amount)
            elif self.operation is Operation.WITHDRAW:
                self.account.deposit(self.amount)
            self.succes = False
            self.__log(undo=True)


# >>> account = BankAccount()
# >>> account.__dict__
# {'balance': 0}
# >>>
# >>> account = BankAccount(100)
# >>> account.__dict__
# {'balance': 100}
# >>>
# >>> cmd1 = BACommand(account, Operation.DEPOSIT, 5000)
# >>> account.__dict__
# {'balance': 100}
# >>> cmd1.execute()
# OK - DEPOSIT: 5000 - 5100
# >>> account.__dict__
# {'balance': 5100}
# >>>
# >>> cmd1 = BACommand(account, Operation.WITHDRAW, 50000)
# >>> cmd1.execute()
# FAIL - WITHDRAW: 50000 - 5100
# >>> account.__dict__
# {'balance': 5100}
# >>>
# >>> cmd1 = BACommand(account, Operation.WITHDRAW, 5000)
# >>> cmd1.execute()
# OK - WITHDRAW: 5000 - 100
# >>>
# >>> account.__dict__
# {'balance': 100}
# >>>
# >>> cmd1.execute()
# >>> account.__dict__
# {'balance': 100}
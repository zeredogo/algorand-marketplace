from pyteal import *

from marketplace_contract import Product


if __name__ == "__main__":
    approval_program = Product().approval_program()
    clear_program = Product().clear_program()
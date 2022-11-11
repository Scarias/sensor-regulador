import argparse

import messengers.messenger_1 as msg1
import messengers.messenger_2 as msg2

parser = argparse.ArgumentParser(
    prog='Producer runner',
    description='Corre el messenger indicado'
)
parser.add_argument(
    'messenger_number',
    type=int,
    choices=range(1, 3)
)

args = parser.parse_args()

cases = {
    1: msg1,
    2: msg2
}
if cases[args.messenger_number]:
    cases[args.messenger_number].process()

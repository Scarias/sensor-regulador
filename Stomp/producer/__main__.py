import argparse
import importlib

import messengers

parser = argparse.ArgumentParser(
    prog = 'Producer runner',
    description = 'Corre el messenger indicado'
)
parser.add_argument(
    'messenger_number',
    type=int,
    choices=range(1, len(messengers.__all__)+1)
)

args = parser.parse_args()

messenger = importlib.import_module(f'messengers.messenger_{args.messenger_number}')
messenger.process()

import logging
import argparse
import re
import numpy as np
import pandas as pd
from pandas.io.pytables import dropna_doc

logger = logging.getLogger(__name__)

def print_output(text):
    """Print to STDOUT and additionally to the logger (in case the --logfile
    option was specified)"""
    print(text)
    logger.info(text)

def main(args):
    logger.info("*** Data clean started ***")
    logger.info(args)

    inputfile = args.input_file
    logger.info("Parsing input file: " + inputfile)
    outputfile = inputfile[:(len(inputfile)-5)]+'_cleaned.xlsx'
    logger.info("Parsing output file: " + outputfile)

    try:
        tb = pd.read_excel(inputfile)

        num_row = tb.shape[0]
        num_col = tb.shape[1]

        print_output(f"Total lines are {num_row}")
        print_output("Total columns are %s" %num_col)

        p1_value = tb.iat[5, 9]
        p2_value = tb.iat[5, 11]

        tablehead = ['CoCd', 'Account Code', 'Texts', 'Reporting Periods'+p1_value, 'Comparison Periods'+p2_value, 'Abs. difference',
                     'Pct.Dif']
        new_tb = tb.iloc[7:(num_row + 1), [2, 4, 7, 10, 12, 14, 16]]
        new_tb.columns = tablehead

        new_tb.to_excel(outputfile, index=False)
        print_output('A new excel file {0} is generated done'.format(outputfile))

    except:
        print_output('Invalid file name or format!')



def configure_logger(logger, log_file=None, log_level=logging.INFO):
    """Configure logger with formatting, set log level, and optionally save
    to a file

    Args:
        logger: logger object to configure

        log_file: optional path to log file

        log_level: log level (e.g. DEBUG, INFO, WARN)
    """
    formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
    if log_file:
        file_handler = logging.FileHandler(filename=log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    logger.setLevel(log_level)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Data clean for TB",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("input_file", type=str,
        help="the input file should be a valid .xlsx file ")
    parser.add_argument("--logfile", type=str,
        help="output log filename")
    parser.add_argument("--verbose", action="store_true",
        help="verbose logging")
    args = parser.parse_args()

    configure_logger(logger, log_file=args.logfile,
        log_level=logging.DEBUG if args.verbose else logging.INFO)

    main(args)

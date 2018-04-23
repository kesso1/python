"""Illustration how Python can be used to perform SQL-like
   processing of data from CSV files. """

from functools import reduce
import operator
from collections import namedtuple

SalesRecord = namedtuple('SalesRecord', 'transaction_id date time customer_id department amount')


def pretty_print_sales_record(record):
    """Pretty format print the supplied SalesRecord."""
    print(f'{record.transaction_id:>5} {record.date:>12} {record.time:>10} '
          f'{record.customer_id:>3} {record.department:>12} '
          f'{record.amount:7.2f}')


def process_sales_query(file_name, query_func, *query_func_args):
    """Open the specified sales CSV file and parses it, generates a iterator of SalesRecord which
       it then passes to query_func along with query_func_args."""
    with open(file_name) as file:
        next(file)  # skip header line (the first line in the file)

        # split each text line at the comma (',') -> turns each text line into an array of strings
        split_strings = map(lambda line: line.split(','), file)

        # Parse the array for each record and create a SalesRecord named tuple
        records = map(lambda record_array: SalesRecord(transaction_id=int(record_array[0]),
                                                       date=record_array[1],
                                                       time=record_array[2],
                                                       customer_id=int(record_array[3]),
                                                       department=record_array[4],
                                                       amount=float(record_array[5])), split_strings)
        query_func(records, *query_func_args)


def list_purchases_of_customer(sales_records_iter, customer_id):
    """List all purchases made by one specific customer."""
    sales_for_customer = filter(lambda s: s.customer_id == customer_id, sales_records_iter)
    for record in sales_for_customer:
        pretty_print_sales_record(record)


def list_total_sales(sales_records_iter):
    """List the total amount of sales."""
    amounts = map(lambda record: record.amount, sales_records_iter)
    total_sales = reduce(operator.add, amounts)
    # Alternatively, the following is also possible:
    # total_sales = reduce(lambda x, y: x + y, amounts)
    # total_sales = sum(amounts)
    print('total sales {:.2f}'.format(total_sales))


def list_min_max_avg_sales(sales_records_iter):
    """List the min, max, sum, and average sale amount."""
    amounts = map(lambda record: record.amount, sales_records_iter)
    min_max_sum_count = reduce(lambda agg, value: (min(agg[0], value), max(agg[1], value), agg[2] + value, agg[3] + 1),
                               amounts, (float("inf"), 0, 0, 0))
    print('aggregate sales: min={:.2f}, max={:.2f}, sum={:.2f}, count={}, avg={:.2f}'.format(
        min_max_sum_count[0], min_max_sum_count[1], min_max_sum_count[2], min_max_sum_count[3],
        min_max_sum_count[0]/min_max_sum_count[3]))


def agg_func(partial_agg, record):
    """Helper function to compute the partial aggregate for the group-by query.
       Since multiline lambdas are not supported in Python, we use a normal function."""
    department, amount = record
    partial_agg[department] = partial_agg.get(department, 0) + amount
    return partial_agg


def list_sales_per_department(sales_record_iter):
    """Group-by query for sales per department."""
    dep_amounts = map(lambda record: (record.department, record.amount),
                      sales_record_iter)
    dep_sum = reduce(agg_func, dep_amounts, {})
    print('sales per department:')
    for dep, sales in dep_sum.items():
        print('{:>12} {:.2f}'.format(dep, sales))


def list_sales_per_department_sorted_descending_sales(sales_record_iter):
    """Fancy version of Group-by query for sales per department orders results
       by sales in descending order."""
    dep_amounts = map(lambda record: (record.department, record.amount), sales_record_iter)
    dep_sum = reduce(agg_func, dep_amounts, {})
    sorted_dep_sum = sorted(dep_sum.items(), key=lambda t: t[1], reverse=True)
    print('sales per department, sorted descending:')
    for dep, sales in sorted_dep_sum:
        print('{:>12} {:.2f}'.format(dep, sales))


if __name__ == '__main__':
    FILE_NAME = 'mocksales.csv'
    process_sales_query(FILE_NAME, list_purchases_of_customer, 23)
    process_sales_query(FILE_NAME, list_total_sales)
    process_sales_query(FILE_NAME, list_min_max_avg_sales)
    process_sales_query(FILE_NAME, list_sales_per_department)
    process_sales_query(FILE_NAME, list_sales_per_department_sorted_descending_sales)
import xlrd
import random

from utils.search_data import SearchData


class ExcelReader:
    @staticmethod
    def get_products_data(amount_of_products_to_check):
        wb = xlrd.open_workbook("../utils/first_page_sample_single_products.xls")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchData(sheet.cell(i, 0).value, sheet.cell(i, 1).value)
            data.append(search_data)

        all_products_number = len(data)

        # Ensure 'x' is not greater than the number of available products
        x = min(amount_of_products_to_check, all_products_number)

        # Randomly select 2 distinct numbers within the range [0, all_products_number-1]
        random_indices = random.sample(range(all_products_number), x)

        # Get the corresponding values from the 'data' list based on the selected indices
        random_values = [data[i] for i in random_indices]

        return random_values

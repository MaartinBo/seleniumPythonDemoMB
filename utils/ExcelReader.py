import xlrd

from utils.search_data import SearchData


class ExcelReader:
    @staticmethod
    def get_products_data():
        wb = xlrd.open_workbook("../utils/testProductsData.xls")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchData(sheet.cell(i, 0).value, sheet.cell(i, 1).value)
            data.append(search_data)
        return data

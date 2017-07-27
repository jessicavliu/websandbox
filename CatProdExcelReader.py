import xlrd

from Product import Product
from Category import Category

#helper method
def get_cell_values(path, sheet_num, first_row, last_row):
	book = xlrd.open_workbook(path)

	#checking if sheet exists
	if sheet_num > book.nsheets:
		print("Error: sheet not found")
		return

	sheet = book.sheet_by_index(sheet_num - 1)

	#checking for bad input
	if sheet.nrows == 0:
		print("Error: your input is an empty sheet")
		return
	if sheet.ncols != 4:
		print("Error: did not provide the correct number of columns in the spreadsheet. You should have 4 values per row: an identifier, name, description, and parent, in that order.")
		return
	if last_row > sheet.nrows:
		print("Error: out of range. You don't have data filled up to row %s. Your last row of data is %s." % (str(last_row), str(sheet.nrows)))
		return

	all_data_list = []
	for row in range(first_row - 1, last_row):
		obj_info = []
		for i in range(len(sheet.row(row))):
			value =sheet.cell(row, i).value
			value = value.replace(u'\xa0', u' ')
			obj_info.append(value)
		all_data_list.append(obj_info)
	return all_data_list

#path:location of workbook
#sheet_num: leftmost sheet is 1, increments as you continue going right
#first_row: first row with cell values you want to retrieve
#last_row: last row with cell values you want to retrieve
#cat_dict: a Category dictionary that will be referenced when finding the Product's parent category
def get_prod_dict_from_cells(path, sheet_num, first_row, last_row, cat_dict):
	all_data_list = get_cell_values(path, sheet_num, first_row, last_row)
	if all_data_list == [] or all_data_list == None or all_data_list == '' or all_data_list == 0:
		return("Error: can't get cell values")
	
	prod_dict = {}
	for l in all_data_list:
		if l[3] == 'None':
			prod_dict[l[0]] = Product(l[1], l[2], None)
		else:
			#TODO: throw error if prod_dict[l[3]] doesn't exist
			prod_dict[l[0]] = Product(l[1], l[2], cat_dict[l[3]])
	return prod_dict

#same params as get_prod_dict_from_cells except no cat_dict
#parent_cat seems sketch
def get_cat_dict_from_cells(path, sheet_num, first_row, last_row):
	all_data_list = get_cell_values(path, sheet_num, first_row, last_row)
	if all_data_list == [] or all_data_list == None or all_data_list == '' or all_data_list == 0:
		return("Error: can't get cell values")
	
	cat_dict = {}
	for l in all_data_list:
		if l[3] == 'None':
			cat_dict[l[0]] = Category(l[1], l[2], None)
		else:
			cat_dict[l[0]] = Category(l[1], l[2], cat_dict[l[3]])
	return cat_dict
		
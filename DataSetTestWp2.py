from ProductDataSet import ProductDataSet
from CategoryDataSet import CategoryDataSet

from Product import Product
from Category import Category

tbl_header = "wp_2"
catset = CategoryDataSet(tbl_header)
prodset = ProductDataSet(tbl_header)

#17
p = 'pink'
print("What is the length of prod(s) p?")
print(prodset.find_prod_length(p))
print()

#18
extrema = "max"
group = "Music"
print("Longest/smallest length prod in cat/store")
print(prodset.find_extrema_length(extrema, group))
print()

#19
print("order prods based on length asc/desc")
print(prodset.order_prods_by_length("asc"))
print()


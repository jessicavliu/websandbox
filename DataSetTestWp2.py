from ProductDataSet import ProductDataSet
from CategoryDataSet import CategoryDataSet

from Product import Product
from Category import Category

tbl_header = "wp_2"
catset = CategoryDataSet(tbl_header)
prodset = ProductDataSet(tbl_header)

#Printing out output
#Make into test cases

#1: How many categories are there total?
print(catset.num_categories())
print()

#2:List all categories
print(catset.list_categories())
print()

#3: List all categories and the number of products they have
print(catset.list_categories_and_prods())
print()

#4: Given a category c, how many products are there in c? 
c = 'pink'
print(catset.find_num_of_prods_in_cat(c))
print()

#5: Which category has the most products?
print(catset.cat_max_prods())
print()

#6: Which category has the least products?
print(catset.cat_min_prods())
print()

#7: What is the description for category c?
c = 'pink'
print(catset.get_cat_description(c))
print()

#7.1: Return descriptions of all cats with name c
c = 'pink'
print(catset.get_cat_descriptions(c))
print()

#7.2: Does content s match the description for any cat?
s = "pink"
print(catset.does_any_cat_match_search(s))
print()

#7.3: Does content s exist for any category named c?
s = "pink"
c = "green"
print(catset.does_search_match_cat(s, c))
print()

#7.4: Does content s exist for a list of category c = [c1, c2, ...]?
#works for strings that are not actually cat names -- uh so this mean the test failed?
s = "X11 greens"
c_list = ["green", "pink"]
print(catset.does_search_match_list_cat(s, c_list))
print()

#7.5: Return instances where string s is content for a category.
#test further
s = "X11"
print(catset.find_cat_match(s))
print()

#7.6: Return instances where string s is a substring for content for category
s = "X11"
print(catset.find_cat_substring_match(s))
print()

#8: Does category c have a parent category?
c = 'cyan'
print(catset.has_parent(c))
print()

#9: What is the parent of category c?
c = 'cyan'
print(catset.parent_of_cat(c))
print()

#9.5: List all parent categories
print(catset.list_parent_cats())
print()


#---
###TEST

#Printing out output
#Make into test cases

#10: Given product name p, does p exist?
p = "pinks"
print(prodset.exists_prod(p))
print()

#11: List all product names
print(prodset.list_prod_names())
print()

#12: Return content/description of prod p
p = 'pink'
print(prodset.get_prod_description(p))
print()

#13: Return content/description of all prods with name p
p = 'pink'
print(prodset.get_prod_descriptions(p))
print()

#14: Does content s match the description for any prod?
s = 'FFC0CB'
print(prodset.does_search_match(s))
print()

#14.5: Does content s match the description for a prod(s) named p?
s = 'FFC0CB'
p = 'pink'
print(prodset.does_search_match_prod(s, p))
print()

#14.75: Does content s match the description for a list of prods p?
#inserting new prod. reqs: no description
#when formulating test cases paste this and other insertions at the top
#look up MERGE
#self.cursor.execute("IF EXISTS (SELECT * FROM wp_posts WHERE post_type = 'product' and post_title = 'Test 14.75.')")
s = 'FFC0CB'
p_list = ['aqua', 'cyan', 'pink']
print(prodset.does_search_match_list_prods(s, p_list))
print()

#15: Return instances where search s is description for a prod
s = 'FFC0CB'
print(prodset.find_match(s))
print()

#16: Return instances where string c is a substring for content for a prod
s = 'FF'
print(prodset.find_substring_match(s))
print()

#17: What is the length of the prod(s) p?
p = 'tomato'
print(prodset.find_prod_length(p))
print()

#18: longest/smallest length prod in cat/store
print(prodset.find_extrema_length(extrema="max", group = "blue"))
print(prodset.find_extrema_length(extrema="min", group = "blue"))
print(prodset.find_extrema_length(extrema="max"))
print(prodset.find_extrema_length(extrema="min"))
print()

#19: Order prods based on length asc/desc
print(prodset.order_prods_by_length("desc"))
print()

#20: List all products with length l
l = 3
print(prodset.find_prods_with_len(l))
print()

#20.1: List number of prods with length l
l = 3
print(prodset.find_num_prods_with_len(l))
print()

#20.2: List all categories with products with length l
print(prodset.find_cats_with_len(l))
print()

#20.3: List num of categories with products with length l
print(prodset.find_num_cats_with_len(l))
print()

#20.4: list all prods in store in a certain range of length
min, max = 3, 3
print(prodset.find_prods_in_range(min, max))
print()

#20.5: list number of prods in store in a certain range of length
min, max = 3, 3
print(prodset.find_num_prods_in_range(min, max))
print()

#20.6: list all cats in store in a certain range of length
min, max = 3, 3
print(prodset.find_cats_in_range(min, max))
print()

#20.7: list number of cats in store in a certain range of length
min, max = 3, 3
print(prodset.find_num_cats_in_range(min, max))
print()

prodset.getDb().close()
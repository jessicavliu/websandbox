from ProductDataSet import ProductDataSet
from CategoryDataSet import CategoryDataSet

tbl_header = "wp"
catset = CategoryDataSet(tbl_header)
prodset = ProductDataSet(tbl_header)

#-----------------------------------------
###TEST

#Printing out output
#Make into test cases
#1
print("How many categories are there total?")
print(catset.num_categories())
print()

#2
print("List all categories")
print(catset.list_categories())
print()

#3
print("List all categories and the number of prods they have.")
print(catset.list_categories_and_prods())
print()

#4
c = 'Music'
print("Given the category " + c + ", how many products are there in " + c + "?")
print(catset.find_num_of_prods_in_cat(c))
print()

#5
print("Which category has the most products?")
print(catset.cat_max_prods())
print()

#6
print("Which category has the least products?")
print(catset.cat_min_prods())
print()

#7
c = 'Music'
print("What is the description for category " + c + "?")
print(catset.get_cat_description(c))
print()

#7.1
c = 'Music'
print("Return descriptions of all categories with name " + c)
print(catset.get_cat_descriptions(c))
print()

#7.2
s = "test"
print("Does content s exist for any category descriptions?")
print(catset.does_any_cat_match_search(s))
print()

#7.3
s = "test"
c = "Music"
print("Does content s exist for any category named c?")
print(catset.does_search_match_cat(s, c))
print()

#7.4
#works for strings that are not actually cat names
s = "test"
c_list = ["Singles", "Music"]
print("Does content s exist for a list of category c = [c1, c2, ...]?")
print(catset.does_search_match_list_cat(s, c_list))
print()

#7.5
#test further
s = "test"
print("Return instances where string s is content for a category.")
print(catset.find_cat_match(s))
print()

#7.6
s = ""
print("Return instances where string s is a substring for content for category.")
print(catset.find_cat_substring_match(s))
print()

#8
c = 'Music'
print("Does category " + c + " have a parent category?")
print(catset.has_parent(c))
print()

#9
c = 'Hoodies'
print ("What is the parent of category " + c + "?")
print(catset.parent_of_cat(c))
print()

#9.5
print("List all parent categories")
print(catset.list_parent_cats())
print()

catset.getDb().close()

#---
###TEST

#Printing out output
#Make into test cases

#10
p = "Woo Ninja"
print("Given product name " + p + ", does it exist?")
print(prodset.exists_prod(p))
print()

#11
print("List all product names")
print(prodset.list_prod_names())
print()

#12
p = 'Woo Ninja'
print("Return description of prod p")
print(prodset.get_prod_description(p))
print()

#13
p = 'Woo Ninja'
print("Return description of all prods with name p")
print(prodset.get_prod_descriptions(p))
print()

#14
s = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.'
print("Does content c exist for any prod?")
print(prodset.does_search_match(s))
print()

#14.5
s = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.'
p = 'Woo Ninja'
print("Does content s match the description for a prod(s) named p?")
print(prodset.does_search_match_prod(s, p))
print()

#14.75
#inserting new prod. reqs: no description
#when formulating test cases paste this and other insertions at the top
#look up MERGE
#self.cursor.execute("IF EXISTS (SELECT * FROM wp_posts WHERE post_type = 'product' and post_title = 'Test 14.75.')")

s = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.'
p_list = ['Test 14.75', 'Woo Ninja']
print("Does content s match the description for a list of prods p?")
print(prodset.does_search_match_list_prods(s, p_list))
print()

#15
s = 'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.'
print("Return instances where string s is content for a prod")
print(prodset.find_match(s))
print()

#16
s = 'Pellentesque'
print("Return instances where string c is a substring for content for a prod")
print(prodset.find_substring_match(s))
print()

#17
p = 'Woo Ninja'
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
print(prodset.order_prods_by_length("desc"))
print()

#20
print("List all prods in cat in a certain range of length")
print()
print()


prodset.getDb().close()

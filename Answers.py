import MySQLdb

db = MySQLdb.connect(host = 'localhost',
                     user = 'root'
    )
#Preprocessing
#Creating a table from inner join and populating it with info
CREATE TABLE product_cat as 
	SELECT wp_term_taxonomy.term_id,
	wp_term_taxonomy.term_taxonomy_id, 
	wp_terms.name,  
	wp_term_taxonomy.taxonomy, 
	wp_term_taxonomy.description, 
	wp_term_taxonomy.parent, 
	wp_term_taxonomy.count 
	FROM wp_terms 
	INNER JOIN wp_term_taxonomy 
	ON wp_terms.term_id = wp_term_taxonomy.term_id 
	WHERE wp_term_taxonomy.taxonomy = 'product_cat';

#Check if table exists



#How many categories are there total?
SELECT COUNT(*) FROM wp_term_taxonomy WHERE taxonomy = 'product_cat';

#List all categories
SELECT name FROM product_cat
 
#Given a category x, how many products are there in x?
SELECT count FROM product_cat where name = x

#Which category has the most products?
SELECT name, count from product_cat 
#Store in a dictionary (name:count); find max

#What is the description for category x?
SELECT description from product_cat where name = x

#Does x have a parent category?
has_parent = SELECT parent from product_cat
	if has_parent == ‘’
		return false
	return true
 
#Product
###Given product name p, does p exist?
SELECT * in wp_posts where wp_type = “product” and post_title = “p”

###List all product names
SELECT t1.id, t1.post_title
	FROM wp_posts t1 
	INNER JOIN wp_term_relationships t2
		ON t1.id = t2.object_id 
	 INNER JOIN wp_term_taxonomy t3
		ON t2.term_taxonomy_id = t3.term_taxonomy_id
		WHERE t3.taxonomy = 'product_cat'
	GROUP BY t1.id
	ORDER BY t1.id;

#return name only = select t1.post_title

###Is p in stock?
NO ANSWER
"don't think my site has the functionality to check yet"
 
###Return p’s price/quantity/number of colors it comes in/rating/weight/etc
NO ANSWER

###Return list of all reviews for product x
#Note: currently using post title = x 
#but may have to change to unique branding
#like id = x
SELECT t1.comment_id, t1.comment_content, t2.post_title
FROM wp_comments t1
INNER JOIN  wp_posts t2
ON t1.comment_post_id = t2.id
WHERE t2.post_title = x

###Return total ratings
NO ANSWER

###Return rating for comments for product x
#Note: currently using post title = x 
#but may have to change to unique branding
#like id = x
SELECT meta_value 
FROM wp_comment_meta t1
INNER JOIN wp_comments t2
ON t1.comment_id = t2.comment_id
INNER JOIN wp_posts t3
ON t2.comment_post_id = t3.id
WHERE t1.meta_key = 'rating'
AND t3.post_title = x

###Return p’s most recent review
SELECT meta_value, comment_content
FROM wp_comment_meta t1
INNER JOIN wp_comments t2
ON t1.comment_id = t2.comment_id
INNER JOIN wp_posts t3
ON t2.comment_post_id = t3.id
WHERE t1.meta_key = 'rating'
AND t3.post_title = x
ORDER BY 

#Return if p has > epsilon reviews
#Return p’s related products (customers also bought, recommended)
NO ANSWER

#Sorting. Is a category because these answers are hard to find=__=
#What is the highest rated/most popular/etc product in catagory x?
NO ANSWER
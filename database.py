import mysql.connector
db = mysql.connector.connect(host="localhost",user="khurana",passwd="ishika321",database="skincare_suggestion")

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE skincare_suggestion")


#mycursor.execute("CREATE TABLE UserInfo(User_id int primary key,User_name varchar(100),Email varchar(100),Phone_number varchar(10),gender varchar(10),age int)")

#mycursor.execute("INSERT INTO UserInfo(User_id,User_name,Email,Phone_number,gender,age) VALUES(1,'i','ish','345','f',23)")

#db.commit()




'''('Oily', 'Acne', 'Salicylic Acid, Niacinamide, Zinc PCA', 'Coconut Oil, Lanolin, Mineral Oil'),
('Oily', 'Redness', 'Niacinamide, Centella Asiatica, Green Tea', 'Alcohol Denat, Essential Oils'),
('Oily', 'Dullness', 'Vitamin C, Lactic Acid, Squalane', 'Alcohol, Harsh Exfoliants'),
('Oily', 'Pigmentation', 'Azelaic Acid, Licorice Root, Alpha Arbutin', 'Fragrance, Harsh Acids'),
('Oily', 'Sensitivity', 'Panthenol, Allantoin, Oat Extract', 'Fragrance, Essential Oils'),
('Oily', 'Aging', 'Retinol, Peptides, Ceramides', 'Strong AHAs, Fragrance'),
('Oily', 'Uneven Texture', 'Glycolic Acid, Niacinamide, Azelaic Acid', 'Physical Scrubs, Fragrance'),
('Oily', 'Large Pores', 'Salicylic Acid, Niacinamide, Clay', 'Heavy Oils, Silicones'),
('Oily', 'Dehydration', 'Hyaluronic Acid, Panthenol, Glycerin', 'Alcohol Denat, Fragrance'),
('Oily', 'Brightening', 'Vitamin C, Arbutin, Ferulic Acid', 'Lemon Juice, Harsh Alcohols'),
('Oily', 'Oil Control', 'Niacinamide, Zinc PCA, Green Tea', 'Heavy Occlusives, Comedogenic Oils'),
('Oily', 'Barrier Repair', 'Ceramides, Squalane, Panthenol', 'Alcohol, Strong Actives'),

('Dry', 'Acne', 'Salicylic Acid, Niacinamide, Zinc PCA', 'Coconut Oil, Lanolin, Mineral Oil'),
('Dry', 'Redness', 'Niacinamide, Centella Asiatica, Green Tea', 'Alcohol Denat, Essential Oils'),
('Dry', 'Dullness', 'Vitamin C, Lactic Acid, Squalane', 'Alcohol, Harsh Exfoliants'),
('Dry', 'Pigmentation', 'Azelaic Acid, Licorice Root, Alpha Arbutin', 'Fragrance, Harsh Acids'),
('Dry', 'Sensitivity', 'Panthenol, Allantoin, Oat Extract', 'Fragrance, Essential Oils'),
('Dry', 'Aging', 'Retinol, Peptides, Ceramides', 'Strong AHAs, Fragrance'),
('Dry', 'Uneven Texture', 'Glycolic Acid, Niacinamide, Azelaic Acid', 'Physical Scrubs, Fragrance'),
('Dry', 'Large Pores', 'Salicylic Acid, Niacinamide, Clay', 'Heavy Oils, Silicones'),
('Dry', 'Dehydration', 'Hyaluronic Acid, Panthenol, Glycerin', 'Alcohol Denat, Fragrance'),
('Dry', 'Brightening', 'Vitamin C, Arbutin, Ferulic Acid', 'Lemon Juice, Harsh Alcohols'),
('Dry', 'Oil Control', 'Niacinamide, Zinc PCA, Green Tea', 'Heavy Occlusives, Comedogenic Oils'),
('Dry', 'Barrier Repair', 'Ceramides, Squalane, Panthenol', 'Alcohol, Strong Actives'),

('Combination', 'Acne', 'Salicylic Acid, Niacinamide, Zinc PCA', 'Coconut Oil, Lanolin, Mineral Oil'),
('Combination', 'Redness', 'Niacinamide, Centella Asiatica, Green Tea', 'Alcohol Denat, Essential Oils'),
('Combination', 'Dullness', 'Vitamin C, Lactic Acid, Squalane', 'Alcohol, Harsh Exfoliants'),
('Combination', 'Pigmentation', 'Azelaic Acid, Licorice Root, Alpha Arbutin', 'Fragrance, Harsh Acids'),
('Combination', 'Sensitivity', 'Panthenol, Allantoin, Oat Extract', 'Fragrance, Essential Oils'),
('Combination', 'Aging', 'Retinol, Peptides, Ceramides', 'Strong AHAs, Fragrance'),
('Combination', 'Uneven Texture', 'Glycolic Acid, Niacinamide, Azelaic Acid', 'Physical Scrubs, Fragrance'),
('Combination', 'Large Pores', 'Salicylic Acid, Niacinamide, Clay', 'Heavy Oils, Silicones'),
('Combination', 'Dehydration', 'Hyaluronic Acid, Panthenol, Glycerin', 'Alcohol Denat, Fragrance'),
('Combination', 'Brightening', 'Vitamin C, Arbutin, Ferulic Acid', 'Lemon Juice, Harsh Alcohols'),
('Combination', 'Oil Control', 'Niacinamide, Zinc PCA, Green Tea', 'Heavy Occlusives, Comedogenic Oils'),
('Combination', 'Barrier Repair', 'Ceramides, Squalane, Panthenol', 'Alcohol, Strong Actives'),

('Sensitive', 'Acne', 'Salicylic Acid, Niacinamide, Zinc PCA', 'Coconut Oil, Lanolin, Mineral Oil'),
('Sensitive', 'Redness', 'Niacinamide, Centella Asiatica, Green Tea', 'Alcohol Denat, Essential Oils'),
('Sensitive', 'Dullness', 'Vitamin C, Lactic Acid, Squalane', 'Alcohol, Harsh Exfoliants'),
('Sensitive', 'Pigmentation', 'Azelaic Acid, Licorice Root, Alpha Arbutin', 'Fragrance, Harsh Acids'),
('Sensitive', 'Sensitivity', 'Panthenol, Allantoin, Oat Extract', 'Fragrance, Essential Oils'),
('Sensitive', 'Aging', 'Retinol, Peptides, Ceramides', 'Strong AHAs, Fragrance'),
('Sensitive', 'Uneven Texture', 'Glycolic Acid, Niacinamide, Azelaic Acid', 'Physical Scrubs, Fragrance'),
('Sensitive', 'Large Pores', 'Salicylic Acid, Niacinamide, Clay', 'Heavy Oils, Silicones'),
('Sensitive', 'Dehydration', 'Hyaluronic Acid, Panthenol, Glycerin', 'Alcohol Denat, Fragrance'),
('Sensitive', 'Brightening', 'Vitamin C, Arbutin, Ferulic Acid', 'Lemon Juice, Harsh Alcohols'),
('Sensitive', 'Oil Control', 'Niacinamide, Zinc PCA, Green Tea', 'Heavy Occlusives, Comedogenic Oils'),
('Sensitive', 'Barrier Repair', 'Ceramides, Squalane, Panthenol', 'Alcohol, Strong Actives'),

('Normal', 'Acne', 'Salicylic Acid, Niacinamide, Zinc PCA', 'Coconut Oil, Lanolin, Mineral Oil'),
('Normal', 'Redness', 'Niacinamide, Centella Asiatica, Green Tea', 'Alcohol Denat, Essential Oils'),
('Normal', 'Dullness', 'Vitamin C, Lactic Acid, Squalane', 'Alcohol, Harsh Exfoliants'),
('Normal', 'Pigmentation', 'Azelaic Acid, Licorice Root, Alpha Arbutin', 'Fragrance, Harsh Acids'),
('Normal', 'Sensitivity', 'Panthenol, Allantoin, Oat Extract', 'Fragrance, Essential Oils'),
('Normal', 'Aging', 'Retinol, Peptides, Ceramides', 'Strong AHAs, Fragrance'),
('Normal', 'Uneven Texture', 'Glycolic Acid, Niacinamide, Azelaic Acid', 'Physical Scrubs, Fragrance'),
('Normal', 'Large Pores', 'Salicylic Acid, Niacinamide, Clay', 'Heavy Oils, Silicones'),
('Normal', 'Dehydration', 'Hyaluronic Acid, Panthenol, Glycerin', 'Alcohol Denat, Fragrance'),
('Normal', 'Brightening', 'Vitamin C, Arbutin, Ferulic Acid', 'Lemon Juice, Harsh Alcohols'),
('Normal', 'Oil Control', 'Niacinamide, Zinc PCA, Green Tea', 'Heavy Occlusives, Comedogenic Oils'),
('Normal', 'Barrier Repair', 'Ceramides, Squalane, Panthenol', 'Alcohol, Strong Actives');
'''

def skin_table(n):
	data=[]
	for _ in range(1,n+1):
		skin_type=fake.random_element('Oily', 'Dry', 'Combination', 'Normal', 'Sensitive')
		concern=fake.random_element('Acne', 'Redness', 'Dullness', 'Pigmentation', 'Sensitivity', 'Aging', 'Uneven Texture', 'Large Pores', 'Dehydration', 'Brightening', 'Oil Control', 'Barrier Repair')
		recommendation=fake.random_element('Salicylic Acid, Niacinamide, Zinc PCA','Vitamin C, Lactic Acid, Squalane','Azelaic Acid, Licorice Root, Alpha Arbutin','Panthenol, Allantoin, Oat Extract','Retinol, Peptides, Ceramides','Hyaluronic Acid, Panthenol, Glycerin')
		to_avoid=fake.random_element('Fragrance, Essential Oils','Alcohol Denat, Mineral Oil','Coconut Oil, Lanolin','Strong AHAs, Harsh Exfoliants','Comedogenic Oils', 'Silicones')
		data.append(skin_type,concern,recommendation,to_avoid)

	mycursor.execute("INSERT INTO SkinInfo (skin_type, concern, recommendation, to_avoid) VALUES(%s,%s,%s,%s)",data)

	print("data added")

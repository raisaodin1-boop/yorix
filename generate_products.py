#!/usr/bin/env python3
import json
import random

# Vendor mapping (will be filled from database)
vendors = {
    'CamTech Mobile Shop': {'category': 'Phones & Accessories', 'location': 'Douala'},
    'Douala Tech Hub': {'category': 'Electronics', 'location': 'Douala'},
    'Mama Clarisse Food Market': {'category': 'Food & Groceries', 'location': 'Yaoundé'},
    'Marché Mokolo Boutique': {'category': 'Fashion', 'location': 'Yaoundé'},
    'Bamenda Fashion House': {'category': 'Fashion', 'location': 'Bamenda'},
    'AfriBeauty Store': {'category': 'Beauty & Cosmetics', 'location': 'Douala'},
    'Briquetterie Hardware Shop': {'category': 'Construction & Home Repair', 'location': 'Yaoundé'},
    'Carrefour Market Boutique': {'category': 'Home & Kitchen', 'location': 'Douala'},
    'Buea Electronics Shop': {'category': 'Electronics', 'location': 'Buea'},
    'Limbe Moto Parts': {'category': 'Auto & Moto Accessories', 'location': 'Limbe'},
    'Bafoussam Local Products': {'category': 'Local Products', 'location': 'Bafoussam'},
    'Maroua Artisan Market': {'category': 'Local Products', 'location': 'Maroua'},
    'Douala Service Pros': {'category': 'Services', 'location': 'Douala'},
    'Yaoundé Phone Repair': {'category': 'Services', 'location': 'Yaoundé'},
    'Grand Marché Electronics': {'category': 'Electronics', 'location': 'Yaoundé'},
    'Douala Fashion Outlet': {'category': 'Fashion', 'location': 'Douala'},
    'Yaoundé Home Essentials': {'category': 'Home & Kitchen', 'location': 'Yaoundé'},
    'Bamenda Food Supply': {'category': 'Food & Groceries', 'location': 'Bamenda'},
    'Kribi Beauty Corner': {'category': 'Beauty & Cosmetics', 'location': 'Kribi'},
    'Yaoundé Central Market Store': {'category': 'Electronics', 'location': 'Yaoundé'},
}

# Product templates for each category
products_templates = {
    'Phones & Accessories': [
        {'title': 'Tecno Spark 10 Pro', 'description': 'Latest Tecno smartphone with 128GB storage, 6.8" display, and 5000mAh battery. Perfect for everyday use.', 'price': 85000, 'image': 'https://images.pexels.com/photos/788946/pexels-photo-788946.jpeg'},
        {'title': 'Infinix Smart 7 HD', 'description': 'Affordable smartphone with dual camera, Android 12, and long battery life. Great value for money.', 'price': 55000, 'image': 'https://images.pexels.com/photos/1092644/pexels-photo-1092644.jpeg'},
        {'title': 'Samsung Galaxy A14', 'description': 'Samsung quality with 64GB storage, triple camera, and premium design. Reliable and fast.', 'price': 110000, 'image': 'https://images.pexels.com/photos/699122/pexels-photo-699122.jpeg'},
        {'title': 'iPhone 11 Refurbished', 'description': 'Certified refurbished iPhone 11 in excellent condition. Comes with 6 months warranty.', 'price': 185000, 'image': 'https://images.pexels.com/photos/788946/pexels-photo-788946.jpeg'},
        {'title': 'Tecno Pop 7 Pro', 'description': 'Budget-friendly phone with essential features. Perfect starter phone for students.', 'price': 38000, 'image': 'https://images.pexels.com/photos/1092644/pexels-photo-1092644.jpeg'},
        {'title': 'Infinix Hot 30i', 'description': 'Mid-range phone with great camera and fast charging. Popular choice in Cameroon.', 'price': 72000, 'image': 'https://images.pexels.com/photos/699122/pexels-photo-699122.jpeg'},
        {'title': 'Xiaomi Redmi 12C', 'description': 'Xiaomi quality at affordable price. 4GB RAM and dual camera system.', 'price': 62000, 'image': 'https://images.pexels.com/photos/1092644/pexels-photo-1092644.jpeg'},
        {'title': 'iPhone XR Refurbished', 'description': 'Premium iPhone experience at great price. Fully tested and certified.', 'price': 165000, 'image': 'https://images.pexels.com/photos/699122/pexels-photo-699122.jpeg'},
        {'title': 'Phone Charger USB-C Fast', 'description': 'Universal fast charger compatible with most smartphones. 25W fast charging.', 'price': 3500, 'image': 'https://images.pexels.com/photos/4219861/pexels-photo-4219861.jpeg'},
        {'title': 'Wireless Earbuds TWS', 'description': 'Bluetooth 5.0 earbuds with charging case. Crystal clear sound quality.', 'price': 8500, 'image': 'https://images.pexels.com/photos/3587478/pexels-photo-3587478.jpeg'},
        {'title': 'Power Bank 20000mAh', 'description': 'High capacity power bank with dual USB ports. Charge multiple devices.', 'price': 12000, 'image': 'https://images.pexels.com/photos/4219861/pexels-photo-4219861.jpeg'},
        {'title': 'Tempered Glass Screen Protector', 'description': 'Premium tempered glass for phone protection. Anti-scratch and anti-fingerprint.', 'price': 1500, 'image': 'https://images.pexels.com/photos/3587478/pexels-photo-3587478.jpeg'},
        {'title': 'Phone Case Shockproof', 'description': 'Durable protective case available in multiple colors. Perfect fit guaranteed.', 'price': 2500, 'image': 'https://images.pexels.com/photos/4219861/pexels-photo-4219861.jpeg'},
        {'title': 'USB Cable 2m Long', 'description': 'Extra long charging cable for convenience. Heavy duty and tangle-free.', 'price': 2000, 'image': 'https://images.pexels.com/photos/3587478/pexels-photo-3587478.jpeg'},
        {'title': 'Bluetooth Speaker Portable', 'description': 'Compact wireless speaker with powerful bass. 8 hours battery life.', 'price': 15000, 'image': 'https://images.pexels.com/photos/3587478/pexels-photo-3587478.jpeg'},
        {'title': 'Selfie Ring Light', 'description': 'LED ring light for perfect selfies and video calls. Adjustable brightness.', 'price': 6500, 'image': 'https://images.pexels.com/photos/4219861/pexels-photo-4219861.jpeg'},
    ],
    'Electronics': [
        {'title': '32" LED TV Samsung', 'description': 'High definition LED TV perfect for your living room. HDMI and USB ports included.', 'price': 135000, 'image': 'https://images.pexels.com/photos/1201996/pexels-photo-1201996.jpeg'},
        {'title': '43" Smart TV LG', 'description': 'Smart TV with Netflix, YouTube apps. WiFi enabled for streaming content.', 'price': 185000, 'image': 'https://images.pexels.com/photos/1201996/pexels-photo-1201996.jpeg'},
        {'title': 'Home Theater System 5.1', 'description': 'Surround sound system with powerful subwoofer. Cinema experience at home.', 'price': 95000, 'image': 'https://images.pexels.com/photos/164693/pexels-photo-164693.jpeg'},
        {'title': 'Microwave Oven 20L', 'description': 'Digital microwave with multiple cooking modes. Easy to use and clean.', 'price': 48000, 'image': 'https://images.pexels.com/photos/2343467/pexels-photo-2343467.jpeg'},
        {'title': 'Electric Blender 1.5L', 'description': 'Powerful blender for smoothies and soups. Multiple speed settings.', 'price': 18000, 'image': 'https://images.pexels.com/photos/6508357/pexels-photo-6508357.jpeg'},
        {'title': 'Rice Cooker 2.8L', 'description': 'Automatic rice cooker with keep-warm function. Perfect rice every time.', 'price': 22000, 'image': 'https://images.pexels.com/photos/2343467/pexels-photo-2343467.jpeg'},
        {'title': 'Electric Kettle 1.8L', 'description': 'Fast boiling kettle with auto shut-off. Stainless steel design.', 'price': 12000, 'image': 'https://images.pexels.com/photos/6508357/pexels-photo-6508357.jpeg'},
        {'title': 'Iron Box Steam', 'description': 'Steam iron for wrinkle-free clothes. Non-stick soleplate.', 'price': 15000, 'image': 'https://images.pexels.com/photos/2343467/pexels-photo-2343467.jpeg'},
        {'title': 'Table Fan 16 Inch', 'description': 'Powerful cooling fan with 3-speed settings. Oscillating function.', 'price': 18000, 'image': 'https://images.pexels.com/photos/5591581/pexels-photo-5591581.jpeg'},
        {'title': 'Standing Fan 18 Inch', 'description': 'Large standing fan with remote control. Ideal for large rooms.', 'price': 28000, 'image': 'https://images.pexels.com/photos/5591581/pexels-photo-5591581.jpeg'},
        {'title': 'Laptop HP 14 inch', 'description': 'Intel Core i3, 4GB RAM, 500GB HDD. Perfect for students and office work.', 'price': 185000, 'image': 'https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg'},
        {'title': 'Wireless Mouse Logitech', 'description': 'Ergonomic wireless mouse with long battery life. Silent clicking.', 'price': 8500, 'image': 'https://images.pexels.com/photos/2115256/pexels-photo-2115256.jpeg'},
        {'title': 'USB Flash Drive 64GB', 'description': 'High speed USB 3.0 flash drive. Reliable data storage.', 'price': 6500, 'image': 'https://images.pexels.com/photos/2881233/pexels-photo-2881233.jpeg'},
        {'title': 'External Hard Drive 1TB', 'description': 'Portable storage for backup and file transfer. USB 3.0 fast speed.', 'price': 35000, 'image': 'https://images.pexels.com/photos/2881233/pexels-photo-2881233.jpeg'},
        {'title': 'Headphones Wireless', 'description': 'Bluetooth headphones with noise cancellation. Comfortable for long use.', 'price': 25000, 'image': 'https://images.pexels.com/photos/3587478/pexels-photo-3587478.jpeg'},
    ],
    'Fashion': [
        {'title': 'Ankara Dress Women', 'description': 'Beautiful African print dress in vibrant colors. Perfect for special occasions.', 'price': 15000, 'image': 'https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg'},
        {'title': 'Traditional Kabba Outfit', 'description': 'Complete kabba set for women. High quality African fabric with beautiful patterns.', 'price': 25000, 'image': 'https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg'},
        {'title': 'Men African Shirt', 'description': 'Stylish African print shirt for men. Available in multiple sizes.', 'price': 12000, 'image': 'https://images.pexels.com/photos/1040945/pexels-photo-1040945.jpeg'},
        {'title': 'Kaba Ngondo Women', 'description': 'Elegant kaba for traditional events. Matching headwrap included.', 'price': 35000, 'image': 'https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg'},
        {'title': 'Wrapper African Print 6 Yards', 'description': 'High quality African wrapper fabric. Perfect for tailoring custom outfits.', 'price': 8500, 'image': 'https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg'},
        {'title': 'Dashiki Shirt Men', 'description': 'Colorful dashiki shirt with traditional embroidery. Comfortable cotton fabric.', 'price': 10000, 'image': 'https://images.pexels.com/photos/1040945/pexels-photo-1040945.jpeg'},
        {'title': 'Men Sneakers White', 'description': 'Comfortable casual sneakers. Perfect for everyday wear.', 'price': 18000, 'image': 'https://images.pexels.com/photos/1478442/pexels-photo-1478442.jpeg'},
        {'title': 'Women Handbag Leather', 'description': 'Stylish leather handbag with multiple compartments. Available in black and brown.', 'price': 22000, 'image': 'https://images.pexels.com/photos/1152077/pexels-photo-1152077.jpeg'},
        {'title': 'Sandals Women Flat', 'description': 'Comfortable flat sandals for daily use. Multiple color options.', 'price': 8500, 'image': 'https://images.pexels.com/photos/1440642/pexels-photo-1440642.jpeg'},
        {'title': 'Men Jeans Denim', 'description': 'Quality denim jeans in regular fit. Durable and comfortable.', 'price': 15000, 'image': 'https://images.pexels.com/photos/1598507/pexels-photo-1598507.jpeg'},
        {'title': 'T-Shirt Cotton Men', 'description': 'Plain cotton t-shirt available in multiple colors. Soft and breathable.', 'price': 3500, 'image': 'https://images.pexels.com/photos/1040945/pexels-photo-1040945.jpeg'},
        {'title': 'Women Blouse Chiffon', 'description': 'Elegant chiffon blouse for office and casual wear. Beautiful drape.', 'price': 12000, 'image': 'https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg'},
        {'title': 'Evening Dress Elegant', 'description': 'Sophisticated evening dress for special events. Available in sizes S-XL.', 'price': 28000, 'image': 'https://images.pexels.com/photos/1926769/pexels-photo-1926769.jpeg'},
    ],
    'Food & Groceries': [
        {'title': 'Rice White 50kg Bag', 'description': 'Premium long grain white rice. Clean and well sorted. Feeds the whole family.', 'price': 28000, 'image': 'https://images.pexels.com/photos/1793536/pexels-photo-1793536.jpeg'},
        {'title': 'Palm Oil 5L Jerry Can', 'description': 'Pure red palm oil from local farms. Rich in vitamins and nutrients.', 'price': 12000, 'image': 'https://images.pexels.com/photos/33783/olive-oil-salad-dressing-cooking-olive.jpg'},
        {'title': 'Plantain Fresh (per dozen)', 'description': 'Fresh ripe plantains perfect for frying or boiling. Locally sourced.', 'price': 2500, 'image': 'https://images.pexels.com/photos/5186877/pexels-photo-5186877.jpeg'},
        {'title': 'Beans White 5kg', 'description': 'Quality white beans. Clean and ready to cook. High in protein.', 'price': 6500, 'image': 'https://images.pexels.com/photos/1556674/pexels-photo-1556674.jpeg'},
        {'title': 'Smoked Fish Mackerel', 'description': 'Well-smoked mackerel fish. Perfect for traditional dishes.', 'price': 4500, 'image': 'https://images.pexels.com/photos/725997/pexels-photo-725997.jpeg'},
        {'title': 'Groundnuts Roasted 1kg', 'description': 'Freshly roasted groundnuts. Crunchy and delicious snack.', 'price': 2000, 'image': 'https://images.pexels.com/photos/1295572/pexels-photo-1295572.jpeg'},
        {'title': 'Tomato Paste 70g Can', 'description': 'Concentrated tomato paste for cooking. Pack of 12 cans.', 'price': 3500, 'image': 'https://images.pexels.com/photos/1327838/pexels-photo-1327838.jpeg'},
        {'title': 'Maggi Cubes Box 100 cubes', 'description': 'Classic Maggi seasoning cubes. Essential for every kitchen.', 'price': 4000, 'image': 'https://images.pexels.com/photos/4198936/pexels-photo-4198936.jpeg'},
        {'title': 'Garri White 5kg', 'description': 'Quality cassava garri. Perfect for eba or soaking.', 'price': 3500, 'image': 'https://images.pexels.com/photos/1793536/pexels-photo-1793536.jpeg'},
        {'title': 'Onions 5kg Bag', 'description': 'Fresh big onions. Essential ingredient for cooking.', 'price': 4500, 'image': 'https://images.pexels.com/photos/144241/pexels-photo-144241.jpeg'},
        {'title': 'Vegetable Oil 5L', 'description': 'Pure vegetable cooking oil. Cholesterol free and healthy.', 'price': 9500, 'image': 'https://images.pexels.com/photos/33783/olive-oil-salad-dressing-cooking-olive.jpg'},
        {'title': 'Sugar White 2kg', 'description': 'Refined white sugar. Perfect for sweetening tea and baking.', 'price': 2500, 'image': 'https://images.pexels.com/photos/1495324/pexels-photo-1495324.jpeg'},
        {'title': 'Fresh Eggs Tray 30', 'description': 'Farm fresh eggs from free-range chickens. Rich and nutritious.', 'price': 3500, 'image': 'https://images.pexels.com/photos/162712/eggs-food-easter-egg-162712.jpeg'},
        {'title': 'Honey Pure 1L', 'description': 'Natural honey from local beekeepers. Sweet and pure.', 'price': 8500, 'image': 'https://images.pexels.com/photos/45863/honey-beekeeper-bee-keepers-45863.jpeg'},
    ],
    'Beauty & Cosmetics': [
        {'title': 'Shea Butter Pure 500g', 'description': 'Unrefined organic shea butter from Northern Cameroon. Perfect for skin and hair.', 'price': 4500, 'image': 'https://images.pexels.com/photos/4465124/pexels-photo-4465124.jpeg'},
        {'title': 'African Black Soap Bar', 'description': 'Traditional African black soap. Natural and gentle cleansing.', 'price': 2500, 'image': 'https://images.pexels.com/photos/4202450/pexels-photo-4202450.jpeg'},
        {'title': 'Coconut Oil Pure 250ml', 'description': 'Virgin coconut oil for hair and skin care. Natural moisturizer.', 'price': 3500, 'image': 'https://images.pexels.com/photos/4465124/pexels-photo-4465124.jpeg'},
        {'title': 'Body Lotion Shea Butter', 'description': 'Moisturizing lotion enriched with shea butter. Keeps skin soft all day.', 'price': 6500, 'image': 'https://images.pexels.com/photos/3018843/pexels-photo-3018843.jpeg'},
        {'title': 'Hair Relaxer Kit', 'description': 'Professional hair relaxer for smooth straight hair. Complete kit included.', 'price': 8500, 'image': 'https://images.pexels.com/photos/3618606/pexels-photo-3618606.jpeg'},
        {'title': 'Braiding Hair Extensions', 'description': 'Quality synthetic hair for braiding. Available in multiple colors.', 'price': 4000, 'image': 'https://images.pexels.com/photos/3618606/pexels-photo-3618606.jpeg'},
        {'title': 'Makeup Foundation', 'description': 'Liquid foundation for African skin tones. Long-lasting coverage.', 'price': 12000, 'image': 'https://images.pexels.com/photos/2113855/pexels-photo-2113855.jpeg'},
        {'title': 'Lipstick Matte Set 6 Colors', 'description': 'Vibrant matte lipstick set. Perfect for every occasion.', 'price': 8500, 'image': 'https://images.pexels.com/photos/2113855/pexels-photo-2113855.jpeg'},
        {'title': 'Face Cream Brightening', 'description': 'Natural skin brightening cream. Safe and effective formula.', 'price': 7500, 'image': 'https://images.pexels.com/photos/3018843/pexels-photo-3018843.jpeg'},
        {'title': 'Perfume Body Spray Women', 'description': 'Long-lasting fragrance spray. Fresh and feminine scent.', 'price': 5500, 'image': 'https://images.pexels.com/photos/965989/pexels-photo-965989.jpeg'},
    ],
    'Home & Kitchen': [
        {'title': 'Gas Cooker 4 Burner', 'description': 'Stainless steel gas cooker with oven. Durable and efficient cooking.', 'price': 85000, 'image': 'https://images.pexels.com/photos/2343467/pexels-photo-2343467.jpeg'},
        {'title': 'Cooking Pot Set Aluminum', 'description': 'Set of 5 cooking pots with lids. Non-stick coating for easy cleaning.', 'price': 22000, 'image': 'https://images.pexels.com/photos/4033148/pexels-photo-4033148.jpeg'},
        {'title': 'Plastic Chairs Set of 4', 'description': 'Durable plastic chairs for indoor and outdoor use. Stackable design.', 'price': 18000, 'image': 'https://images.pexels.com/photos/1350789/pexels-photo-1350789.jpeg'},
        {'title': 'Dining Table Glass Top', 'description': 'Modern dining table with 4 chairs. Elegant glass top design.', 'price': 125000, 'image': 'https://images.pexels.com/photos/1350789/pexels-photo-1350789.jpeg'},
        {'title': 'Bed Mattress Foam 6x6', 'description': 'High density foam mattress. Comfortable and supportive sleep.', 'price': 45000, 'image': 'https://images.pexels.com/photos/1957478/pexels-photo-1957478.jpeg'},
        {'title': 'Curtains Window Pair', 'description': 'Beautiful window curtains with matching tie-backs. Multiple colors available.', 'price': 12000, 'image': 'https://images.pexels.com/photos/1444424/pexels-photo-1444424.jpeg'},
        {'title': 'Bedsheet Set Cotton', 'description': 'Soft cotton bedsheet with pillow cases. King size available.', 'price': 15000, 'image': 'https://images.pexels.com/photos/1957478/pexels-photo-1957478.jpeg'},
        {'title': 'Towel Set Bath 4 Pieces', 'description': 'Absorbent cotton towels. Soft and durable quality.', 'price': 8500, 'image': 'https://images.pexels.com/photos/6000065/pexels-photo-6000065.jpeg'},
        {'title': 'Wardrobe 3 Door Wooden', 'description': 'Spacious wooden wardrobe with mirror. Ample storage space.', 'price': 95000, 'image': 'https://images.pexels.com/photos/1350789/pexels-photo-1350789.jpeg'},
    ],
    'Local Products': [
        {'title': 'Handmade Basket Large', 'description': 'Traditional woven basket from West Cameroon. Perfect for storage or decoration.', 'price': 8500, 'image': 'https://images.pexels.com/photos/5824488/pexels-photo-5824488.jpeg'},
        {'title': 'Traditional Fabric Ndop', 'description': 'Authentic Ndop cloth from Grassfields. Rich cultural heritage.', 'price': 15000, 'image': 'https://images.pexels.com/photos/3679540/pexels-photo-3679540.jpeg'},
        {'title': 'Clay Pot Traditional', 'description': 'Handcrafted clay cooking pot. Traditional cooking experience.', 'price': 4500, 'image': 'https://images.pexels.com/photos/4107278/pexels-photo-4107278.jpeg'},
        {'title': 'Wooden Stool Carved', 'description': 'Hand-carved traditional stool. Beautiful African craftsmanship.', 'price': 12000, 'image': 'https://images.pexels.com/photos/1350789/pexels-photo-1350789.jpeg'},
        {'title': 'Calabash Decorated', 'description': 'Decorated calabash for traditional ceremonies. Unique artwork.', 'price': 6500, 'image': 'https://images.pexels.com/photos/5824488/pexels-photo-5824488.jpeg'},
        {'title': 'Leather Bag Handmade', 'description': 'Genuine leather bag made by Northern artisans. Durable and stylish.', 'price': 18000, 'image': 'https://images.pexels.com/photos/1152077/pexels-photo-1152077.jpeg'},
        {'title': 'Woven Mat Large', 'description': 'Traditional woven sleeping mat. Cool and comfortable.', 'price': 5500, 'image': 'https://images.pexels.com/photos/5824488/pexels-photo-5824488.jpeg'},
    ],
    'Construction & Home Repair': [
        {'title': 'Cement Bag 50kg', 'description': 'High quality Portland cement. Perfect for construction projects.', 'price': 6500, 'image': 'https://images.pexels.com/photos/1216589/pexels-photo-1216589.jpeg'},
        {'title': 'Paint White 4L', 'description': 'Water-based interior paint. Smooth finish and easy application.', 'price': 12000, 'image': 'https://images.pexels.com/photos/1669754/pexels-photo-1669754.jpeg'},
        {'title': 'Hammer Claw 500g', 'description': 'Durable steel hammer with wooden handle. Essential tool for construction.', 'price': 4500, 'image': 'https://images.pexels.com/photos/209274/pexels-photo-209274.jpeg'},
        {'title': 'Screwdriver Set 6 Pieces', 'description': 'Complete screwdriver set with different sizes. Magnetic tips.', 'price': 5500, 'image': 'https://images.pexels.com/photos/209274/pexels-photo-209274.jpeg'},
        {'title': 'Electric Drill 13mm', 'description': 'Powerful electric drill for home repairs. Variable speed control.', 'price': 28000, 'image': 'https://images.pexels.com/photos/209274/pexels-photo-209274.jpeg'},
        {'title': 'Measuring Tape 5m', 'description': 'Steel measuring tape with lock function. Accurate measurements.', 'price': 2500, 'image': 'https://images.pexels.com/photos/209274/pexels-photo-209274.jpeg'},
    ],
    'Auto & Moto Accessories': [
        {'title': 'Motorcycle Helmet Full Face', 'description': 'Safety helmet with face shield. DOT certified protection.', 'price': 18000, 'image': 'https://images.pexels.com/photos/163210/motorcycles-race-helmets-pilots-163210.jpeg'},
        {'title': 'Car Air Freshener', 'description': 'Long-lasting car fragrance. Multiple scent options available.', 'price': 1500, 'image': 'https://images.pexels.com/photos/164634/pexels-photo-164634.jpeg'},
        {'title': 'Engine Oil 4L', 'description': 'Synthetic motor oil for better engine performance. Suitable for all vehicles.', 'price': 12000, 'image': 'https://images.pexels.com/photos/4315570/pexels-photo-4315570.jpeg'},
        {'title': 'Motorcycle Side Mirror Pair', 'description': 'Replacement side mirrors with clear visibility. Easy installation.', 'price': 4500, 'image': 'https://images.pexels.com/photos/163210/motorcycles-race-helmets-pilots-163210.jpeg'},
        {'title': 'Car Battery 12V 75Ah', 'description': 'Long-lasting car battery with 2 years warranty. Maintenance free.', 'price': 45000, 'image': 'https://images.pexels.com/photos/4315570/pexels-photo-4315570.jpeg'},
        {'title': 'Car Floor Mats Set', 'description': 'Durable rubber floor mats. Protects car interior from dirt.', 'price': 8500, 'image': 'https://images.pexels.com/photos/164634/pexels-photo-164634.jpeg'},
    ],
    'Services': [
        {'title': 'Plumber Service Call', 'description': 'Professional plumbing repairs and installations. Available 24/7 for emergencies.', 'price': 15000, 'image': 'https://images.pexels.com/photos/834892/pexels-photo-834892.jpeg'},
        {'title': 'Electrician Service', 'description': 'Certified electrician for wiring, repairs, and installations. Safe and reliable.', 'price': 18000, 'image': 'https://images.pexels.com/photos/257736/pexels-photo-257736.jpeg'},
        {'title': 'House Cleaning Service', 'description': 'Professional deep cleaning for homes and offices. Experienced team.', 'price': 25000, 'image': 'https://images.pexels.com/photos/4107278/pexels-photo-4107278.jpeg'},
        {'title': 'Phone Screen Replacement', 'description': 'Fast screen repair for all phone models. Quality replacement parts.', 'price': 12000, 'image': 'https://images.pexels.com/photos/699122/pexels-photo-699122.jpeg'},
        {'title': 'Phone Battery Replacement', 'description': 'Original battery replacement with warranty. Quick turnaround time.', 'price': 8500, 'image': 'https://images.pexels.com/photos/699122/pexels-photo-699122.jpeg'},
    ],
}

# Generate SQL
print("Generating product data...")
vendor_names = list(vendors.keys())

sql_parts = []
count = 0
target = 520  # Generate more than 500

for vendor_name in vendor_names:
    vendor_info = vendors[vendor_name]
    category = vendor_info['category']
    location = vendor_info['location']

    if category in products_templates:
        templates = products_templates[category]
        # Each vendor gets 10-30 products
        num_products = random.randint(15, 35)

        for i in range(num_products):
            if count >= target:
                break

            # Pick a random template
            template = random.choice(templates)

            # Add some variation
            price_variation = random.uniform(0.9, 1.15)
            price = int(template['price'] * price_variation)

            stock = random.randint(5, 150)
            rating = round(random.uniform(3.8, 4.9), 1)
            reviews = random.randint(25, 350)
            featured = random.choice([True, False, False, False])  # 25% featured
            ships_intl = random.choice([True, False])
            delivery_type = random.choice(['local', 'national', 'national'])

            # Escape single quotes
            title = template['title'].replace("'", "''")
            description = template['description'].replace("'", "''")
            vendor_escaped = vendor_name.replace("'", "''")

            sql_parts.append(f"((SELECT id FROM vendors WHERE business_name = '{vendor_escaped}'), '{title}', '{description}', {price}, '{category}', {stock}, '{template['image']}', {rating}, {reviews}, '{location}', '{delivery_type}', {str(ships_intl).lower()}, {str(featured).lower()}, 'active')")
            count += 1

    if count >= target:
        break

print(f"Generated {count} products")
print(f"SQL size: ~{len(',\n'.join(sql_parts)) / 1024:.1f}KB")

# Write to file
with open('/tmp/products_data.sql', 'w') as f:
    f.write("INSERT INTO marketplace_products (vendor_id, title, description, price, category, stock, image_url, rating, reviews_count, location, delivery_type, ships_internationally, featured, status) VALUES\n")
    f.write(',\n'.join(sql_parts))
    f.write(';\n')

print("SQL written to /tmp/products_data.sql")

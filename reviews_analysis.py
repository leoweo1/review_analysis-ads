import pandas as pd

# reading the reviews file
reviews_df = pd.read_csv('Sample_Yelp_Reviews_Exam.csv')

# 4. determine the 10 users with the most number of reviews
print("4. TOP 10 USERS WITH MOST NUMBER OF REVIEWS:")
print("=" * 50)
user_review_counts = reviews_df['user_name'].value_counts().head(10)
for i, (user, count) in enumerate(user_review_counts.items(), 1):
    print(f"{i}. {user}: {count} reviews")

# 5. determine the top 10 cities with the most number of reviews
print("\n5. TOP 10 CITIES WITH MOST NUMBER OF REVIEWS:")
print("=" * 50)
city_review_counts = reviews_df['user_location'].value_counts().head(10)
for i, (city, count) in enumerate(city_review_counts.items(), 1):
    print(f"{i}. {city}: {count} reviews")

# 6. from the dataset determine the year that had the most number of reviews
print("\n6. YEAR WITH MOST NUMBER OF REVIEWS:")
print("=" * 50)

# convert date_written to datetime and extract year
reviews_df['date_written'] = pd.to_datetime(reviews_df['date_written'])
reviews_df['year'] = reviews_df['date_written'].dt.year

yearly_reviews = reviews_df['year'].value_counts().sort_index()

# find the year with most reviews
max_year = yearly_reviews.idxmax()
max_reviews = yearly_reviews.max()

print(f"Year with most reviews: {max_year} with {max_reviews} reviews")

# show all years for context
print("\nReview count by year:")
for year, count in yearly_reviews.items():
    print(f"  {year}: {count} reviews")
from imdb import IMDb
from textblob import TextBlob

# Create IMDb object
ia = IMDb()

# Search for a movie
movies = ia.search_movie('Dune')  # You can replace 'Dune' with any movie you want to search for

# Get the movie ID
movie_id = movies[0].movieID

# Get movie details
movie = ia.get_movie(movie_id)

# Print movie title and plot
print(f"Movie Title: {movie['title']}")

# Get reviews
ia.update(movie, 'reviews')

# Check if reviews are available
if 'reviews' in movie:
    reviews = movie['reviews']
    
    # Print a review and perform sentiment analysis
    if reviews:
        # Print only the first review
        review = reviews[0]
        review_content = review.get('content')
        
        print(f"Content: {review_content}\n")

        # Sentiment analysis
        analysis = TextBlob(review_content)
        sentiment = analysis.sentiment
        print(f"Sentiment Analysis:\nPolarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
    else:
        print("No reviews available.")
else:
    print("No reviews available.")
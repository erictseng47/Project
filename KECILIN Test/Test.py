from imdb import IMDb
from textblob import TextBlob

# 創建IMDb對象
ia = IMDb()

# 搜索一部電影
movies = ia.search_movie('Dune')  # 你可以替換 'Inception' 為任何你想要查詢的電影

# 獲取電影ID
movie_id = movies[0].movieID

# 獲取電影詳細信息
movie = ia.get_movie(movie_id)

# 打印電影名稱和簡介
print(f"Movie Title: {movie['title']}")

# 獲取影評
ia.update(movie, 'reviews')

# 檢查是否有影評可用
if 'reviews' in movie:
    reviews = movie['reviews']
    
    # 打印一則影評並進行情感分析
    if reviews:
        # 只打印第一則影評
        review = reviews[0]
        review_content = review.get('content')
        
        print(f"Content: {review_content}\n")

        # 情感分析
        analysis = TextBlob(review_content)
        sentiment = analysis.sentiment
        print(f"Sentiment Analysis:\nPolarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
    else:
        print("No reviews available.")
else:
    print("No reviews available.")

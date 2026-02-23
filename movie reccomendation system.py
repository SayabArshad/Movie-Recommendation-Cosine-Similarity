#import libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

data = {'movie_id': [1, 2, 3, 4, 5],
        'title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Pulp Fiction'],
        'genre': ['Action, Sci-Fi', 'Action, Sci-Fi, Thriller', 'Adventure, Drama, Sci-Fi', 'Action, Crime, Drama', 'Crime, Drama'],}

#convert data into dataframe
movies_df = pd.DataFrame(data)

#Display the dataset
print("Movies Dataset:")
print(movies_df)

# Create a TF-IDF Vectorizer to convert the genre text into vectors
tfidf = TfidfVectorizer(stop_words='english')

# Fit and transform the genre data
tfidf_matrix = tfidf.fit_transform(movies_df['genre'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get movie recommendations based on genre similarity
def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = movies_df[movies_df['title'] == title].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 3 most similar movies (excluding itself)
    sim_scores = sim_scores[1:4]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 3 most similar movies
    return movies_df['title'].iloc[movie_indices]

# Test the recommendation system
movie_title = 'Inception'
recommended_movies = get_recommendations(movie_title)
print(f"\nMovies similar to '{movie_title}':")
for movie in recommended_movies:
    print(movie)
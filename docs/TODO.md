# To-do

## Foundation (data wrangling + basic analysis)

- [x] Import IMDb dataset into Python (pandas).
- [-] Clean/prepare columns (budget, revenue, runtime, genres, release year, etc.).
- [ ] Create a correlation heatmap between IMDb score and numeric features.
- [ ] Visualize at least 3 relationships (scatter plot, box plot, line plot).

## Insights (digging deeper with visuals)

- [ ] Group by **genre** → average IMDb score per genre.
- [ ] Group by **year** → check if movies are “getting better or worse.”
- [ ] Identify directors/actors with consistently high-rated movies.
- [ ] Storytelling: write down 3 “surprising findings” you didn’t expect.

## Machine Learning (basic prediction)

- [ ] Preprocess categorical data (e.g., one-hot encode genres).
- [ ] Train a **linear regression model** to predict IMDb score.
- [ ] Train a **random forest model** and compare performance.
- [ ] Evaluate with metrics (MAE, RMSE).

## Make it cool (interactive app/dashboard)

- [ ] Build a **Streamlit/Dash app** with:
  - Movie score predictor (input features → predicted score).
  - Interactive charts (filter by year/genre).
- [ ] Deploy it online (Streamlit Cloud is free).

## Optional Stretch Goals

- Cluster movies into “hidden groups” using K-means.
- Sentiment analysis of plot summaries → correlate language with scores.
- Compare IMDb vs Rotten Tomatoes vs Metacritic scores (bias analysis).

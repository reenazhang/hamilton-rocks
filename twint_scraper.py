import twint

# Configure
c = twint.Config()
c.Username = "HamiltonMusical"
c.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Tweet: {tweet}"
c.Store_csv = True
c.Output = "tweet_file"
c.Pandas = True

# Run
twint.run.Search(c)

# Store results in a dataframe
df = twint.storage.panda.Tweets_df
df.sample(5)

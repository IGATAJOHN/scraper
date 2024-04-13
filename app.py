from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def check_retweet(authenticated_user, tweet_id):
    # Placeholder logic: Assume the user has retweeted if tweet ID is even
    return int(tweet_id) % 2 == 0

def check_following(authenticated_user, account_to_follow):
    # Placeholder logic: Assume the user is following if account name contains "follow"
    return "follow" in account_to_follow.lower()

def check_like(authenticated_user, tweet_id):
    # Placeholder logic: Assume the user has liked if tweet ID is divisible by 3
    return int(tweet_id) % 3 == 0

def has_specific_hashtag(tweet_text, target_hashtag):
    # Remove special characters and split the tweet into words
    words = re.findall(r'\w+', tweet_text.lower())
    
    # Check if the target hashtag is in the words
    return target_hashtag.lower() in words

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    authenticated_user = data.get('authenticated_user')
    tweet_id = data.get('tweet_id')
    account_to_follow = data.get('account_to_follow')
    tweet_text = data.get('tweet_text')
    target_hashtag = data.get('target_hashtag')

    retweet_result = check_retweet(authenticated_user, tweet_id)
    following_result = check_following(authenticated_user, account_to_follow)
    like_result = check_like(authenticated_user, tweet_id)
    hashtag_result = has_specific_hashtag(tweet_text, target_hashtag)

    return jsonify({
        "retweet_validation_result": retweet_result,
        "following_validation_result": following_result,
        "like_validation_result": like_result,
        "hashtag_validation_result": hashtag_result
    })

if __name__ == '__main__':
    app.run(debug=True)

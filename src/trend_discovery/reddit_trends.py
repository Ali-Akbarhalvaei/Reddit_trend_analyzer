import requests
from typing import List, Dict, Any


REDDIT_POPULAR_URL = "https://www.reddit.com/r/popular.json"

HEADERS = {"User-Agent": "InstAgentBot/0.1 by u/YourUsername"}


def get_reddit_trends(limit: int = 5) -> List[Dict[str, Any]]:
    """
    Fetches top trending posts from the r/popular subreddit.

    Args:
        limit (int): The number of top posts to fetch.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, where each dictionary
                              represents a trending post. Returns an empty
                              list if the fetch fails.
    """
    try:
        response = requests.get(
            REDDIT_POPULAR_URL, headers=HEADERS, params={"limit": limit}
        )
        # This will raise an HTTPError if the response was an error (4xx or 5xx)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Reddit: {e}")
        return []  # Return an empty list to signify failure

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    trending_posts = []
    for post in posts:
        post_data = post.get("data", {})
        # Add a check to ensure title exists
        if "title" in post_data:
            trending_posts.append(
                {
                    "title": post_data["title"],
                    "score": post_data.get("score", 0),
                    "url": post_data.get("url", ""),
                }
            )

    return trending_posts


if __name__ == "__main__":

    print("----- Reddit Trends Test -----")
    trends = get_reddit_trends(limit=3)
    if trends:
        for idx, trend in enumerate(trends, 1):
            print(f"{idx}. {trend['title']} (Score: {trend['score']})")
    else:
        print("Failed to fetch trends from Reddit.")
    print("----------------------------")

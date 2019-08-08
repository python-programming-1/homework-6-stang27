import csv
import pprint


def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    vid_data = []
    with open('USvideos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)


def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    # Create an empty dictionary that will take the channel and the views
    channels_and_views = {}
    # Iterate through the loop and sum the views for the same channel name
    for video in data[1:]:
    	# Set the default for the views dictionary
    	channels_and_views.setdefault(video['channel_title'], 0)
    	channels_and_views[video['channel_title']] += int(video['views'])
    
    # Create the return dictionary
    most_popular_and_least_popular_channel = {'most_popular_channel': None, 'least_popular_channel': None, 'most_pop_num_views': 0,
                                              'least_pop_num_views': float('Inf')}
    # Analyze the view dictionary for the most popular channel
    for k,v in channels_and_views.items():
    	if int(v) > most_popular_and_least_popular_channel['most_pop_num_views']:
    		most_popular_and_least_popular_channel['most_popular_channel'] = k
    		most_popular_and_least_popular_channel['most_pop_num_views'] = int(v)
    # Analyze the view dictionary for the least popular channel
    for k,v in channels_and_views.items():
    	if k == 'Unspecified':
    		continue
    	if int(v) < most_popular_and_least_popular_channel['least_pop_num_views']:
    		most_popular_and_least_popular_channel['least_popular_channel'] = k
    		most_popular_and_least_popular_channel['least_pop_num_views'] = v
    # Return dictionary
    return most_popular_and_least_popular_channel


def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    # Create 2 dictionarys: 1 for likes, 1 for dislikes
    channels_and_likes = {}
    channels_and_dislikes = {}
    # Iterate through the loop and sum the likes and sum the dislikes
    for video in data[1:]:
    	# Set the default for the likes and dislikes
    	channels_and_likes.setdefault(video['channel_title'], 0)
    	channels_and_dislikes.setdefault(video['channel_title'], 0)
    	channels_and_likes[video['channel_title']] += int(video['likes'])
    	channels_and_dislikes[video['channel_title']] += int(video['dislikes'])
    # Create the return dictionary
    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': 0, 'most_disliked_channel': None, 'num_dislikes': 0}
    #Analyze the likes dictionary for the most likes
    for k,v in channels_and_likes.items():
    	if int(v) > most_liked_and_disliked_channel['num_likes']:
    		most_liked_and_disliked_channel['most_liked_channel'] = k
    		most_liked_and_disliked_channel['num_likes'] = int(v)
    # Analyze the dislikes dictionary for the most dislikes
    for k,v in channels_and_dislikes.items():
    	if int(v) > most_liked_and_disliked_channel['num_dislikes']:
    		most_liked_and_disliked_channel['most_disliked_channel'] = k
    		most_liked_and_disliked_channel['num_dislikes'] = int(v)
    # Return dictionary
    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()

    # uncomment the line below to see what the data looks like
    # print_data(vid_data)
    
    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)
    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)
    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))

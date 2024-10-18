import vk_api
import json
import argparse
import os

def get_user_info(vk, user_id):
    user = vk.users.get(user_ids=user_id, fields="followers_count")
    followers = vk.users.getFollowers(user_id=user_id)['items']
    subscriptions = vk.users.getSubscriptions(user_id=user_id)['groups']['items']
    return {
        'user': user[0],
        'followers': followers,
        'subscriptions': subscriptions
    }

def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main(token, user_id, result_path):
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    data = get_user_info(vk, user_id)

    save_to_json(data, result_path)
    print(f"Данные сохранены в {result_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VK user data collector")
    parser.add_argument('--token', type=str, help="VK API Access Token", required=True)
    parser.add_argument('--user_id', type=str, help="VK user ID", default=None)
    parser.add_argument('--result_path', type=str, help="Path to save the result JSON file", default="result.json")
    args = parser.parse_args()

    user_id = args.user_id if args.user_id else '462027867'
    result_path = args.result_path

    main(args.token, user_id, result_path)






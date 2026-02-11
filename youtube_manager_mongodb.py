from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId
from pymongo.errors import PyMongoError

# MongoDB Collection
try:
    client = MongoClient("mongodb+srv://<username>:<password>@cluster0.knbctv0.mongodb.net/")
    db = client["ytmanager"]
    video_collection = db["videos"]
    print("Connected to MongoDB Successfully")
except PyMongoError as e:
    print("Database connection failed: ", e)
    exit()

def add_video(name, time):
    try:
        video_collection.insert_one({"name": name, "time": time})
        print("Video added successfully")
    except PyMongoError as e:
        print("Error adding video: ", e)

def list_videos():
    try:
        videos = video_collection.find()
        found = False
        for video in videos:
            found = True
            print(f"ID: {video['_id']}, Name: {video.get['name']} and Time: {video.get['time']}")
        if not found:
            print("No videos found")
    except PyMongoError as e:
        print("Error fetching videos: ",e)

def update_video(video_id, new_name, new_time):
    try:
        result = video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name,"time": new_time}}
        )
        if result.matched_count == 0:
            print("No video found with this ID")
        else:
            print("Video updated successfully")
    except InvalidId:
        print("Invalid video ID format")
    except PyMongoError as e:
        print("Error updating video: ", e)


def delete_video(video_id):
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count == 0:
            print("No video found with this ID")
        else:
            print("Video deleted successfully")
    except InvalidId:
        print("Invalid video Id format")
    except PyMongoError as e:
        print("Error deleting video: ", e)

def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                list_videos()

            elif choice == '2':
                name = input("Enter the video name: ").strip()
                time = input("Enter the video time: ").strip()

                if not name or not time:
                    print("Name and time cannot be empty")
                else:
                    add_video(name, time)

            elif choice == '3':
                video_id = input("Enter the video id to update: ")
                name = input("Enter the updated video name: ")
                time = input("Enter the updated video time: ")
                update_video(video_id, name, time)

            elif choice == '4':
                video_id = input("Enter the video id to delete: ")
                delete_video(video_id)

            elif choice == '5':
                print("Exiting app...")
                break

            else:
                print("Invalid Choice")
        except Exception as e:
            print("Unexpected error occurred: ", e)

if __name__ == "__main__":

    main()

import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            #print(type(test))
            return test
    except FileNotFoundError:
        return [1,2]  # Default data if file not found


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file, indent=4)


def list_all_videos(videos):
    print("\n")
    print("*" * 90)
    for index ,video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 90)

def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1 <= index < len(videos):
        name = input("Enter the new name of the video: ")
        time = input("Enter the new time of the video: ")
        videos[index-1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index.")

def main():
    videos = load_data()
    while True:
        print("Welcome to the YouTube Manager!\n")
        print("1. list all youtube video")
        print("2. Upload Video")
        print("3. Update Video ")
        print("4. Delete a Video Details")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice. Please try again.")  
    
if __name__ == "__main__":
    main() 
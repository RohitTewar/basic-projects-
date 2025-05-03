import sqlite3
# This is a simple Youtube video manager app with SQLite database

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor() # Create a cursor object to execute SQL commands

cursor.execute('''    
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


#Cursor.execute() method is used to execute SQL commands
# The CREATE TABLE statement creates a new table in the database if it does not already exist.

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video( name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit() #commit the changes to the database

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,)) #always use tuple for single value (,) like ('video_id',) it treated like tuple
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)

        elif choice == '3':
            video_id = int(input("Enter video id to Update: "))
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id,name, time)

        elif choice == '4':
            video_id = int(input("Enter video id to delete: "))
            delete_video(video_id)

        elif choice == '5':
            break
        else:  
            print("Invalid choice. Please try again.")

    conn.close() # Close the database connection when done

if __name__ == '__main__':     # This is the main entry point of the program
                               #If this file is run directly, the main() function will be executed
    main()
import sqlite3

conn = sqlite3.connect('YoutubeVideos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL               
    )
''')

def ListVideos():
    cursor.execute("Select * from videos")

    for row in cursor.fetchall():
        print(row)

def addVideo(name, time):
    cursor.execute("Insert into videos (name, time) values (?,?)", (name, time))
    conn.commit()


def updateVideo(videoID,newName, newTime):
    cursor.execute("Update videos set name = ?, time = ? Where id = ?", (newName ,newTime, videoID))
    conn.commit()
    

def deleteVideo(videoID):
    cursor.execute("Delete from videos where id = ?",(videoID,))
    conn.commit()



def main():
    while True:
        print("\nYoutube Manager app with db")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")

        choice = input("Enter your choice: ")

        if choice == '1':
            ListVideos()
        elif choice == '2':
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            addVideo(name, time)
        elif choice == '3':
            videoID = input("Enter Video ID to update : ")
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            updateVideo(videoID, name, time)
        elif choice == '4':
            videoID = input("Enter Video ID to delete : ")

            deleteVideo(videoID)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()

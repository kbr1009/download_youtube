from pytube import YouTube


def input_info():
    print("YouTubeのurlを入力")
    url = input("→")
    print("指定したいタイトルを入力")
    title = input("→")
    video = title + ".mp4"
    if url == "":
        print("YouTubeのurlを入力")
        return input_info()
    else:
        return url, video, title

def main():
    try:
        info = input_info()
        yt = YouTube(info[0])
        print(yt.title)
        print(yt.thumbnail_url)
        print(info[1])
        stream = yt.streams.get_highest_resolution()
        if info[2] == "":
            stream.download('/Users/reokobayashi/downloadyoutube/videos')
        else:
            stream.download('/Users/reokobayashi/downloadyoutube/videos', info[1])
    except:
        print("urlが無効!")
        main()

if __name__=="__main__":
    main()

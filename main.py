from pytube import YouTube


def input_info():
    print("urlを入力")
    url = input("→")
    
    print("タイトルを入力")
    title = input("→")
    video = title + ".mp4"
    if url == "":
        print("urlを入力してくだい")
        return input_info()
    else:
        return url, video, title

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

except ArithmeticError as e:
    print(e)
    print(type(e))

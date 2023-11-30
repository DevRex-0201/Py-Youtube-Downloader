from pytube import YouTube

def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        video.download(output_path)
        print(f"Download complete: {yt.title}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

if __name__ == "__main__":
    video_urls = [
        "https://www.youtube.com/embed/ckxhh6-HZ8g?rel=0&autoplay=0", "https://www.youtube.com/embed/hq-gMoyPbHA?rel=0&autoplay=0", "https://www.youtube.com/embed/Kkx95AnHIAs?rel=0&autoplay=0", "https://www.youtube.com/embed/4m-vZxoABD8?rel=0&autoplay=0", "https://www.youtube.com/embed/Sj64akxB_tg?rel=0&autoplay=0", "https://www.youtube.com/embed/cMMYeoCI6BY?rel=0&autoplay=0", "https://www.youtube.com/embed/m6_IHv8hdKY?rel=0&autoplay=0", "https://www.youtube.com/embed/j0cqGrg8PCM?rel=0&autoplay=0", "https://www.youtube.com/embed/d2awkQ7-uZY?rel=0&autoplay=0", "https://www.youtube.com/embed/83eghS5XxEM?feature=oembed", "https://www.youtube.com/embed/D_Y-wdAqjDg?rel=0&autoplay=0", "https://www.youtube.com/embed/Tzo6kqzHVlE?rel=0&autoplay=0", "https://www.youtube.com/embed/Talc4NYDMvk?rel=0&autoplay=0", "https://www.youtube.com/embed/MOlcwW5gXkk?rel=0&autoplay=0", "https://www.youtube.com/embed/h5xhqUu69aE?rel=0&autoplay=0", "https://www.youtube.com/embed/jOYvznMn400?rel=0&autoplay=0", "https://www.youtube.com/embed/83eghS5XxEM?feature=oembed", "https://www.youtube.com/embed/D_Y-wdAqjDg?rel=0&autoplay=0", "https://www.youtube.com/embed/Tzo6kqzHVlE?rel=0&autoplay=0", "https://www.youtube.com/embed/Talc4NYDMvk?rel=0&autoplay=0", "https://www.youtube.com/embed/MOlcwW5gXkk?rel=0&autoplay=0", "https://www.youtube.com/embed/h5xhqUu69aE?rel=0&autoplay=0", "https://www.youtube.com/embed/jOYvznMn400?rel=0&autoplay=0", "https://www.youtube.com/embed/MvR-7rknNzo?rel=0&autoplay=0", "https://www.youtube.com/embed/CckSuhOfRrI?rel=0&autoplay=0", "https://www.youtube.com/embed/0UcCyZtVFFc?rel=0&autoplay=0", "https://www.youtube.com/embed/8KPCiXDfSY8?rel=0&autoplay=0", "https://www.youtube.com/embed/eUiSCEBGxXk?rel=0&autoplay=0", "https://www.youtube.com/embed/Sj64akxB_tg?rel=0&autoplay=0", "https://www.youtube.com/embed/cMMYeoCI6BY?rel=0&autoplay=0", "https://www.youtube.com/embed/m6_IHv8hdKY?rel=0&autoplay=0", "https://www.youtube.com/embed/j0cqGrg8PCM?rel=0&autoplay=0", "https://www.youtube.com/embed/d2awkQ7-uZY?rel=0&autoplay=0", "https://www.youtube.com/embed/PxHj77Eb-0k?rel=0&autoplay=0", "https://www.youtube.com/embed/zjUdtK6ukqY?rel=0&autoplay=0", "https://www.youtube.com/embed/da1vvigy5tQ?rel=0&autoplay=0", "https://www.youtube.com/embed/9CXd1f1Ss3M?rel=0&autoplay=0", "https://www.youtube.com/embed/FCmqQg6saQ0?rel=0&autoplay=0", "https://www.youtube.com/embed/_iMYimEQ0zc?rel=0&autoplay=0", "https://www.youtube.com/embed/2rkp3N1bmDU?rel=0&autoplay=0", "https://www.youtube.com/embed/TpeK9uJNN7c?rel=0&autoplay=0", "https://www.youtube.com/embed/7bqJhQNAoP0?rel=0&autoplay=0", "https://www.youtube.com/embed/EqKNfyUPzoU?rel=0&autoplay=0", "https://www.youtube.com/embed/CHR8AJKxlZ4?rel=0&autoplay=0", "https://www.youtube.com/embed/aPpcBMwLg2Q?rel=0&autoplay=0", "https://www.youtube.com/embed/Fo-80yaEYG0?rel=0&autoplay=0", "https://www.youtube.com/embed/D-tz-989wiQ?rel=0&autoplay=0", "https://www.youtube.com/embed/1bHr6rfk_ag?rel=0&autoplay=0", "https://www.youtube.com/embed/DJlckOM7lbI?rel=0&autoplay=0", "https://www.youtube.com/embed/60ZsHvoQ06I?rel=0&autoplay=0", "https://www.youtube.com/embed/V-gBgfKVIgY?rel=0&autoplay=0"
    ]

    output_directory = "output"  # Replace with your desired output directory

    for video_url in video_urls:
        download_video(video_url, output_directory)

# YouTube Video Downloader

## Overview

This Python script allows you to download YouTube videos using the `pytube` library. Simply provide a list of YouTube video URLs, and the script will download the videos in the highest resolution available. The downloaded videos will be saved to a specified output directory.

## Video Preview

[![Video Preview](https://github.com/DevRex-0201/Project-Images/blob/main/video%20preview/Py-Youtube-Downloader.png)](https://drive.google.com/file/d/1ztljYdrFuyDd719e1CdsK2Rp_9prfKuF/view?usp=drive_link)

## Features

- Download YouTube videos in the highest resolution.
- Simple and easy-to-use script.
- Supports batch downloading of multiple videos.

## Prerequisites

Make sure you have Python installed on your system. You can install the required library using the following command:

```bash
pip install pytube
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/youtube-video-downloader.git
   ```

2. Navigate to the project directory:

   ```bash
   cd youtube-video-downloader
   ```

3. Open the `download_videos.py` file and update the `video_urls` list with the YouTube URLs you want to download.

4. Run the script:

   ```bash
   python download_videos.py
   ```

   By default, the downloaded videos will be saved in the "output" directory. You can change the output directory by modifying the `output_directory` variable in the script.

## Example

```python
# Example video URLs
video_urls = [
    "https://www.youtube.com/watch?v=example1",
    "https://www.youtube.com/watch?v=example2",
    "https://www.youtube.com/watch?v=example3",
]

# Output directory
output_directory = "output"

# Download videos
for video_url in video_urls:
    download_video(video_url, output_directory)
```

## Note

- Ensure that you have the necessary permissions to download and use YouTube videos.
- The script uses the `pytube` library, which may be subject to changes in the future. Check for updates or modifications to the library if issues arise.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pytube](https://github.com/nficano/pytube) - A lightweight, dependency-free Python library for downloading YouTube videos.

Feel free to contribute to the project by opening issues or submitting pull requests. Enjoy downloading your favorite YouTube videos hassle-free!

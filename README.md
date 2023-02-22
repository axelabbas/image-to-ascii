# **Video to ASCII Converter** 
A python tool that allows you to convert a video into an ASCII version of the same video. The output of the program is an mp4 video.
# **Requirements** 
- Pillow
- OpenCV
- NumPy

# **Installation**
- Clone this repository to your local machine.
- Install the required packages using pip install -r requirements.txt.
- Run the program using python video_to_ascii.py.

# **Usage**
The program takes two arguments: the path to the input video file and the path to the output file. By default, the output file is a text file with the same name as the input video file but with a .txt extension.


# **How it works**
The program works by reading each frame of the input video and converting it into a grayscale image. The grayscale image is then resized to a smaller size to reduce the number of characters in the output text. Each pixel in the resized image is then converted into an ASCII character based on its brightness value. Finally, the ASCII characters are concatenated into a single string and written to the output file.

# **Example**
Here is an example of what the result might look like:

**Input**

<video src="https://user-images.githubusercontent.com/62534624/220768339-547e3e0a-40c3-4798-a1b7-5e0ad2e1e0fb.mp4" controls="controls" style="max-width: 730px;">
</video>

**Output**

<video src="https://user-images.githubusercontent.com/62534624/220768605-e2a36259-2c10-4dc1-8c0f-d09a2612a60e.mp4
" controls="controls" style="max-width: 730px;">
</video>


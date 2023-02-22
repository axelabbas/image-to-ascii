# **Video to ASCII Converter** 
A python tool that allows you to convert a video into an ASCII version of the same video. The output of the program is an mp4 format video.
# **Requirements** 
- Pillow
- OpenCV
- NumPy

# **Installation**
- Clone this repository to your local machine.
- Install the required packages using pip install -r requirements.txt.
- Run the program using 
```python videToAscii.py```.

# **Usage**
First save your input video in the inputs folder, After that run the python code, you'll be asked to enter the input video's name, enter the video name only (***Not inputs/filename***), After that enter the desired output file name, After letting the program run, the ascii video will be saved at ***outputs/{filename}***.

***this assumes you're not looking to customize your output***

# **Customize**
Allows you to customize the output video's text color and background color.
After getting asked if you want to customize the output, enter Y, you'll be asked to enter a BG color (input is color name only. i.e: white), and then the text's color (input is the color's rgb values i.e: 255,255,255)

# **How it works**
The program works by reading each frame of the input video and converting it into a grayscale image. The grayscale image is then resized to a smaller size. Each pixel in the resized frame is then converted into an ASCII character based on its brightness value. Finally, the ASCII characters are concatenated into a single string, after that each character in the string are written onto a new frame, Making it an ascii version of the original frame, and last all frames are added up to make a new video.

# **Example**
Here is an example of what the result might look like:

**Input**

<video src="https://user-images.githubusercontent.com/62534624/220768339-547e3e0a-40c3-4798-a1b7-5e0ad2e1e0fb.mp4" controls="controls" style="max-width: 730px;">
</video>

**Output**

<video src="https://user-images.githubusercontent.com/62534624/220768605-e2a36259-2c10-4dc1-8c0f-d09a2612a60e.mp4
" controls="controls" style="max-width: 730px;">
</video>


import html
from IPython.display import display, Javascript, Image
#from google.colab.output import eval_js

def preProcessVideo():
  js = Javascript('''
    const video = document.createElement('video');
    const labelElement = document.createElement('span');
    const videoUrl = 'https://drive.google.com/file/d/1fGMLac9kQayel_CyrZaztC2lnZqIZ8MB/view?usp=sharing'

    async function playVideo() {
      const div = document.createElement('div');

      video.style.width = 320;
      video.style.height = 320;

      document.body.appendChild(div);
      div.appendChild(labelElement);
      div.appendChild(video);
      
      var source = document.createElement('source');

      source.setAttribute('src', videoUrl);
      source.setAttribute('type', 'video/mp4');
      video.appendChild(source);
      video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);
    }
    ''')
  display(js)
  #eval_js('playVideo()'.format())

preProcessVideo()


import numpy as np
import cv2

# Open a sample video available in sample-videos
vcap = cv2.VideoCapture('https://drive.google.com/file/d/1fGMLac9kQayel_CyrZaztC2lnZqIZ8MB/view?usp=sharing')
#if not vcap.isOpened():
#    print "File Cannot be Opened"

while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    if frame is not None:
        # Display the resulting frame
        cv2.imshow('frame',frame)
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Video stop")

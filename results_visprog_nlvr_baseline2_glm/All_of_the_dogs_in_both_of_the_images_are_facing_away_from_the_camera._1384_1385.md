Question: All of the dogs in both of the images are facing away from the camera.

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/03/6a/49/d2/barking-brook-sled-dog.jpg

Right image URL: http://www.jokkmokkguiderna.com/wp-content/uploads/2017/05/Huskytour_swedish_lapland_2017-huvudbild-1.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'All of the dogs in both of the images are facing away from the camera.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the dogs in both of the images are facing away from the camera.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


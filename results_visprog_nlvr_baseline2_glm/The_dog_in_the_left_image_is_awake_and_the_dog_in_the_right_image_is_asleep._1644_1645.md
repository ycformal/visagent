Question: The dog in the left image is awake and the dog in the right image is asleep.

Reference Answer: False

Left image URL: http://i1176.photobucket.com/albums/x322/Jensen8278/39d270e8.jpg

Right image URL: https://i.pinimg.com/736x/61/7a/7d/617a7d7f5ab8cdad2a01a77ddd0a0d17--dog-sleeping-doberman-pinscher.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The dog in the left image is awake and the dog in the right image is asleep.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The dog in the left image is awake and the dog in the right image is asleep.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


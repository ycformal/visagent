Question: No guinea pig is one solid color, and the right image contains twice as many guinea pigs as the left image.

Reference Answer: True

Left image URL: http://www.cottontails-rescue.org.uk/wp-content/uploads/2013/03/Bubble-and-Squeak-4-11.11.13-edited.jpg

Right image URL: https://www.omlet.co.uk/images/originals/Guinea-pigs-eating-together.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'No guinea pig is one solid color, and the right image contains twice as many guinea pigs as the left image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'No guinea pig is one solid color, and the right image contains twice as many guinea pigs as the left image.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


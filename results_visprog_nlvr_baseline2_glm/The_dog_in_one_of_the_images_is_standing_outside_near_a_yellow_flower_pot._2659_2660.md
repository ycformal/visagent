Question: The dog in one of the images is standing outside near a yellow flower pot.

Reference Answer: False

Left image URL: http://zwergschnauzer-vom-schwarzen-ort.de/Bilder/huendinnen/3.jpg

Right image URL: https://s3-us-west-1.amazonaws.com/niusnews-imgs/210089_4.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The dog in one of the images is standing outside near a yellow flower pot.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The dog in one of the images is standing outside near a yellow flower pot.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


Question: Both basins are sitting on a counter.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/0d/39/0a/32/wash-basin-the-fridge.jpg

Right image URL: http://www.shirecruisers.co.uk/narrowboat/images/CO10.JPG

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
ANSWER0=VQA(image=IMAGE,question="Is 'Both basins are sitting on a counter.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both basins are sitting on a counter.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


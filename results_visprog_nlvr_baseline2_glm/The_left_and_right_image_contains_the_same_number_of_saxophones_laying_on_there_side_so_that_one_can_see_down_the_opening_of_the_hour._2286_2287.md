Question: The left and right image contains the same number of saxophones laying on there side so that one can see down the opening of the hour.

Reference Answer: True

Left image URL: https://cdn.shopify.com/s/files/1/0870/1056/products/yamaha_yas-23_alto_saxophone_222891n_1024x1024.jpg?v=1473701735

Right image URL: http://news.p-mom.net/wp-content/uploads/2016/11/saxophone-546303_640.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number of saxophones laying on there side so that one can see down the opening of the hour.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number of saxophones laying on there side so that one can see down the opening of the hour.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


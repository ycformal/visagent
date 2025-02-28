Question: One image shows three side-by-side gray-and-white husky puppies in upright sitting poses, and all dogs in both images are puppies.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/68/0d/92/680d92f7813ff87e3ce4bb8b251a992d.jpg

Right image URL: https://i.pinimg.com/736x/42/6a/23/426a23f64dc87a7180c992c13e2733a2--three-year-olds-malamute.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows three side-by-side gray-and-white husky puppies in upright sitting poses, and all dogs in both images are puppies.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows three side-by-side gray-and-white husky puppies in upright sitting poses, and all dogs in both images are puppies.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


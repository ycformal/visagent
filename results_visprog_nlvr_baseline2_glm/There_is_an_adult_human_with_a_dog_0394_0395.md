Question: There is an adult human with a dog

Reference Answer: True

Left image URL: http://www.city-data.com/forum/attachments/dogs/94952d1336347669-leonberger-pup-dscn4655.jpg

Right image URL: https://i.pinimg.com/236x/db/cf/ee/dbcfeee496f4ca023c7b3132bcc30569--huge-dogs-giant-dogs.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is an adult human with a dog' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is an adult human with a dog' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


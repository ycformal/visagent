Question: All images show dogs in snowy scenes, and one image includes a florward-facing dog with a face-full of snow.

Reference Answer: False

Left image URL: http://1.bp.blogspot.com/-evRGi--48dU/T4F5CB5WYjI/AAAAAAAAFEM/OHJkbuHMRXo/s640/026.JPG

Right image URL: https://asgardkennel.files.wordpress.com/2011/02/boudica-snow-jan-2011a1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All images show dogs in snowy scenes, and one image includes a florward-facing dog with a face-full of snow.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All images show dogs in snowy scenes, and one image includes a florward-facing dog with a face-full of snow.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


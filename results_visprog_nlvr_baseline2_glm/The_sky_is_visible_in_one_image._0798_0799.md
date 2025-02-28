Question: The sky is visible in one image.

Reference Answer: True

Left image URL: https://natureworldadventures.files.wordpress.com/2013/07/african-zebras-20.jpg

Right image URL: https://mpnforum.files.wordpress.com/2013/12/zebra-handsome-single.png

Original program:

```
Statement: The sky is visible in one image.
Program:
ANSWER0=VQA(image=LEFT,question='Is the sky visible in the image?')
ANSWER1=VQA(image=RIGHT,question='Is the sky visible in the image?')
ANSWER2=EVAL(expr='{ANSWER0} xor {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The sky is visible in one image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The sky is visible in one image.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


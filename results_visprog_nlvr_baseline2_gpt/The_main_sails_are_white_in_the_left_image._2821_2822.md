Question: The main sails are white in the left image.

Reference Answer: False

Left image URL: https://www.coastandcountry.co.uk/wp-content/uploads/2013/08/Sailing-on-Salcombe-harbour-690.jpg

Right image URL: https://boxstuff-development-thumbnails.s3.amazonaws.com/521453_1024x400f.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='What color are the main sails?')
ANSWER1=EVAL(expr='{ANSWER0} == white')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The main sails are white in the left image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The main sails are white in the left image.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


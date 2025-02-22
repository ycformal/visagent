Question: The left image contains no more than one rodent.

Reference Answer: True

Left image URL: http://www.cottontails-rescue.org.uk/wp-content/uploads/2013/03/Bubble-and-Squeak-4-11.11.13-edited.jpg

Right image URL: https://www.omlet.co.uk/images/originals/Guinea-pigs-eating-together.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many rodents are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many rodents are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many rodents are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 <= 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 <= 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True


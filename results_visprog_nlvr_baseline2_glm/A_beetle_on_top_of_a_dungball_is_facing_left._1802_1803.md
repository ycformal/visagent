Question: A beetle on top of a dungball is facing left.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2012/02/01/article-2094950-118D0563000005DC-77_468x359.jpg

Right image URL: https://i.pinimg.com/736x/e4/50/99/e45099a2cd7fc308236bc42a104a4d85--drawing-challenge-beetles.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A beetle on top of a dungball is facing left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A beetle on top of a dungball is facing left.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


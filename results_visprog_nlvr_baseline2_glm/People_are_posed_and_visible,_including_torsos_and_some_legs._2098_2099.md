Question: People are posed and visible, including torsos and some legs.

Reference Answer: True

Left image URL: http://i64.photobucket.com/albums/h164/ybfchic/March%202016%20Part%203/zoebar2.jpg

Right image URL: http://i64.photobucket.com/albums/h164/ybfchic/March%202016%20Part%203/TBS1.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'People are posed and visible, including torsos and some legs.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'People are posed and visible, including torsos and some legs.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


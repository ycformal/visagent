Question: The dog on the left is standing in the snow.

Reference Answer: False

Left image URL: http://4.bp.blogspot.com/-HHD98kGGB7o/Uju1gUdVWFI/AAAAAAAAKdw/v0bWbTCFRgU/s1600/Bethany4.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/23/d4/e4/23d4e4150615dbb995656390e3fe7b47.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The dog on the left is standing in the snow.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The dog on the left is standing in the snow.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


Question: One of the dogs is all black, and the other one is not all white.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/mwt1PwJpXK8/hqdefault.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/53/cc/15/53cc15be04578f699f6765f796c3185e.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One of the dogs is all black, and the other one is not all white.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the dogs is all black, and the other one is not all white.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


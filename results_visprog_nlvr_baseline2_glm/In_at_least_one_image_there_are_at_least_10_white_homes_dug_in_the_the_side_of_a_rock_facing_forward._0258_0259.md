Question: In at least one image there are at least 10 white homes dug in the the side of a rock facing forward.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/p53mYPIIQsg/hqdefault.jpg

Right image URL: https://farm5.static.flickr.com/4084/4989714982_8f51b56b72.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there are at least 10 white homes dug in the the side of a rock facing forward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there are at least 10 white homes dug in the the side of a rock facing forward.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


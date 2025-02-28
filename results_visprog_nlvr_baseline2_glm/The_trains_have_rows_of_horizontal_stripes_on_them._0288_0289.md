Question: The trains have rows of horizontal stripes on them.

Reference Answer: False

Left image URL: http://farm3.static.flickr.com/2620/5719990915_89781e8781.jpg

Right image URL: http://www.trainboard.com/railimages/data/1261/celaya21.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The trains have rows of horizontal stripes on them.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The trains have rows of horizontal stripes on them.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


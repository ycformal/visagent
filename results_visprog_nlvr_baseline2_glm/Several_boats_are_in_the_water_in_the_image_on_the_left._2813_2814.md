Question: Several boats are in the water in the image on the left.

Reference Answer: True

Left image URL: http://www.loveachill.com/images/achillinfo/standard/Sport/achill-yawl.jpg

Right image URL: http://www.advertiser.ie/images/2008/08/859.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Several boats are in the water in the image on the left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Several boats are in the water in the image on the left.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


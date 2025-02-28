Question: There are two guinea pigs standing neat to each-other in the image on the left.

Reference Answer: True

Left image URL: https://leesburgvetblog.files.wordpress.com/2014/02/guinea-pigs_vanetta-and-sully.jpg?w=640&h=427&crop=1

Right image URL: https://farm4.staticflickr.com/3257/2864103965_051cc6d855.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are two guinea pigs standing neat to each-other in the image on the left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two guinea pigs standing neat to each-other in the image on the left.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


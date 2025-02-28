Question: There are a total of two school buses.

Reference Answer: False

Left image URL: http://s3.amazonaws.com/edscoop-media/uploads/_articlesCenterImages/14277041232_3a62d1a148_z.jpg?mtime=20160629121406

Right image URL: https://bloximages.chicago2.vip.townnews.com/cnhinews.com/content/tncms/assets/v3/editorial/e/ab/eab863ac-9cdd-11e4-855b-d3d172852be7/54b7fc16bca5e.image.jpg?resize=1200%2C799

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are a total of two school buses.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are a total of two school buses.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


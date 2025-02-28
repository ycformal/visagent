Question: In at least one image there is a sailfish mounted on the wall.

Reference Answer: False

Left image URL: http://hgtvhome.sndimg.com/content/dam/images/hgtv/fullset/2013/3/4/0/sh13_08-living-room-EPP7263_4x3.jpg.rend.hgtvcom.616.462.suffix/1400976272082.jpeg

Right image URL: http://hgtvhome.sndimg.com/content/dam/images/hgrm/fullset/2013/6/25/0/sh13_09-living-room-EPP5082_4x3.jpg.rend.hgtvcom.1280.960.suffix/1405441949537.jpeg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a sailfish mounted on the wall.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a sailfish mounted on the wall.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


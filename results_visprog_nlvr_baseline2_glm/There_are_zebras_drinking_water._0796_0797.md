Question: There are zebras drinking water.

Reference Answer: False

Left image URL: http://1.bp.blogspot.com/-muQGsr0nV8Q/VDBBYQTp_-I/AAAAAAAADKQ/YhmQTBEoHP4/s1600/file000729957443.jpg

Right image URL: http://www.teamwindchase.com/Zebras_10_375.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are zebras drinking water.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are zebras drinking water.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False


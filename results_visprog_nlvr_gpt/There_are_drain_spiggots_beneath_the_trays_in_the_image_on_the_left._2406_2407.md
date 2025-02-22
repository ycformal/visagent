Question: There are drain spiggots beneath the trays in the image on the left.

Reference Answer: True

Left image URL: https://3.imimg.com/data3/CS/LK/MY-3662038/3sink-work-table-500x500.jpg

Right image URL: https://5.imimg.com/data5/UD/AK/MY-2/three-sink-unit-500x500.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Are there drain spiggots beneath the trays?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there drain spiggots beneath the trays?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


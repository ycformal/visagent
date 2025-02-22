Question: There are drain spiggots beneath the trays in the image on the left.

Reference Answer: True

Left image URL: https://4.imimg.com/data4/SK/NQ/MY-900071/three-sink-unit-500x500.jpg

Right image URL: https://content4.jdmagicbox.com/comp/delhi/i2/011pxx11.xx11.140918211805.x2i2/catalogue/a-g-commercial-kitchen-equipment-pvt-ltd-west-punjabi-bagh-delhi-28.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Are there drain spiggots beneath the trays?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there drain spiggots beneath the trays?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False


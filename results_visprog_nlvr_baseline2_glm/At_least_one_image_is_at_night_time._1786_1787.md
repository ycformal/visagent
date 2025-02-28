Question: At least one image is at night time.

Reference Answer: False

Left image URL: http://media2.abc15.com//photo/2010/11/27/ADOT_snowplow_2_20101127102153_320_240.JPG

Right image URL: https://i.pinimg.com/564x/42/57/1f/42571fd57cdfe030bba28a70b9503fa1--snow-plow-rigs.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one image is at night time.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one image is at night time.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true


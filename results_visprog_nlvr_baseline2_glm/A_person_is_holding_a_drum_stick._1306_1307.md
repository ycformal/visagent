Question: A person is holding a drum stick.

Reference Answer: False

Left image URL: http://www.toucans.net/css_pix/magicpans_large.jpg

Right image URL: https://cdn.asme.org/wwwasmeorg/media/ASMEMedia/CareerEducation/EarlyCareerEngineers/METoday/engineering_drums_1.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A person is holding a drum stick.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A person is holding a drum stick.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false


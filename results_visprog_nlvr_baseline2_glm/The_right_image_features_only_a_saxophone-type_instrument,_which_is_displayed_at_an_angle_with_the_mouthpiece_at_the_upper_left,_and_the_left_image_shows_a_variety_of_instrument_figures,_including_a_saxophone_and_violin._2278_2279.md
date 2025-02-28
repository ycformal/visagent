Question: The right image features only a saxophone-type instrument, which is displayed at an angle with the mouthpiece at the upper left, and the left image shows a variety of instrument figures, including a saxophone and violin.

Reference Answer: True

Left image URL: https://img1.etsystatic.com/189/1/12323349/il_340x270.1270434897_5uo3.jpg

Right image URL: http://store.drumbum.com/media/saxophone-with-austrian-crystals-night-light.jpg

Original program:

```
Statement: The right image features only a saxophone-type instrument, which is displayed at an angle with the mouthpiece at the upper left, and the left image shows a variety of instrument figures, including a saxophone and violin.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image features only a saxophone-type instrument, which is displayed at an angle with the mouthpiece at the upper left, and the left image shows a variety of instrument figures, including a saxophone and violin.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image features only a saxophone-type instrument, which is displayed at an angle with the mouthpiece at the upper left, and the left image shows a variety of instrument figures, including a saxophone and violin.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


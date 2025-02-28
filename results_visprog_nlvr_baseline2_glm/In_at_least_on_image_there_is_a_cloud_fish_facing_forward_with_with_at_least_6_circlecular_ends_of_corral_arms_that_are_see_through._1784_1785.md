Question: In at least on image there is a cloud fish facing forward with with at least 6 circlecular ends of corral arms that are see through.

Reference Answer: True

Left image URL: http://www.baltana.com/download/6821/1680x1050/crop/clown-fish-animal-wallpaper-06498.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/da/c8/ab/dac8abe0b7267b1426d6966b68e4e04c--white-anemone-sea-fish.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least on image there is a cloud fish facing forward with with at least 6 circlecular ends of corral arms that are see through.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least on image there is a cloud fish facing forward with with at least 6 circlecular ends of corral arms that are see through.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


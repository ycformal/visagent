Question: There are zebras drinking water.

Reference Answer: False

Left image URL: http://1.bp.blogspot.com/-muQGsr0nV8Q/VDBBYQTp_-I/AAAAAAAADKQ/YhmQTBEoHP4/s1600/file000729957443.jpg

Right image URL: http://www.teamwindchase.com/Zebras_10_375.jpg

Program:

```
Statement: There are zebras drinking water.
Program:
ANSWER0=VQA(image=LEFT,question='Are there zebras drinking water?')
ANSWER1=VQA(image=RIGHT,question='Are there zebras drinking water?')
ANSWER2=EVAL(expr='{ANSWER0} or {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'There'


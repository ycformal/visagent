Question: Are his skis in the air?

Reference Answer: no

Image path: ./sampled_GQA/413948.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='skier')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='skis')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are his skis in the air?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABCAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDvKSlxSUCEpCaXFBFAhuaCaU1FLIIo2dugGaSVwbSV2cv4puJJriCyjRix5x6k1tWLtZ2cMAs58KoBPy/41gaaH1LWpb5+URsL9e36V1y8iu3ENQhGlbb8zycFF1ak8Re19vQQT5UExyL9Vo84dgfxFSY4phTJzXHoeraXcaLmPoSfyNPEinvTPLUHOKNmDwaNBJy6imeMHBdQfrRUbQgnOKKq0Rc0+xdNJilNFSaCUmKWkNJgNNYPiHUPLiFnB808p27R1Ga255FhiZ2OABXK6TDJqWuSX7D93GxwT0Jrpw8FrUlsvzPPx9WXu0Iby/BdTYsLOLStPjjdkXHzSOzADP1NXZp4oQpeWNSMnDMBkd6zfEVmNR0mSz+XdK6IhYZAbcMGsLRLn/hHLl9NvQZVLbXl5YINuep6g9Tmsptzbkzso01BKEFp/kdoriRFdCGRhkMOhFO7U2JI44lSJVWMD5QowAPangVkaDCKKcRSUwEopaKAJ6Q0U00wFJpCaSs3WNQFlbEKQZDwo9acIOcuVGdWrGlBzlsjP1u+eeZLG2G55OCfQVq2NqlhZJCg+6Mk+prO0SweINdXAPnSc4J6CthuFretJJKnHZHFhYSk3iKm728kU7mJbuFo2DAZBDKcEEHIwfqKqanDIYpLmJCHCsXTgpKMchgevArWVQBjFLJEkqbHGVzyM9a52d8dDDjTUbO0t2gBUSFVeFjuWPP93PIxXQKMKBycCmNEjsjMuShyvsafmkULSd6N1ITQAUUmaKAJiaaaM1BdXUdpC0srAKB+dNJt2RMpKKu9gu7uO0gaSQgY6Vz1nbyapd/2hcgiBT8i/wB40QpLr18J5QwtU6Ie9dFGiABVA2rwAOldTtQVl8T38jzEnjJ87+Bbefn6CqP4sYJpPvN7CntwMCgLgVzX6npW6CUUuKXFSUJmjNLijbQAlNNP20hWgYyipNlFACmuV8TM32mFNx2+meKKK6cJ/FR52af7tI3LRQlggUBRtHTiri8AYoorOp8T9TfD/wAOPoKfvUtFFZs3QCloopFBRRRQAtJRRQAoooopDP/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are his skis in the air?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no


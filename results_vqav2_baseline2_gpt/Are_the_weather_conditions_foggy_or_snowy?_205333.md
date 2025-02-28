Question: Are the weather conditions foggy or snowy?

Reference Answer: foggy

Image path: ./sampled_GQA/205333.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='weather')
ANSWER0=VQA(image=IMAGE,question='What are the weather conditions?')
ANSWER1=EVAL(expr="'foggy' if 'foggy' in {ANSWER0} else 'snowy' if 'snowy' in {ANSWER0} else 'neither'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are the weather conditions foggy or snowy?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAaAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwC8NJljHzKVHqeKX+zFYZI4PepIpXYguc49a0RfOIwhKlR2Ir2ZVZrY8eNKPVmK2mBWyAPxqNtPZWGcAHmr+paja6fYyXlyGWJCu4oM7ckDOPTmklVieMHn1pe3lsyvYpalvS7WGBASwLHtnGK6u1jMkW5p9uBwF5NcUpkwCBjjrV+C+kt4htyx9QeT+dclS8nc6qbUVY62DSxJlxKH78jFV5rWGVzEk0aS9hINvP1Nc03iC7jBVnCoegIyc1VbX7q53IhV0B5OOP1rLkkac6Nq+8N6vEPM2iVCePLbP6Vi3Vvc2zbJo2Q+hFadlr2qwW+22aIKBwMDP4elZ19qk87F72VmY9yaauhOzMxlO7pUTgirsdzDJwq+Ye3UU67SAkbMK2OcHIzWlyDIYDNFSuqhsZzRTC5bRjjrSSeabm3dZNsabi65+9kYH6801egpx6Vu9TC1ij4gjjv9CvLRwzeZGcBVJJI5GMe4FXorlXgjKbh8o+Vuo46H3qJjxTY+ZRUtFLaxoQ3KoACe3SrAvYSwBYA9twIz+NZt+AIlYAAgjB/GqoZhdKAxAOcjPXis2rs0WiubjS28oGQjg9MHrTIotNR/nt+vcOQazJFVwAyhuvUZ7VjQTSi82iR9vpuOKzkrFxZ6KNfeGFYYiREBjBxzWDdXjySklM46EVURiUU5PT1prE88moUUhtscbnJwTzUTPnvUUvSoGJyvJrREsmZhmioT1oqrE3P/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are the weather conditions foggy or snowy?')=<b><span style='color: green;'>foggy</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>foggy</span></b></div><hr>

Answer: foggy


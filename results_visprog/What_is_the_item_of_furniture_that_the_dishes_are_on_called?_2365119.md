Question: What is the item of furniture that the dishes are on called?

Reference Answer: The piece of furniture is a shelf.

Image path: ./sampled_GQA/2365119.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='dishes')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the item of furniture that the dishes are on called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='dishes')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAcAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzGMk2sR9CRWexw5HvWjDepJp6WZRQ8MjOsndg2Mj8CM/iaxrpily69Oa54KzaPQb0uWN3p1FaB+6DWDmUjKk/hTXmnPDOx+prRxuEK6hfQ15XUfeYD8arm4hHVxWYSxNJtb0o5EDxcuiNT7ZAP4v0pft8A/ib8qzPLal8o+350+RC+tVexqLqEOfvH/vmrcV5byLjzVB9+K5/aF6sPzp6SKOgzScENYqfWx18C7lGCMdcg1NNdxwxrG8sagdcsOtYlvdxSWcEMm8cspKNt+nbmsy58pXOyYtz0ZcH9MilGA6mI7I6f+07Mcfak/AGiuQ3f7VFXyIx+sy7F8Af2i5ViFBJ/r/Wo7/BuNw7ir1qoM7ZA+6apXoAePj+Gsk/eLS0ZROQcikYydQTUrCmhQR3ra5hKOpHuk9TRl/U1YEY9TS+WM0XD2b7kbkNbRDI3qzA49OCM8c9+5/DvFtJq4sSn1qeO0jc8lvzpORaoNmaIx3NSIqg9PzrZg0uCQcs/wCBH+FaMXh+zYctLx7j/ColVSNI4dmChHl8gYHrVeZY2bjOfrXbw+GbBkGTMc/7f/1qk/4RbS1xmOQ/VzWarxRcqLe559sor0dPC+k7ebdj/wADP+NFH1mPYj6sj//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the item of furniture that the dishes are on called?')=<b><span style='color: green;'>cabinet</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>cabinet</span></b></div><hr>

Answer: cabinet

Question: What is the item of furniture that the dishes are on called?

Reference Answer: The piece of furniture is a shelf.

Image path: ./sampled_GQA/2365119.jpg

Program:

```
 What is the <attr> of A <spatial pos> B called?
Program:
BOX0=LOC(image=IMAGE,object='dishes')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='furniture')
ANSWER0=VQA(image=IMAGE0,question='What is the item of furniture that the dishes are on called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='dishes')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAcAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzGMk2sR9CRWexw5HvWjDepJp6WZRQ8MjOsndg2Mj8CM/iaxrpily69Oa54KzaPQb0uWN3p1FaB+6DWDmUjKk/hTXmnPDOx+prRxuEK6hfQ15XUfeYD8arm4hHVxWYSxNJtb0o5EDxcuiNT7ZAP4v0pft8A/ib8qzPLal8o+350+RC+tVexqLqEOfvH/vmrcV5byLjzVB9+K5/aF6sPzp6SKOgzScENYqfWx18C7lGCMdcg1NNdxwxrG8sagdcsOtYlvdxSWcEMm8cspKNt+nbmsy58pXOyYtz0ZcH9MilGA6mI7I6f+07Mcfak/AGiuQ3f7VFXyIx+sy7F8Af2i5ViFBJ/r/Wo7/BuNw7ir1qoM7ZA+6apXoAePj+Gsk/eLS0ZROQcikYydQTUrCmhQR3ra5hKOpHuk9TRl/U1YEY9TS+WM0XD2b7kbkNbRDI3qzA49OCM8c9+5/DvFtJq4sSn1qeO0jc8lvzpORaoNmaIx3NSIqg9PzrZg0uCQcs/wCBH+FaMXh+zYctLx7j/ColVSNI4dmChHl8gYHrVeZY2bjOfrXbw+GbBkGTMc/7f/1qk/4RbS1xmOQ/VzWarxRcqLe559sor0dPC+k7ebdj/wADP+NFH1mPYj6sj//Z">, <b><span style='color: darkorange;'>object</span></b>='furniture')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAcAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzGMk2sR9CRWexw5HvWjDepJp6WZRQ8MjOsndg2Mj8CM/iaxrpily69Oa54KzaPQb0uWN3p1FaB+6DWDmUjKk/hTXmnPDOx+prRxuEK6hfQ15XUfeYD8arm4hHVxWYSxNJtb0o5EDxcuiNT7ZAP4v0pft8A/ib8qzPLal8o+350+RC+tVexqLqEOfvH/vmrcV5byLjzVB9+K5/aF6sPzp6SKOgzScENYqfWx18C7lGCMdcg1NNdxwxrG8sagdcsOtYlvdxSWcEMm8cspKNt+nbmsy58pXOyYtz0ZcH9MilGA6mI7I6f+07Mcfak/AGiuQ3f7VFXyIx+sy7F8Af2i5ViFBJ/r/Wo7/BuNw7ir1qoM7ZA+6apXoAePj+Gsk/eLS0ZROQcikYydQTUrCmhQR3ra5hKOpHuk9TRl/U1YEY9TS+WM0XD2b7kbkNbRDI3qzA49OCM8c9+5/DvFtJq4sSn1qeO0jc8lvzpORaoNmaIx3NSIqg9PzrZg0uCQcs/wCBH+FaMXh+zYctLx7j/ColVSNI4dmChHl8gYHrVeZY2bjOfrXbw+GbBkGTMc/7f/1qk/4RbS1xmOQ/VzWarxRcqLe559sor0dPC+k7ebdj/wADP+NFH1mPYj6sj//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the item of furniture that the dishes are on called?')=<b><span style='color: green;'>cabinet</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>cabinet</span></b></div><hr>

Answer: cabinet

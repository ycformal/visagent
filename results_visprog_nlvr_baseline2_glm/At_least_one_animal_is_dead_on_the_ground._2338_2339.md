Question: At least one animal is dead on the ground.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/h8VRXTswZF4/hqdefault.jpg

Right image URL: https://photos.smugmug.com/Mammals/Common-Warthog/i-6ZXNMn4/0/66a14afd/O/DC4F5614.jpg

Original program:

```
The program provided does not have a statement or question related to this scenario. Therefore, we cannot determine if the statement is true or false based on the given program.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAmAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDjtJjcaHp6kf8ALANgDqCK0HWae2QiP5VO49M49fcVreFdAubvQtHnU5ja2RmBHLD0/QVFqJW2UWVkR50asJCRwwz0B9K4Wm5M7FokNt4HVN65WIMAcnkeh/SrljeSLDdIZPNeIEkgYyOzD0qhbMZ2c3EwSONc7V4z9aINeWPUzbWek/aLiciInzMA54z9adOC3kKT7HU6cZTYqZZWkD4/eE5JyT+ldF8PlCQ+IlOCBrc3I/65xUkemCHyjNs87y1R9g4JA7VF4HJjHiMeYF/4nc3BIGf3cXrWU9mUlqjtw6gdeK53X/FEOiskSQ+fNIM8tgKM47VqPeKseRKhAOD83P5VwnjeaB5rd1I3+WVcBs4Ocj881nBXZpZDX+I8kV80MtiiEfdkVmYHPsaL/wAVXktu0m5ZIyN21AVH/wCuuXa0jlhV2YjPzA+lKPMjjbMkrjbgJnAP4D+ddKhHsQ7miNSnvYZWltgqHG1ihBJ/+tVSTgEsx/lXP/bTFcKUJiBGNoJ+X2xWlFJI8Ee5QA4ztHJH+FaWS2MnfqWBIeep59aKgZVLHLr+NFAjtfBCqvgXQnP/AD5pgjt1rjbuLN1reozArBZu0cYB5kkJ4QD1rrPBV0W8FaFAuAy2SDJPHOali0eK10+ONxuaSczuWHRieDjtgcVk5WbNLaI4iXRr6WIXLQBYghZld9rnjoAOprR8MafZ6f4lW+E3nRx2yPulwCHbgke4zgCulNtcSXDoQSSwCgjA2nGTn6Hj6VM2hQRMI/s6OgGDITyTngEVHO2iuVGmupx3So8aFs5HTGByPw6Vyeiveyz+Iri0RcNq8vzb1H8EfQGumt7F7WFlHLKoGSc/r3rn9D1+z0WXxFZyW7yy/wBsSsuwgAAxx9z9KNbaBomTT6dqMSLJNI2xhlhE+7HtxXO68Y4LLAadiX4LqBx6DH41p32twXkxZrWWJW4Ajkyfrzx+lY9/c2PmQhrh2+bJ/iCDHp+NVBSvqOTVtDOsrye6scrFINny5x1Hb8cYzRfamtvbxbkflQMdOBVmwudOWyUNeSiXnEaJ8o59T61FJPG16iiTenlH58DrmtEQLd6erXDucKcKRntT7tfs5MKkEAA4HYnmsueKaW/IF3KsRXcNmPpire8BeefTiq0RLbe4hA9HB74I5opfPH8TqpPY9qKBHkG9gMbjj60eY/8Afb86KK6TmDzH/vN+dHmP/fb86KKADzH/ALzfnXo/gQZ0F2PX7Q/P4LRRUVPhNKfxHQyDc4GaqtCChyOtFFc50FSSIITgmo5JJFjjUhdikjjqeaKKpEskWWbOcptxzxzUg4+YjOTxk5xRRQDGyXRR9qhRj1XPP50UUUyT/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


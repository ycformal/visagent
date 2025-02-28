Question: At least one person can be seen lying in bed in one image and there is nobody in a bed in the other image.

Reference Answer: False

Left image URL: https://development.asia/sites/default/files/explainer/eliminating-malaria.jpg

Right image URL: https://fthmb.tqn.com/2z-3oZx_6R8EsNj7Mlh5gFg0cG4=/960x0/filters:no_upscale()/GettyImages-187139688-5970fa1703f40200106ef4c6.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one person can be seen lying in bed in one image and there is nobody in a bed in the other image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDwHFaem24lnQkdxxVOBRIduQCfWuisrKWOeFhHklA2F5yOOf1rKpKysb04X1PdPCPiJNE8HWb3E9tFbQsx3TDhckimeLdRh1nwy728sMlrM3mBoicHAxn6VwV5relD4fXNjqCSecjKqKhAcMGyOvTvz6VnWnjC0/4QUaakMqXNs2JX35VwxJGB278e1YJScTX3VI5u40lbi7ZU+WPJZ2PRUHU/0+tYWoIsU/lIMKoGQeuTzXoN/Hb2OmZZlMccYmuWH8Z/hQe2Tj8zXm00zzzSSucs7Fm+prSi3LUzrWWg0A8YqzGfXFEKRmAE43Z9K1YWtjEqeQkZGMsck10KKlpcwUminG4xtbkeua6fw3pSa7PFYqrtdyE7RwAQATnJ+lP0Xw9YzLFM4Zm3nG8/KRnjj6V6HrHhjSrrwbJ9nYR39oBKJwACUH3l+mDn8K4a6vJU4vfqdlP4XNnlctzDZI6QMx6ghjnPNY01zvcuxyxrqotG0zZmW783cQc5rH1nTbC0BNvc+ZIT9wEHaK61gpU480jneIjN2RhM6k5zRSLcSRrtXZgeqA0VXKiedkAJFSx3EqYAkYD/AHjxUFFOxKbRdli4MjXSOXOTl8kn1OCf1q/pGo2FurQ3VkJneTPmF8DHofasOipcU1ZlKbTujtvFdyLyzigsnjaAYmlMbA73xjp2CjoPrXF8jim0UoQ5FYJz5ncs25wK3tBtY7rUFSctsClsL6joKxLaN2QEY9q07JriGUsmAcYzmoqy0aTKhHVNnpbaVKvkeSjuP4unHpxW/DHciVUS3lWNkAkDjcGyMH8D6V5xa32qx8x3UbH3YCtJPEOvwAZaJh6A/wCBrx5qrtdHoxlDszlvFGj3vhzWJbdt4t2JeCTsyHp+I6GsJZMqwOCfpz+dd1rOr3Gt2qR3sC5ibKHk8kc/SuYmtIdrfLhj/EOtelRxMnFKpucVSilK8NjEbZnpRVp7NQ3ysce9FdXOjDkZn0UUVRIUUUUAFFFFAGnZf6hPqa0ou31oorirbnTT2NK2+7VkffH1oorz57nXEWTv9ax5+p+tFFXQFV2M2T75ooor0lscZ//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one person can be seen lying in bed in one image and there is nobody in a bed in the other image.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True


Question: Is the blue car to the right or to the left of the bench made of metal?

Reference Answer: The car is to the right of the bench.

Image path: ./sampled_GQA/n271392.jpg

Program:

```
 Is A <planar pos> or <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='bench made of metal')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='blue car')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'right' if {ANSWER0} > 0 else 'left'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='bench made of metal')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAmADADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDHm8M3Gm2guNUv4tDiPzeRPNulmUYBPlA5BA5IPUEZqzPqOkeHtLnOhXml311F+9F1qF1HK5wMgRQLlFbnAPXrXIS+Htf3TMLSWZZ26zBQ3qSfm4PJ9a5q6hurTVDZzbPOhJiZZXVlBAxgknbWFPll1OlSSOqs/G2qy373FxqF00khYtHJcttcldpIJ+6w4x/Dx0x06zw94mk1hkgvriBowHf7BeWst0S3IkMZQFkwMdCMA9xXkMLTlhD5bSrkqBnI/D/Guy0jTtH/AOER1i6me7tNftEEltBNN5YZPlBZcgEnkjg56etdlSMHHYcJTk7XJZ9Vtf7ZCX8zrbsP3ThzmM59TzwPWtgG7tY57K9mkuHu4ma0dH27lIKAHnlDjHHT5cVzGg20fiK5ht/siTak77I4twj83uVJPsCQ3bmrd22uWeuaf4dFoJr21uGSCwQAlUkAJjEmfmQjDA9uT7UpNXKTdrnoZkVYWlEiEZ9eAPTnvXkfiZXXxneywpI7tIJ4zAcnkA5yMn1+lei3HhTXI5Waa40u2ZjnmDOP/HDWWYx4d1a01jU79rgmOa3ItrUh1DIRk4AGM/jzXm4ei6UtXuQqDjrc4FLyCVLyeQOkvDeWxZ/MycH5uoI65JwelXLe8u7+0a1WaGMWy+fE7McrjryM9jyMfyrQv/7E8TeK9SuJ9Re3gZY2hcQgGTCqrZDEEHI/nTNUt/D2nQQz6Zc3M1yJNksbnCtGQQcdx27nrXf7RpcpUYdSKy1XUbHTrmU3XmeSysDk/Mdy5weGA+mKz73xHqB8ULq9u6W97Ft2Oi42lVwOOmccelXr/wCyLFriWFtdpaLgIjfMY1JUjeeuMg8/T1rLjsDcatKskbr5h3IAuSSRkdOvbp60XXUuSnokfYIlkHBkY+x5/nSPZ2lx/rrO2kPQlohRRWZgzPm8KeHpyfN0e1y3UhOtVT8PvCbjadDsmHo0INFFMTbGp8O/C0NwlxFo1tHLH0eMuuR6EBsEex4rUi0TT4MLFawoo4CqgA/IUUUh8z7n/9k="></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAmADADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDHm8M3Gm2guNUv4tDiPzeRPNulmUYBPlA5BA5IPUEZqzPqOkeHtLnOhXml311F+9F1qF1HK5wMgRQLlFbnAPXrXIS+Htf3TMLSWZZ26zBQ3qSfm4PJ9a5q6hurTVDZzbPOhJiZZXVlBAxgknbWFPll1OlSSOqs/G2qy373FxqF00khYtHJcttcldpIJ+6w4x/Dx0x06zw94mk1hkgvriBowHf7BeWst0S3IkMZQFkwMdCMA9xXkMLTlhD5bSrkqBnI/D/Guy0jTtH/AOER1i6me7tNftEEltBNN5YZPlBZcgEnkjg56etdlSMHHYcJTk7XJZ9Vtf7ZCX8zrbsP3ThzmM59TzwPWtgG7tY57K9mkuHu4ma0dH27lIKAHnlDjHHT5cVzGg20fiK5ht/siTak77I4twj83uVJPsCQ3bmrd22uWeuaf4dFoJr21uGSCwQAlUkAJjEmfmQjDA9uT7UpNXKTdrnoZkVYWlEiEZ9eAPTnvXkfiZXXxneywpI7tIJ4zAcnkA5yMn1+lei3HhTXI5Waa40u2ZjnmDOP/HDWWYx4d1a01jU79rgmOa3ItrUh1DIRk4AGM/jzXm4ei6UtXuQqDjrc4FLyCVLyeQOkvDeWxZ/MycH5uoI65JwelXLe8u7+0a1WaGMWy+fE7McrjryM9jyMfyrQv/7E8TeK9SuJ9Re3gZY2hcQgGTCqrZDEEHI/nTNUt/D2nQQz6Zc3M1yJNksbnCtGQQcdx27nrXf7RpcpUYdSKy1XUbHTrmU3XmeSysDk/Mdy5weGA+mKz73xHqB8ULq9u6W97Ft2Oi42lVwOOmccelXr/wCyLFriWFtdpaLgIjfMY1JUjeeuMg8/T1rLjsDcatKskbr5h3IAuSSRkdOvbp60XXUuSnokfYIlkHBkY+x5/nSPZ2lx/rrO2kPQlohRRWZgzPm8KeHpyfN0e1y3UhOtVT8PvCbjadDsmHo0INFFMTbGp8O/C0NwlxFo1tHLH0eMuuR6EBsEex4rUi0TT4MLFawoo4CqgA/IUUUh8z7n/9k=">, <b><span style='color: darkorange;'>object</span></b>='blue car')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAmADADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDHm8M3Gm2guNUv4tDiPzeRPNulmUYBPlA5BA5IPUEZqzPqOkeHtLnOhXml311F+9F1qF1HK5wMgRQLlFbnAPXrXIS+Htf3TMLSWZZ26zBQ3qSfm4PJ9a5q6hurTVDZzbPOhJiZZXVlBAxgknbWFPll1OlSSOqs/G2qy373FxqF00khYtHJcttcldpIJ+6w4x/Dx0x06zw94mk1hkgvriBowHf7BeWst0S3IkMZQFkwMdCMA9xXkMLTlhD5bSrkqBnI/D/Guy0jTtH/AOER1i6me7tNftEEltBNN5YZPlBZcgEnkjg56etdlSMHHYcJTk7XJZ9Vtf7ZCX8zrbsP3ThzmM59TzwPWtgG7tY57K9mkuHu4ma0dH27lIKAHnlDjHHT5cVzGg20fiK5ht/siTak77I4twj83uVJPsCQ3bmrd22uWeuaf4dFoJr21uGSCwQAlUkAJjEmfmQjDA9uT7UpNXKTdrnoZkVYWlEiEZ9eAPTnvXkfiZXXxneywpI7tIJ4zAcnkA5yMn1+lei3HhTXI5Waa40u2ZjnmDOP/HDWWYx4d1a01jU79rgmOa3ItrUh1DIRk4AGM/jzXm4ei6UtXuQqDjrc4FLyCVLyeQOkvDeWxZ/MycH5uoI65JwelXLe8u7+0a1WaGMWy+fE7McrjryM9jyMfyrQv/7E8TeK9SuJ9Re3gZY2hcQgGTCqrZDEEHI/nTNUt/D2nQQz6Zc3M1yJNksbnCtGQQcdx27nrXf7RpcpUYdSKy1XUbHTrmU3XmeSysDk/Mdy5weGA+mKz73xHqB8ULq9u6W97Ft2Oi42lVwOOmccelXr/wCyLFriWFtdpaLgIjfMY1JUjeeuMg8/T1rLjsDcatKskbr5h3IAuSSRkdOvbp60XXUuSnokfYIlkHBkY+x5/nSPZ2lx/rrO2kPQlohRRWZgzPm8KeHpyfN0e1y3UhOtVT8PvCbjadDsmHo0INFFMTbGp8O/C0NwlxFo1tHLH0eMuuR6EBsEex4rUi0TT4MLFawoo4CqgA/IUUUh8z7n/9k="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAmADADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDHm8M3Gm2guNUv4tDiPzeRPNulmUYBPlA5BA5IPUEZqzPqOkeHtLnOhXml311F+9F1qF1HK5wMgRQLlFbnAPXrXIS+Htf3TMLSWZZ26zBQ3qSfm4PJ9a5q6hurTVDZzbPOhJiZZXVlBAxgknbWFPll1OlSSOqs/G2qy373FxqF00khYtHJcttcldpIJ+6w4x/Dx0x06zw94mk1hkgvriBowHf7BeWst0S3IkMZQFkwMdCMA9xXkMLTlhD5bSrkqBnI/D/Guy0jTtH/AOER1i6me7tNftEEltBNN5YZPlBZcgEnkjg56etdlSMHHYcJTk7XJZ9Vtf7ZCX8zrbsP3ThzmM59TzwPWtgG7tY57K9mkuHu4ma0dH27lIKAHnlDjHHT5cVzGg20fiK5ht/siTak77I4twj83uVJPsCQ3bmrd22uWeuaf4dFoJr21uGSCwQAlUkAJjEmfmQjDA9uT7UpNXKTdrnoZkVYWlEiEZ9eAPTnvXkfiZXXxneywpI7tIJ4zAcnkA5yMn1+lei3HhTXI5Waa40u2ZjnmDOP/HDWWYx4d1a01jU79rgmOa3ItrUh1DIRk4AGM/jzXm4ei6UtXuQqDjrc4FLyCVLyeQOkvDeWxZ/MycH5uoI65JwelXLe8u7+0a1WaGMWy+fE7McrjryM9jyMfyrQv/7E8TeK9SuJ9Re3gZY2hcQgGTCqrZDEEHI/nTNUt/D2nQQz6Zc3M1yJNksbnCtGQQcdx27nrXf7RpcpUYdSKy1XUbHTrmU3XmeSysDk/Mdy5weGA+mKz73xHqB8ULq9u6W97Ft2Oi42lVwOOmccelXr/wCyLFriWFtdpaLgIjfMY1JUjeeuMg8/T1rLjsDcatKskbr5h3IAuSSRkdOvbp60XXUuSnokfYIlkHBkY+x5/nSPZ2lx/rrO2kPQlohRRWZgzPm8KeHpyfN0e1y3UhOtVT8PvCbjadDsmHo0INFFMTbGp8O/C0NwlxFo1tHLH0eMuuR6EBsEex4rUi0TT4MLFawoo4CqgA/IUUUh8z7n/9k=">)=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'right' if ANSWER0 > 0 else 'left'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'right' if 0 > 0 else 'left'")=<b><span style='color: green;'>left</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>left</span></b></div><hr>

Answer: left

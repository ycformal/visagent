Question: On what type of furniture is that plant?

Reference Answer: The plant is on the desk.

Image path: ./sampled_GQA/n264887.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='plant')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='On what type of furniture is that plant?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='plant')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABgAFIDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDw44I4OfeomWnt8kx5yGoYZrI0vzIhPtwa2bO8E0a5P71fvD196xyKQFkfKkg9iKJR5kRGTiztYdajtYRkksD92hPEUl7eQ2kALGQ4JXnaPWuJLMc5JOferWnTSQX0bxfezjriqu0iHZs6e68PTXMxeS/kJz0cZH6VUXw/qdsxktvInGexwfyNWD4gvIZCrEOOmHQNVuDxSg4ls4yPVGK/41zqc0U4plKCBbOKSTWor2CPgR/ZolO5vQ54rodAjLWguIp54bRjiNZQpJx7DgVB/bukXkDQXMMnlvglXUOP0qo2maVOhXT9YltQ3/LLzDt/I1r7dW5ZIz9j1udabqxB/wCPlP8AvoUV5e9jbxyMnn79pI3Y6+9FLlo9gtPuZkzlpjwBg9AMU89M0yZcTtnjmmlzjFVa5pB23HBctjj1qSSKPaHGRnjk9DUQDwurMMqemOhFWBKSrKOATzQ9CJSdyqqlmCgcngVbtW8u/jcKSgJUHt0/yaREyQ7A7ecYPLVG8zs/JKgHhemPwoeuhKZNdXJldtgwOg9/eoFllHV6QHJJokDYHYHv60kraBdsUXbd1U/Tip4LrdKo+Yc565qkdoUjGST1z0qWAABn44+UCqaRVy0bklidueetFW44UEag9cDNFFybmbInmXBQFQWxgscD8TUUyLE+wMrYHJU5FSXYxL74quaFsUTx52diD2pSCMkAge9W7a1a508Sq4iMbeX/AL5+8PpVeWGaPhxkf3hyD+NLcTIG+Ykk9OlPExddrDd9aj4wRQoIII6UxD94A4Xj1NIdzAEjPpSEg8YxSSrtIAOVIypxjiiwWGE881btVGYwy7gxJIqqq72ArQt1zOB0C8YPamxsu4jHBY/nRVbKt83PPPSimRc6JtI03XBLJCslo0ZCBQd4U+hPceh61QfwZMB8l5Gf+AGptLe6s9QRYpmUzBQ4QnBQ9Q34V1IbmuSpzRl7st/Q3hZrVHGvYz6PYeTMyFmkZgVPUbcd6jttpgyRya2vEsZlS3AIB3Ec/Ss2zjX7OSMFg3IPYVrSvKOrInZPQqTJHuGURiezKDTdRgt4NgFvCWKgnbuGP1rSSQmUIFUg8ZxVW6eF3bzIlYA4z3ro5bR3Mr3ZhBlLlgigKOnWonLSNknJ6Vr/ANnRXCO1uzp03ZGQKVvDt2qb4jFMhGRtcAn86zbtuaIzbZgrEfxZ/SrKRnyQyjDSDA9+ahFvLEWLRMCxKKMdSDyB61NHI1vDEZFPyN90jkDNHUC8tjdqij5eBjqKKkEysMhxg80UrCOljWD7VJPHH5bPxj0HYfoKtK1ZsVwuz5cMPUGpluiRxxXPNczuaR0Vij4gPEHtk1mW5/d++7r6Ve1eQuqq44z8rdR24qhENmBkHvWlHYmZZQkEthSQOtVXS3kzuMqnrxzU+cRH3quq7pR6Z5rp6GXUtwK0MHlxL1Odzkc/lV9nWzsCTz5abm9zVVGBI54pt/KJbSSPpvGM1jVtZFwuZmnytPc2LysBHDuJZjxnJNQ3btPcSz9VDck+p/8A1VIyqLMw7RhGXHvTEt4pYXdnYPk8Z4IFCtuNijZgfKn/AHyaKrmGTPyyMB25oquUVzpWtFHzKCjf3k4NME0sRxLG7L/fjXP5j/CtPYR6VFJHlSRwfauds1sZv2hLiUhXDDuOn6GoSirMwAwB6Ut1EyEygfMnzfWo3kLTMV6EZBP0rSmtdCZ7DnHy4yaRUAOe9MLPg9CPpTkl3PgjBrosZE/QccVXuJCcA1aK/u/eqc4znPWsamrLhsVpH+VueOtVBNJGAMDFSS52sPaqzHNC0QPVl1b3CgFOcc0VS8wjjP6UVV2Fkf/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='On what type of furniture is that plant?')=<b><span style='color: green;'>table</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>table</span></b></div><hr>

Answer: table

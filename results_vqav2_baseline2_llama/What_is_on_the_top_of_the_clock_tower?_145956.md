Question: What is on the top of the clock tower?

Reference Answer: flag

Image path: ./sampled_GQA/145956.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='clock tower')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='umbrella')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'umbrella' if {ANSWER0} > 0 else 'nothing'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What is on the top of the clock tower?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA+AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDrwmDlcCtC1tpCQ2dwqgHKqA6bWzjGc1t2Q+VSMr7GvarSsjxqMdSaONHOAAHHrTWtyxO5QMVobUblkG71FOEYI4rgc7HcoFBFMYwoAFVL+QLERgZNbJWPGHHtWTf2Q3BlfKdMVdNpy1Jmmo6HM3bSx3dvHFbFoZAfMlD8xnt8vcHnntUgdguBUV9q1jb6q+ntcRtcqq7k3DcC3TjOTwR+dXls2LbWOD6da9CFSLWrOGcJJ6IqhiJM5IHvzUr3REZRCeepqz/ZpHLuAO3rTPsiIGDZJ7mm502JRmjOCZNG0g1O8QVsA5FNKc1te5jaw5F+UblyfY0UqlQOeTRWbRomU7m7NvqBWY4IBIYHA+gHbOD+Vaunawbp2VQvlqQAVOc8VyEF4L6OO3kkVHaXc2xckqAQMn1/xroNPS3hhkkjK/KAQCRyMdR/9euSPv7nXJci8zs7e7SRfvc1KJmJIH4Vx9hqsc+p+QWweOP1/wA/hXVW1souDOBucrs3bj0znGO1Y1KcY6o0pzk9GOnFw64XAPrWfqt9/ZGkvPKN5XhQOpY9q38ZHbIry34hRyXGvBprmUQRRqqRb1Cq2MtxtJOeOtYSqcsdDaMLvU5uweC/1h9X8Qaeguft0cimIbWJyAvIx3wPfFety2G+UPASjD7wrxfUYLrSFt7tJZGjEgco+1uFO4lWXHbnBHavoEFZQs8XRwGBx1B5qKFVq46tNOxjSQOB0Bx1zUP2UOxdASD2zW9NFHPGQw2t6jrWR5ckLFVk3Y6V1QndGEoWM+bTGA3oQB6E1QkiaNtrDBrYublgdrCs92LZzyOwPauylKbWpyVYwT0Km2ipse1Fb3MDlo7W2m1ZQdzxopYEkkMoGB07ZJrRkaIWkawRsC5KIpwoI6HOevOBVmykFtevLCgwY/IT9zgIqjLEe2Tj3xWhbjTbLSX1XV2jgHlhLdXwGWMdOvc8sT715cq/I7WPUVLnSdybRtOjiRHlhVWUZ5A4OP8APNdVAkuAVC7cdK8dm8aajqGrz/2M0L2vlBlQ5Rtg7nIPJJ7e1d34P1y81OxguHYrGR5TRlApBU8/l3qJ1VPYqFFx3NPxPr0HhrRXvblyjP8Au4m8tnUORwGx0ryifxraXN3LdSXVpM0jYMiygDnHG1hkY/pXo3xDut9jaWsVy8DFzMzIR91R3/WvLU064e8niZ7eS3hiV45JIonMj45GNuQAe+a46krs6Ix0Nrw49v4h8T6VCZoJoIXMh8mXcpweMj/gIP417YUyM5FfOumW9xafEezlsbRbidJI1litUCMy5BLqOhI+bIPavokcHrVQ2FLcQBRkMBVC+s97CROo/h9a0vlNAUOMVrGTi7oiUU1YwtkMi7JosMPaoJtNhVd6klOpHpW7LbqM/KDnvVKS3K7sA7T2reFXszCVPujmrj7NDLtNxGuRkBmANFWLzQlnm3GW4XAwAmMfqDRXaqq7nL7LyPOv+Elhhs7MRYjhdC4heUEnc/TIzjjPB9PeuY1zWL3xFc+fcyEsD8gX7oweOOlYFt4hl01WT7LBLGzbiHByT6kjHatSLxVp91DJFJoqJIEPzxycZ9cY968SpNyPWhFRLWk3B02Se8llcv5BUMy5JZug9Oveu6+Guv2zWGo29/My22lqhVH7Mc7gTjoWxj0rh4pLDUtPkjtVuIpl+Zi+CpAHTGaZo9zqIuWt7O8+yNcFY2kVN5O0McEHqKUZWHJXO48Q642sarNJbumyOJY4yCCp7kj8v1Fcl4dmuYY7mae8knWaUECUHK4+Y/0qbUINdizNcnSrwuNoZ4WRhxnqtZltrCxXC+fp0QKkkrFO+Cfqeahu+o0j0j4a2y6h4klvpY03RI8inqVJ+Uc/i1etmEN3xXjfwq1Ax6pc2yL8sq4yevHzf1r1q3uGlQt0wcVrDYiW5L5TL15FICUNSq+7g05owetXcmwKVdcE1HJGuDzxSbcHr0qREBxmgChLbNKwYTSoMYwjYH8qKx7nxdYwrC4t7krMhccqMYZl/mpoq7sXKf/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is on the top of the clock tower?')=<b><span style='color: green;'>flag</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>flag</span></b></div><hr>

Answer: flagpole


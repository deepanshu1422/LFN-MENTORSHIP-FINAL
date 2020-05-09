# LFN-MENTORSHIP-FINAL
Task by CHEN Liang SIR

To Verify the resource configuration of a type of hardware server.

Mentor :-CHEN Liang

Mentee :-Deepanshu Udhwani

  
  
  
  
  
  
  
  
![](https://lh6.googleusercontent.com/bqakPWHwi5g_Vf7v1o_etBw610eUNO63PKEi0LZVRmRrrzEADuzMoDR976cdhkFMOcOqd4uFiCjUXHLCdvTDWpmlqzFdavcLmQeBF37fVt6HdzvrUmb201z6QZxIkG8uM-NlIh51)  
  
  
  
  
  
  
  
  
  
  

Github Directory:-

[https://github.com/deepanshu1422/LFN-MENTORSHIP-FINAL](https://github.com/deepanshu1422/LFN-MENTORSHIP-FINAL)

  
  
  

### Introduction:

**To verify the resource configuration of a type of hardware server.
Only the server matching the requested configuration can be passed, otherwise checking will fail with a reason.**

  
  
  

## Problem Statement:

*Whenever a REST-API is called it returns a JSON. Here the motive of ours is to :*

  

-   Check whether the response from the API/JSON request is the same as we expected or not If all the parameters match then the requested configuration gets passed else it fails.
    

  

-   When it fails, we need to show why the test case failed and how can we correct the configuration.
    

  

-   Here we take 2 JSON files assuming that same response would be shared by the API call.
    

  
  
  
  
  
  
  
  
  
  
  

**

## Program Execution Diagram

**

  
![](https://docs.google.com/drawings/u/1/d/ssF4xCpVyL1TYQspvzI7FRg/image?w=573&h=431&rev=292&ac=1&parent=14-O13E_9D6b-rJV4s2Rz2OsOlun5BnZMr18yL05SPFg)  
  
  
  
  
  
  

***

The code comprises of few simple steps:

***

  

1.  We regard 1.json as a configuration file and 2.json the file that needs to get tested.
    
2.  These files are then imported to the [finalfile.py](https://github.com/deepanshu1422/LFN-MENTORSHIP-FINAL/blob/master/finalfile.py)
    
3.  Then the JSON file is dumped and loaded using the methods json.dumps() and JSON.load()
    
4.  By doing this we get a HashMap (dictionary in this case) along with the key-value pairs in sorted order.
    
5.  Now the key-value pairs are matched and length is found out.
    
6.  The answer would be true only if all key-value pairs in [1.json](https://github.com/deepanshu1422/LFN-MENTORSHIP-FINAL/blob/master/1.json) matches with key-value pairs of [2.json](https://github.com/deepanshu1422/LFN-MENTORSHIP-FINAL/blob/master/2.json) irrespective of whether more information is present in [2.json](https://github.com/deepanshu1422/LFN-MENTORSHIP-FINAL/blob/master/2.json)
    
7.  If the response is false , the file is traversed recursively to the lowest key and a dictionary gets stored.
    
8.  Sir, as instructed by you: In this whole exercise, I have used only 1 library “deep diff” in order to calculate the difference between 2 dictionaries.
    
9.  The difference is shown on the screen along with a rejection or the acceptance 
    

  
  

**

## Test Cases:

**

  

****I’ve tried to cover almost all functions/methods in UNIT Testing.
Basically most of the tests revolve around assertTrue() assertFalse() assertEqual()****

  
  

----------------------------------------------------------------------------------------------------

  
  

> Requirements for the Program

 - [x] Python 3

    pip install deepdiff

  
  

Clone the repository

    git clone https://github.com/deepanshu1422/LFN-MENTORSHIP-FINAL

  
  
  
  
  
  
  
  

> Check the contents of the file 1.json and 2.json

![](https://lh6.googleusercontent.com/l0lh6LGUd9eHNqECwz7JgS8weh6S_ZwyIpJnYIsxuxSwekMZA_AFgtPt_ZBuhd00wawIKChhGgeW4YU0D5YlH5UI0DVeqEJKN9zGA877LbH9aWXg16ykmKBqhtE__gsr9EX2uaSX)

  
  
  
  
  

> Open cmd/terminal on your system

![](https://lh5.googleusercontent.com/f5pAUJQCbHZit-R4_X-Fe1VVWUTP4IxAPEDyQn6wWsKSRNSaDQucvvO6UteC4mQyV2l45yt6rn3sCznUKYy0xsEX8H3kWYO_cIkZBc87DDn_gypn6wBnmI-PBO5W0uJitXh7j3mW)

  

> Test 1 (Both The Files Matches)

![](https://lh5.googleusercontent.com/V5LQKigmxmu9X7FdfsjRWYOf1VW0xZH7ilSrWNV5cVm2QqAALHg5g-t79S2dYSW3xm9TRxp7pObX_8xpaZONPosU3w5gJPGfotN7xudcxzjMoRbXYVeHoanepiTm6alLiyR6Keoh)

![](https://lh4.googleusercontent.com/HeMEEmvy0Rxw0TRUK2vTCza5Gsz2jd7XtGzeAy9mXTY0drm9zWbFJbzTA889D0FAi4cJ19YTdlrLK8JzFgyIaA2n0dI7ecvRsaTg3kkKDcEgV2bGyOr538cAXN3YYe8iUOmZZTGa)

  
  
  
  
  
  
  
  
  
  
  
  
  

> Test 2 (All contents of 1.json are present in 2.json along with other
> unwanted contents)

![](https://lh6.googleusercontent.com/KNfUfqdTMnzr7P8PJr6mQTT-CsH3PWWhIQrKPqrzmM4vDKmAYi9Pce7JoYAyqtCSEwqHVUbdQfVh-g4iWUC6x5Me-wtwMMw7Brj-qLATpqIuoGOc3FhQ0TEYp1EqUJMjtVB5SIBe)

![](https://lh6.googleusercontent.com/8c_UdgMkafT_mBCFdP3UNpotUxGatJwkFVaC2hML49Vr-7B5mBWX_5Eo_j-ivRrfffsYtiUZbIJ-OrZaI8xyGrPbsjSYD1qE-NiXJ4OCqVuwyrf76S0trfNNf-Tf8JtgRJ5vnpCI)

  
  
  
  

*

***Here the main thing to notice is we are always doing changes in 2.json not in 1.json***

*

  
  
  
  
  
  

> Test 3(Content in 2.json is changed which is already present in
> 1.json) :(

  

![](https://lh4.googleusercontent.com/GT5gEgQiPFOjpkXuD4hfBgn0uZrDf8HX3yp8RX8DA3wpWC6QOCVkTzET8VhcR9VVKXAJZgqTz4FdY0utc59TLKH5vQEZmkjl2c2Nl-ph5yWccHi-MDCo5F6gLieKjMXQAc-Rq0zA)

![](https://lh4.googleusercontent.com/k3-jDdnpkMmP1Pfh-TSaS08ICnu0noKu7azqV4w2Zm_mag3sa1GPbEnb8JGj2hP3Z4glPoG1FRdnUPReySKD1irhuqStrLXVZr-0nBlibznGo70Yw3qpXm9py95B1zMVhhWGeTOq)

  

> 3 Base and Most Important cases and screenshots are covered in this
> file in order to run others please run the unit tests as well as any
> random modification you would like :)

  
  
  
  
  
  

**Now to run the Unit Tests
Go inside the directory and run**

![](https://lh5.googleusercontent.com/DDq5qmaTv0Xeo3iWlq6ZKcJ43aCH2m3Drnu_C2_0Z0-y8jxIBiE8feLcQpK8TirVHJ5PPjn5r0gDqQRaTi2lRAjx8vFW8LyQ0UdyZP7fxpowJKOIfXJ_i2vECuKGnjfm-2_xG08a)

    nose2 -v

![](https://lh6.googleusercontent.com/4AWLYW-lFM-EQ7MF1OZZS7KHqaNyZ0labmpjtCJpeW78KhZhduuUzjt6DWxoWQa1vEoPC6XONL_gdF0DIgHFylN8LvtnAiyHMxewWpD_15mOBuYW6FqHVLWoMRJ-rXJCCHk0hc-e)

  

![](https://lh3.googleusercontent.com/cNpDlj8JGUFJMwSWQFiQTXGeE8AoDOJZsKYKledaaRq5w7IZ9jd5lN0VKRSjObaXp39juFAS7TGED3KAIVWUcx8Gf9IQF2QotYFaVNU8GJbOsVdKY1X-QriR15HhDN0bqLA7cYtO)

  
  

Deliverables:-

response JSON includes all the items of required items, then it should pass. which means:

- the order could be ignored     
 - [x] Done

-many more items may present in response but not in required items as long as the required items present in the response.

 - [x] Done

- The value for a key can be a number, string, or list or dictionary at any level.

 - [x] Done
- unit test function code

 - [x] Done


Thank You!

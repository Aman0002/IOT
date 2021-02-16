# Smart Lab System

### Description

1. This is  an Android based Application, which sends the control commands to the cloud for our appliances **Fan and Bulb** , with the help of two Buttons **TURN-ON** and **TURN-OFF**.
2. Our Android Application also have the facility to check the status of our Appliances ,whether they are ON or OFF from the cloud through a button **STATUS** .
3. The cloud we are using for this application is [Things Speak](https://thingspeak.com/) .
4. At the cloud ,I've made a single channel having two fields. **field1** for the Fan  ,**field2** for the Bulb .
   * If any field value is equals to 1 then it means that the appliance is ON! .
   * But, if filed value equals to 0 then it means that respective appliance is OFF!.
5. At the appliance end ,we are continuously reading the values of **field1** and **field2** from the cloud and accordingly turning on or off the appliances with the given python code,that is connected to our **Raspberry pie.** through the BOARD.

### NOTE:

``` 
After clicking on TURN-ON or TURN-OFF buttons inside our Android Application,I've made all buttons to be disabled for 15 seconds ,because of the sleep time of THINGSPEAK cloud.As it only get the data properly if and only if write-request made to the cloud is at an interval of 10-15 secs.
```



### RUN and SETUP

1. Install the **apk** file in the mobile,and make sure to turn on the INTERNET connection.

2. If want to run the code in android studio ,make sure that the :-

   ```
   a.)Give Internet Permission inside AndroidManifest.xml
   
   <uses-permission android:name="android.permission.INTERNET"/>
   ```

   ```
   b.)Add Dependency inside the build.grade(Module:app)
       
     implementation 'com.android.volley:volley:1.1.1'
   ```

3. Run the given python code ,at the appliances end by making the proper connection with Raspberry pie.




# Airplane_Operations_Detection
Airplane Operations Detection API

In this project, all operations of aircrafts monitored under human control have been automated.

The project is designed to process the sent image in cloud and send back the coordinates with the processed image.

![](https://github.com/ozkandgn/Airplane_Operations_Detection/blob/master/detection.gif)

This API can be modify and you can use as a server in your cloud for end device.

Used:

    TensorFlow Object Detection Library == 1.15.0
  
    Colab
  
    Docker
  
    Google Cloud Compute Engine
  
    Python-SocketIO
 
 
You can find Docker Image file : https://hub.docker.com/r/ozkandgn/tensor
 
If you want to use for prediction in your custom image, you can change inference_graph and training folders.

If you want to create inference_graph and training you can use colab and obj_det_colab.ipynb file. (You must create your own train.recor-test.record files)

I used 8888(jupyter), 8081(socket) port forwarding in docker.

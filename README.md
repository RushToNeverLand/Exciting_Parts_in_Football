# Exciting_Parts_in_Football
This repositpry in used to extract features of exciting football game part.

# Requirements(version 1.0):
1. Based on Ubuntu 16.04 LTS
2. Have installed the Caffe with Cuda 8.0(you can install CuDNN to accelerate it, that't depends on your GPU condition).
3. Prepare your own dataset.
4. Each single avi file is decoded with 5FPS (it's depend your decision) in a single directory.
5. Generate {train,test}.list files in list directory. Each line corresponds to "image directory" and a class (zero-based). 

# Usage
1. python train_c3d_ucf101.py will train C3D model. The trained model will saved in models directory.
2. python predict_c3d_ucf101.py will test C3D model on a validation data set.
3. cd ./C3D-tensorflow-1.0 &&python Random_clip_valid.py will get the random-clip accuracy on UCF101 test set with provided sports1m_finetuning_ucf101.model
4. C3D-tensorflow-1.0/Random_clip_valid.py code is compatible with tensorflow 1.0+ , with a little bit different with the old repository
5. IMPORTANT NOTE: when you load the sports1m_finetuning_ucf101.model,you should use the tranpose operation like:pool5 = tf.transpose(pool5, perm=[0,1,4,2,3]),or in Random_clip_valid.py looks like:["transpose", [0, 1, 4, 2, 3]], but if you load conv3d_deepnetA_sport1m_iter_1900000_TF.model or c3d_ucf101_finetune_whole_iter_20000_TF.model,you don't need tranpose operation,just comment that line code.

# Add the python files to detect the scoreboard
When goals happened, the scoreboard will change in a few seconds. So it's a good feature to record when to goal. And the accuary is high and the model is robust enough.

So far, we have two models to get the exciting parts of football game. We use two models to raise accuracy.

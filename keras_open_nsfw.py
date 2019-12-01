import keras
from keras.models import Model
from keras import layers
import keras.backend as K
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input

import numpy as np
import sys


def OpenNsfw(weight_file = "open_nsfw.h5"):
    data            = layers.Input(name = 'data', shape = (224, 224, 3,) )
    conv_1_input    = layers.ZeroPadding2D(padding = ((3, 3), (3, 3)))(data)
    conv_1          = layers.Conv2D(name='conv_1', filters=64, kernel_size=(7, 7), strides=(2, 2), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_1_input)
    bn_1            = layers.BatchNormalization(name = 'bn_1', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_1)
    relu_1          = layers.Activation(name = 'relu_1', activation = 'relu')(bn_1)
    pool1_input     = layers.ZeroPadding2D(padding = ((0, 1), (0, 1)))(relu_1)
    pool1           = layers.MaxPooling2D(name = 'pool1', pool_size = (3, 3), strides = (2, 2), padding = 'valid')(pool1_input)
    conv_stage0_block0_proj_shortcut = layers.Conv2D(name='conv_stage0_block0_proj_shortcut', filters=128, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(pool1)
    conv_stage0_block0_branch2a = layers.Conv2D(name='conv_stage0_block0_branch2a', filters=32, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(pool1)
    bn_stage0_block0_proj_shortcut = layers.BatchNormalization(name = 'bn_stage0_block0_proj_shortcut', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block0_proj_shortcut)
    bn_stage0_block0_branch2a = layers.BatchNormalization(name = 'bn_stage0_block0_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block0_branch2a)
    relu_stage0_block0_branch2a = layers.Activation(name = 'relu_stage0_block0_branch2a', activation = 'relu')(bn_stage0_block0_branch2a)
    conv_stage0_block0_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage0_block0_branch2a)
    conv_stage0_block0_branch2b = layers.Conv2D(name='conv_stage0_block0_branch2b', filters=32, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage0_block0_branch2b_input)
    bn_stage0_block0_branch2b = layers.BatchNormalization(name = 'bn_stage0_block0_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block0_branch2b)
    relu_stage0_block0_branch2b = layers.Activation(name = 'relu_stage0_block0_branch2b', activation = 'relu')(bn_stage0_block0_branch2b)
    conv_stage0_block0_branch2c = layers.Conv2D(name='conv_stage0_block0_branch2c', filters=128, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage0_block0_branch2b)
    bn_stage0_block0_branch2c = layers.BatchNormalization(name = 'bn_stage0_block0_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block0_branch2c)
    eltwise_stage0_block0 = layers.add(name = 'eltwise_stage0_block0', inputs = [bn_stage0_block0_proj_shortcut, bn_stage0_block0_branch2c])
    relu_stage0_block0 = layers.Activation(name = 'relu_stage0_block0', activation = 'relu')(eltwise_stage0_block0)
    conv_stage0_block1_branch2a = layers.Conv2D(name='conv_stage0_block1_branch2a', filters=32, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage0_block0)
    bn_stage0_block1_branch2a = layers.BatchNormalization(name = 'bn_stage0_block1_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block1_branch2a)
    relu_stage0_block1_branch2a = layers.Activation(name = 'relu_stage0_block1_branch2a', activation = 'relu')(bn_stage0_block1_branch2a)
    conv_stage0_block1_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage0_block1_branch2a)
    conv_stage0_block1_branch2b = layers.Conv2D(name='conv_stage0_block1_branch2b', filters=32, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage0_block1_branch2b_input)
    bn_stage0_block1_branch2b = layers.BatchNormalization(name = 'bn_stage0_block1_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block1_branch2b)
    relu_stage0_block1_branch2b = layers.Activation(name = 'relu_stage0_block1_branch2b', activation = 'relu')(bn_stage0_block1_branch2b)
    conv_stage0_block1_branch2c = layers.Conv2D(name='conv_stage0_block1_branch2c', filters=128, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage0_block1_branch2b)
    bn_stage0_block1_branch2c = layers.BatchNormalization(name = 'bn_stage0_block1_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block1_branch2c)
    eltwise_stage0_block1 = layers.add(name = 'eltwise_stage0_block1', inputs = [relu_stage0_block0, bn_stage0_block1_branch2c])
    relu_stage0_block1 = layers.Activation(name = 'relu_stage0_block1', activation = 'relu')(eltwise_stage0_block1)
    conv_stage0_block2_branch2a = layers.Conv2D(name='conv_stage0_block2_branch2a', filters=32, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage0_block1)
    bn_stage0_block2_branch2a = layers.BatchNormalization(name = 'bn_stage0_block2_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block2_branch2a)
    relu_stage0_block2_branch2a = layers.Activation(name = 'relu_stage0_block2_branch2a', activation = 'relu')(bn_stage0_block2_branch2a)
    conv_stage0_block2_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage0_block2_branch2a)
    conv_stage0_block2_branch2b = layers.Conv2D(name='conv_stage0_block2_branch2b', filters=32, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage0_block2_branch2b_input)
    bn_stage0_block2_branch2b = layers.BatchNormalization(name = 'bn_stage0_block2_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block2_branch2b)
    relu_stage0_block2_branch2b = layers.Activation(name = 'relu_stage0_block2_branch2b', activation = 'relu')(bn_stage0_block2_branch2b)
    conv_stage0_block2_branch2c = layers.Conv2D(name='conv_stage0_block2_branch2c', filters=128, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage0_block2_branch2b)
    bn_stage0_block2_branch2c = layers.BatchNormalization(name = 'bn_stage0_block2_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage0_block2_branch2c)
    eltwise_stage0_block2 = layers.add(name = 'eltwise_stage0_block2', inputs = [relu_stage0_block1, bn_stage0_block2_branch2c])
    relu_stage0_block2 = layers.Activation(name = 'relu_stage0_block2', activation = 'relu')(eltwise_stage0_block2)
    conv_stage1_block0_proj_shortcut = layers.Conv2D(name='conv_stage1_block0_proj_shortcut', filters=256, kernel_size=(1, 1), strides=(2, 2), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage0_block2)
    conv_stage1_block0_branch2a = layers.Conv2D(name='conv_stage1_block0_branch2a', filters=64, kernel_size=(1, 1), strides=(2, 2), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage0_block2)
    bn_stage1_block0_proj_shortcut = layers.BatchNormalization(name = 'bn_stage1_block0_proj_shortcut', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block0_proj_shortcut)
    bn_stage1_block0_branch2a = layers.BatchNormalization(name = 'bn_stage1_block0_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block0_branch2a)
    relu_stage1_block0_branch2a = layers.Activation(name = 'relu_stage1_block0_branch2a', activation = 'relu')(bn_stage1_block0_branch2a)
    conv_stage1_block0_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage1_block0_branch2a)
    conv_stage1_block0_branch2b = layers.Conv2D(name='conv_stage1_block0_branch2b', filters=64, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage1_block0_branch2b_input)
    bn_stage1_block0_branch2b = layers.BatchNormalization(name = 'bn_stage1_block0_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block0_branch2b)
    relu_stage1_block0_branch2b = layers.Activation(name = 'relu_stage1_block0_branch2b', activation = 'relu')(bn_stage1_block0_branch2b)
    conv_stage1_block0_branch2c = layers.Conv2D(name='conv_stage1_block0_branch2c', filters=256, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage1_block0_branch2b)
    bn_stage1_block0_branch2c = layers.BatchNormalization(name = 'bn_stage1_block0_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block0_branch2c)
    eltwise_stage1_block0 = layers.add(name = 'eltwise_stage1_block0', inputs = [bn_stage1_block0_proj_shortcut, bn_stage1_block0_branch2c])
    relu_stage1_block0 = layers.Activation(name = 'relu_stage1_block0', activation = 'relu')(eltwise_stage1_block0)
    conv_stage1_block1_branch2a = layers.Conv2D(name='conv_stage1_block1_branch2a', filters=64, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage1_block0)
    bn_stage1_block1_branch2a = layers.BatchNormalization(name = 'bn_stage1_block1_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block1_branch2a)
    relu_stage1_block1_branch2a = layers.Activation(name = 'relu_stage1_block1_branch2a', activation = 'relu')(bn_stage1_block1_branch2a)
    conv_stage1_block1_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage1_block1_branch2a)
    conv_stage1_block1_branch2b = layers.Conv2D(name='conv_stage1_block1_branch2b', filters=64, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage1_block1_branch2b_input)
    bn_stage1_block1_branch2b = layers.BatchNormalization(name = 'bn_stage1_block1_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block1_branch2b)
    relu_stage1_block1_branch2b = layers.Activation(name = 'relu_stage1_block1_branch2b', activation = 'relu')(bn_stage1_block1_branch2b)
    conv_stage1_block1_branch2c = layers.Conv2D(name='conv_stage1_block1_branch2c', filters=256, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage1_block1_branch2b)
    bn_stage1_block1_branch2c = layers.BatchNormalization(name = 'bn_stage1_block1_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block1_branch2c)
    eltwise_stage1_block1 = layers.add(name = 'eltwise_stage1_block1', inputs = [relu_stage1_block0, bn_stage1_block1_branch2c])
    relu_stage1_block1 = layers.Activation(name = 'relu_stage1_block1', activation = 'relu')(eltwise_stage1_block1)
    conv_stage1_block2_branch2a = layers.Conv2D(name='conv_stage1_block2_branch2a', filters=64, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage1_block1)
    bn_stage1_block2_branch2a = layers.BatchNormalization(name = 'bn_stage1_block2_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block2_branch2a)
    relu_stage1_block2_branch2a = layers.Activation(name = 'relu_stage1_block2_branch2a', activation = 'relu')(bn_stage1_block2_branch2a)
    conv_stage1_block2_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage1_block2_branch2a)
    conv_stage1_block2_branch2b = layers.Conv2D(name='conv_stage1_block2_branch2b', filters=64, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage1_block2_branch2b_input)
    bn_stage1_block2_branch2b = layers.BatchNormalization(name = 'bn_stage1_block2_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block2_branch2b)
    relu_stage1_block2_branch2b = layers.Activation(name = 'relu_stage1_block2_branch2b', activation = 'relu')(bn_stage1_block2_branch2b)
    conv_stage1_block2_branch2c = layers.Conv2D(name='conv_stage1_block2_branch2c', filters=256, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage1_block2_branch2b)
    bn_stage1_block2_branch2c = layers.BatchNormalization(name = 'bn_stage1_block2_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block2_branch2c)
    eltwise_stage1_block2 = layers.add(name = 'eltwise_stage1_block2', inputs = [relu_stage1_block1, bn_stage1_block2_branch2c])
    relu_stage1_block2 = layers.Activation(name = 'relu_stage1_block2', activation = 'relu')(eltwise_stage1_block2)
    conv_stage1_block3_branch2a = layers.Conv2D(name='conv_stage1_block3_branch2a', filters=64, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage1_block2)
    bn_stage1_block3_branch2a = layers.BatchNormalization(name = 'bn_stage1_block3_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block3_branch2a)
    relu_stage1_block3_branch2a = layers.Activation(name = 'relu_stage1_block3_branch2a', activation = 'relu')(bn_stage1_block3_branch2a)
    conv_stage1_block3_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage1_block3_branch2a)
    conv_stage1_block3_branch2b = layers.Conv2D(name='conv_stage1_block3_branch2b', filters=64, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage1_block3_branch2b_input)
    bn_stage1_block3_branch2b = layers.BatchNormalization(name = 'bn_stage1_block3_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block3_branch2b)
    relu_stage1_block3_branch2b = layers.Activation(name = 'relu_stage1_block3_branch2b', activation = 'relu')(bn_stage1_block3_branch2b)
    conv_stage1_block3_branch2c = layers.Conv2D(name='conv_stage1_block3_branch2c', filters=256, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage1_block3_branch2b)
    bn_stage1_block3_branch2c = layers.BatchNormalization(name = 'bn_stage1_block3_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage1_block3_branch2c)
    eltwise_stage1_block3 = layers.add(name = 'eltwise_stage1_block3', inputs = [relu_stage1_block2, bn_stage1_block3_branch2c])
    relu_stage1_block3 = layers.Activation(name = 'relu_stage1_block3', activation = 'relu')(eltwise_stage1_block3)
    conv_stage2_block0_proj_shortcut = layers.Conv2D(name='conv_stage2_block0_proj_shortcut', filters=512, kernel_size=(1, 1), strides=(2, 2), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage1_block3)
    conv_stage2_block0_branch2a = layers.Conv2D(name='conv_stage2_block0_branch2a', filters=128, kernel_size=(1, 1), strides=(2, 2), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage1_block3)
    bn_stage2_block0_proj_shortcut = layers.BatchNormalization(name = 'bn_stage2_block0_proj_shortcut', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block0_proj_shortcut)
    bn_stage2_block0_branch2a = layers.BatchNormalization(name = 'bn_stage2_block0_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block0_branch2a)
    relu_stage2_block0_branch2a = layers.Activation(name = 'relu_stage2_block0_branch2a', activation = 'relu')(bn_stage2_block0_branch2a)
    conv_stage2_block0_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage2_block0_branch2a)
    conv_stage2_block0_branch2b = layers.Conv2D(name='conv_stage2_block0_branch2b', filters=128, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage2_block0_branch2b_input)
    bn_stage2_block0_branch2b = layers.BatchNormalization(name = 'bn_stage2_block0_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block0_branch2b)
    relu_stage2_block0_branch2b = layers.Activation(name = 'relu_stage2_block0_branch2b', activation = 'relu')(bn_stage2_block0_branch2b)
    conv_stage2_block0_branch2c = layers.Conv2D(name='conv_stage2_block0_branch2c', filters=512, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block0_branch2b)
    bn_stage2_block0_branch2c = layers.BatchNormalization(name = 'bn_stage2_block0_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block0_branch2c)
    eltwise_stage2_block0 = layers.add(name = 'eltwise_stage2_block0', inputs = [bn_stage2_block0_proj_shortcut, bn_stage2_block0_branch2c])
    relu_stage2_block0 = layers.Activation(name = 'relu_stage2_block0', activation = 'relu')(eltwise_stage2_block0)
    conv_stage2_block1_branch2a = layers.Conv2D(name='conv_stage2_block1_branch2a', filters=128, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block0)
    bn_stage2_block1_branch2a = layers.BatchNormalization(name = 'bn_stage2_block1_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block1_branch2a)
    relu_stage2_block1_branch2a = layers.Activation(name = 'relu_stage2_block1_branch2a', activation = 'relu')(bn_stage2_block1_branch2a)
    conv_stage2_block1_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage2_block1_branch2a)
    conv_stage2_block1_branch2b = layers.Conv2D(name='conv_stage2_block1_branch2b', filters=128, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage2_block1_branch2b_input)
    bn_stage2_block1_branch2b = layers.BatchNormalization(name = 'bn_stage2_block1_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block1_branch2b)
    relu_stage2_block1_branch2b = layers.Activation(name = 'relu_stage2_block1_branch2b', activation = 'relu')(bn_stage2_block1_branch2b)
    conv_stage2_block1_branch2c = layers.Conv2D(name='conv_stage2_block1_branch2c', filters=512, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block1_branch2b)
    bn_stage2_block1_branch2c = layers.BatchNormalization(name = 'bn_stage2_block1_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block1_branch2c)
    eltwise_stage2_block1 = layers.add(name = 'eltwise_stage2_block1', inputs = [relu_stage2_block0, bn_stage2_block1_branch2c])
    relu_stage2_block1 = layers.Activation(name = 'relu_stage2_block1', activation = 'relu')(eltwise_stage2_block1)
    conv_stage2_block2_branch2a = layers.Conv2D(name='conv_stage2_block2_branch2a', filters=128, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block1)
    bn_stage2_block2_branch2a = layers.BatchNormalization(name = 'bn_stage2_block2_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block2_branch2a)
    relu_stage2_block2_branch2a = layers.Activation(name = 'relu_stage2_block2_branch2a', activation = 'relu')(bn_stage2_block2_branch2a)
    conv_stage2_block2_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage2_block2_branch2a)
    conv_stage2_block2_branch2b = layers.Conv2D(name='conv_stage2_block2_branch2b', filters=128, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage2_block2_branch2b_input)
    bn_stage2_block2_branch2b = layers.BatchNormalization(name = 'bn_stage2_block2_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block2_branch2b)
    relu_stage2_block2_branch2b = layers.Activation(name = 'relu_stage2_block2_branch2b', activation = 'relu')(bn_stage2_block2_branch2b)
    conv_stage2_block2_branch2c = layers.Conv2D(name='conv_stage2_block2_branch2c', filters=512, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block2_branch2b)
    bn_stage2_block2_branch2c = layers.BatchNormalization(name = 'bn_stage2_block2_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block2_branch2c)
    eltwise_stage2_block2 = layers.add(name = 'eltwise_stage2_block2', inputs = [relu_stage2_block1, bn_stage2_block2_branch2c])
    relu_stage2_block2 = layers.Activation(name = 'relu_stage2_block2', activation = 'relu')(eltwise_stage2_block2)
    conv_stage2_block3_branch2a = layers.Conv2D(name='conv_stage2_block3_branch2a', filters=128, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block2)
    bn_stage2_block3_branch2a = layers.BatchNormalization(name = 'bn_stage2_block3_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block3_branch2a)
    relu_stage2_block3_branch2a = layers.Activation(name = 'relu_stage2_block3_branch2a', activation = 'relu')(bn_stage2_block3_branch2a)
    conv_stage2_block3_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage2_block3_branch2a)
    conv_stage2_block3_branch2b = layers.Conv2D(name='conv_stage2_block3_branch2b', filters=128, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage2_block3_branch2b_input)
    bn_stage2_block3_branch2b = layers.BatchNormalization(name = 'bn_stage2_block3_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block3_branch2b)
    relu_stage2_block3_branch2b = layers.Activation(name = 'relu_stage2_block3_branch2b', activation = 'relu')(bn_stage2_block3_branch2b)
    conv_stage2_block3_branch2c = layers.Conv2D(name='conv_stage2_block3_branch2c', filters=512, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block3_branch2b)
    bn_stage2_block3_branch2c = layers.BatchNormalization(name = 'bn_stage2_block3_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block3_branch2c)
    eltwise_stage2_block3 = layers.add(name = 'eltwise_stage2_block3', inputs = [relu_stage2_block2, bn_stage2_block3_branch2c])
    relu_stage2_block3 = layers.Activation(name = 'relu_stage2_block3', activation = 'relu')(eltwise_stage2_block3)
    conv_stage2_block4_branch2a = layers.Conv2D(name='conv_stage2_block4_branch2a', filters=128, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block3)
    bn_stage2_block4_branch2a = layers.BatchNormalization(name = 'bn_stage2_block4_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block4_branch2a)
    relu_stage2_block4_branch2a = layers.Activation(name = 'relu_stage2_block4_branch2a', activation = 'relu')(bn_stage2_block4_branch2a)
    conv_stage2_block4_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage2_block4_branch2a)
    conv_stage2_block4_branch2b = layers.Conv2D(name='conv_stage2_block4_branch2b', filters=128, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage2_block4_branch2b_input)
    bn_stage2_block4_branch2b = layers.BatchNormalization(name = 'bn_stage2_block4_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block4_branch2b)
    relu_stage2_block4_branch2b = layers.Activation(name = 'relu_stage2_block4_branch2b', activation = 'relu')(bn_stage2_block4_branch2b)
    conv_stage2_block4_branch2c = layers.Conv2D(name='conv_stage2_block4_branch2c', filters=512, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block4_branch2b)
    bn_stage2_block4_branch2c = layers.BatchNormalization(name = 'bn_stage2_block4_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block4_branch2c)
    eltwise_stage2_block4 = layers.add(name = 'eltwise_stage2_block4', inputs = [relu_stage2_block3, bn_stage2_block4_branch2c])
    relu_stage2_block4 = layers.Activation(name = 'relu_stage2_block4', activation = 'relu')(eltwise_stage2_block4)
    conv_stage2_block5_branch2a = layers.Conv2D(name='conv_stage2_block5_branch2a', filters=128, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block4)
    bn_stage2_block5_branch2a = layers.BatchNormalization(name = 'bn_stage2_block5_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block5_branch2a)
    relu_stage2_block5_branch2a = layers.Activation(name = 'relu_stage2_block5_branch2a', activation = 'relu')(bn_stage2_block5_branch2a)
    conv_stage2_block5_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage2_block5_branch2a)
    conv_stage2_block5_branch2b = layers.Conv2D(name='conv_stage2_block5_branch2b', filters=128, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage2_block5_branch2b_input)
    bn_stage2_block5_branch2b = layers.BatchNormalization(name = 'bn_stage2_block5_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block5_branch2b)
    relu_stage2_block5_branch2b = layers.Activation(name = 'relu_stage2_block5_branch2b', activation = 'relu')(bn_stage2_block5_branch2b)
    conv_stage2_block5_branch2c = layers.Conv2D(name='conv_stage2_block5_branch2c', filters=512, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block5_branch2b)
    bn_stage2_block5_branch2c = layers.BatchNormalization(name = 'bn_stage2_block5_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage2_block5_branch2c)
    eltwise_stage2_block5 = layers.add(name = 'eltwise_stage2_block5', inputs = [relu_stage2_block4, bn_stage2_block5_branch2c])
    relu_stage2_block5 = layers.Activation(name = 'relu_stage2_block5', activation = 'relu')(eltwise_stage2_block5)
    conv_stage3_block0_proj_shortcut = layers.Conv2D(name='conv_stage3_block0_proj_shortcut', filters=1024, kernel_size=(1, 1), strides=(2, 2), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block5)
    conv_stage3_block0_branch2a = layers.Conv2D(name='conv_stage3_block0_branch2a', filters=256, kernel_size=(1, 1), strides=(2, 2), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage2_block5)
    bn_stage3_block0_proj_shortcut = layers.BatchNormalization(name = 'bn_stage3_block0_proj_shortcut', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block0_proj_shortcut)
    bn_stage3_block0_branch2a = layers.BatchNormalization(name = 'bn_stage3_block0_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block0_branch2a)
    relu_stage3_block0_branch2a = layers.Activation(name = 'relu_stage3_block0_branch2a', activation = 'relu')(bn_stage3_block0_branch2a)
    conv_stage3_block0_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage3_block0_branch2a)
    conv_stage3_block0_branch2b = layers.Conv2D(name='conv_stage3_block0_branch2b', filters=256, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage3_block0_branch2b_input)
    bn_stage3_block0_branch2b = layers.BatchNormalization(name = 'bn_stage3_block0_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block0_branch2b)
    relu_stage3_block0_branch2b = layers.Activation(name = 'relu_stage3_block0_branch2b', activation = 'relu')(bn_stage3_block0_branch2b)
    conv_stage3_block0_branch2c = layers.Conv2D(name='conv_stage3_block0_branch2c', filters=1024, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage3_block0_branch2b)
    bn_stage3_block0_branch2c = layers.BatchNormalization(name = 'bn_stage3_block0_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block0_branch2c)
    eltwise_stage3_block0 = layers.add(name = 'eltwise_stage3_block0', inputs = [bn_stage3_block0_proj_shortcut, bn_stage3_block0_branch2c])
    relu_stage3_block0 = layers.Activation(name = 'relu_stage3_block0', activation = 'relu')(eltwise_stage3_block0)
    conv_stage3_block1_branch2a = layers.Conv2D(name='conv_stage3_block1_branch2a', filters=256, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage3_block0)
    bn_stage3_block1_branch2a = layers.BatchNormalization(name = 'bn_stage3_block1_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block1_branch2a)
    relu_stage3_block1_branch2a = layers.Activation(name = 'relu_stage3_block1_branch2a', activation = 'relu')(bn_stage3_block1_branch2a)
    conv_stage3_block1_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage3_block1_branch2a)
    conv_stage3_block1_branch2b = layers.Conv2D(name='conv_stage3_block1_branch2b', filters=256, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage3_block1_branch2b_input)
    bn_stage3_block1_branch2b = layers.BatchNormalization(name = 'bn_stage3_block1_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block1_branch2b)
    relu_stage3_block1_branch2b = layers.Activation(name = 'relu_stage3_block1_branch2b', activation = 'relu')(bn_stage3_block1_branch2b)
    conv_stage3_block1_branch2c = layers.Conv2D(name='conv_stage3_block1_branch2c', filters=1024, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage3_block1_branch2b)
    bn_stage3_block1_branch2c = layers.BatchNormalization(name = 'bn_stage3_block1_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block1_branch2c)
    eltwise_stage3_block1 = layers.add(name = 'eltwise_stage3_block1', inputs = [relu_stage3_block0, bn_stage3_block1_branch2c])
    relu_stage3_block1 = layers.Activation(name = 'relu_stage3_block1', activation = 'relu')(eltwise_stage3_block1)
    conv_stage3_block2_branch2a = layers.Conv2D(name='conv_stage3_block2_branch2a', filters=256, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage3_block1)
    bn_stage3_block2_branch2a = layers.BatchNormalization(name = 'bn_stage3_block2_branch2a', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block2_branch2a)
    relu_stage3_block2_branch2a = layers.Activation(name = 'relu_stage3_block2_branch2a', activation = 'relu')(bn_stage3_block2_branch2a)
    conv_stage3_block2_branch2b_input = layers.ZeroPadding2D(padding = ((1, 1), (1, 1)))(relu_stage3_block2_branch2a)
    conv_stage3_block2_branch2b = layers.Conv2D(name='conv_stage3_block2_branch2b', filters=256, kernel_size=(3, 3), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(conv_stage3_block2_branch2b_input)
    bn_stage3_block2_branch2b = layers.BatchNormalization(name = 'bn_stage3_block2_branch2b', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block2_branch2b)
    relu_stage3_block2_branch2b = layers.Activation(name = 'relu_stage3_block2_branch2b', activation = 'relu')(bn_stage3_block2_branch2b)
    conv_stage3_block2_branch2c = layers.Conv2D(name='conv_stage3_block2_branch2c', filters=1024, kernel_size=(1, 1), strides=(1, 1), dilation_rate=(1, 1), padding='valid', use_bias=True)(relu_stage3_block2_branch2b)
    bn_stage3_block2_branch2c = layers.BatchNormalization(name = 'bn_stage3_block2_branch2c', axis = -1, epsilon = 9.999999747378752e-06, center = True, scale = True)(conv_stage3_block2_branch2c)
    eltwise_stage3_block2 = layers.add(name = 'eltwise_stage3_block2', inputs = [relu_stage3_block1, bn_stage3_block2_branch2c])
    relu_stage3_block2 = layers.Activation(name = 'relu_stage3_block2', activation = 'relu')(eltwise_stage3_block2)
    pool            = layers.AveragePooling2D(name = 'pool', pool_size = (7, 7), strides = (1, 1), padding = 'valid')(relu_stage3_block2)
    fc_nsfw_0       = __flatten(name = 'fc_nsfw_0', input = pool)
    fc_nsfw_1       = layers.Dense(name = 'fc_nsfw_1', units = 2, use_bias = True)(fc_nsfw_0)
    prob            = layers.Activation(name = 'prob', activation = 'softmax')(fc_nsfw_1)
    model           = Model(inputs = [data], outputs = [prob])
    model.load_weights(weight_file)
    return model

def __flatten(name, input):
    if input.shape.ndims > 2: return layers.Flatten(name = name)(input)
    else: return input

if __name__ == '__main__':
    model = OpenNsfw()

    img_path = sys.argv[1]
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    print('Predicted:', preds)

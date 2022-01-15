import string

width = 350
height = 100
label_len = 5

#characters = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
characters = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

label_classes = len(characters)+1

# save checkpoint path
cp_save_path = './models/weights_opencv_mix.hdf5' 

# the model for predicting
base_model_path = './colabModels/model_captcha_lorxx.h5'  

# TensorBoard save path, Optional
tb_log_dir = './tensorboard'  

#load_model_path = './goodModels/weights_loryxx_differentFonts3.hdf5'
load_model_path =''
# load_model_path = './models/weights.20-0.263-0.270.hdf5' # using pre-trained model
learning_rate = 0.01
initial_epoch = 0
is_training = True

#img_dir = './lorxx_opencv/'
img_dir = './database_test_lorxx_differentFonts2/'

# description_path = './data/train.csv'

# img_dir = './data/public_test'
# description_path = './data/public_test.csv'

# img_dir = './data/private_test'
# description_path = './data/private_test.csv'

N_EPOCHS = 150
BATCH_SIZE = 8
downsample_factor = 4

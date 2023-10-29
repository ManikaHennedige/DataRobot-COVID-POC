from App.utils.test_functions import load_labels, data_constructor, phase1_labels_updater
import tensorflow as tf

def preprocess(label_filename, image_folderpath, dims=(128,128)):

    fnames_test, classes_test , bboxes_test = load_labels(label_filename, image_folderpath)
    densenet_x, densenet_y = data_constructor(fnames_test, classes_test, dims , index  = [0] , bboxes = bboxes_test)
    densenet_x = tf.keras.applications.densenet.preprocess_input(densenet_x)
    densenet_y = phase1_labels_updater(densenet_y)

    return {'x': densenet_x, 'y': densenet_y}


import sys
import tensorflow as tf
from matplotlib import gridspec as gridspec
from matplotlib import pyplot as plt
import kernels

def read_one_image(filename):
    image_string = tf.read_file(filename)
    image_decoded = tf.image.decode_image(image_string)
    image = tf.cast(image_decoded, tf.float32)/256.0
    return image

def convolve(image, kernels, rgb=True, strides=[1,3,3,1], padding='SAME'):
    images = [image[0]]
    for i, kernel in enumerate(kernels):
        filtered_image = tf.nn.conv2d(image,
                                      kernel,
                                      strides,
                                      padding)[0]
        if i == 2:
            filtered_image = tf.minimum(tf.nn.relu(filtered_image), 255)
        images.append(filtered_image)
    return images

def show_images(images, rgb=True):
    gs = gridspec.GridSpec(1, len(images))
    for i, image in enumerate(images):
        plt.subplot(gs[0, i])
        if rgb:
            plt.imshow(image)
        else:
            image = image.reshape(image.shape[0], image.shape[1])
        plt.axis('off')
    plt.show()

def main():
    rgb = False
    if rgb:
        kernels_list = [kernels.BLUR_FILTER_RGB,
                        kernels.SHARPEN_FILTER_RGB,
                        kernels.EDGE_FILTER_RGB,
                        kernels.TOP_SOBEL_RGB,
                        kernels.EMBOSS_FILTER_RGB]
    else:
        kernels_list = [kernels.BLUR_FILTER,
                        kernels.SHARPEN_FILTER,
                        kernels.EDGE_FILTER,
                        kernels.TOP_SOBEL,
                        kernels.EMBOSS_FILTER]
    kernels_list = kernels_list[1:]
    image = read_one_image('data/friday.jpg')
    if not rgb:
        image = tf.image.rgb_to_grayscale(image)
    image = tf.expand_dims(image, 0)
    images = convolve(image, kernels_list, rgb)
    with tf.Session() as sess:
        images = sess.run(images)
    show_images(images, rgb)

if __name__ == "__main__":
    main()


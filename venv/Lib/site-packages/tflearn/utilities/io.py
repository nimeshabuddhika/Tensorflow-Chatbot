from __future__ import division, print_function, absolute_import

import numpy as np
import tensorflow as tf

from ..data_flow import ArrayFlow


def generate_data_tensor(X, Y, batch_size, shuffle=True, num_threads=1):
    #TODO: Add a way with no batch?
    #TODO: Set threads to #CPUs fo machine
    cr = None
    if isinstance(X, tf.Tensor) and isinstance(Y, tf.Tensor):
        if len(Y.get_shape().as_list()) > 1:
            raise Exception("Labels must be 1-D tensor.")
        # Optional Image and Label Batching
        if shuffle:
            X, Y = tf.train.shuffle_batch([X, Y], batch_size=batch_size,
                                      min_after_dequeue=batch_size,
                                      capacity=batch_size * num_threads * 4,
                                      num_threads=num_threads)
        else:
            X, Y = tf.train.batch([X, Y], batch_size=batch_size,
                                  capacity=batch_size * num_threads * 4,
                                  num_threads=num_threads)

    # Array Input
    elif X is not None and Y is not None:
        if len(list(np.shape(Y))) > 1:
            raise Exception("Labels must be 1-D array.")
        # Create a queue using feed_dicts
        cr = ArrayFlow(X, Y, batch_size, shuffle=True)
        X, Y = cr.get()
        X = tf.reshape(X, [-1] + list(np.shape(X)))
        Y = tf.reshape(Y, [-1] + list(np.shape(Y)))

    return X, Y, cr

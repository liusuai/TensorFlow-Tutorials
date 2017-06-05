import numpy as np
import tensorflow as tf
# reduction 简单粗暴的说就是，n 维的数据中，把某一个维度上这一序列的数缩减到一个（比如求它们的和或者平均值），这样就降低了一个维度，所以叫 reduce，
# 比如 map-reduce 也差不多是这个意思。上面 凡心 的图已经很清楚了，目前这个 reduction_indices 参数改名叫 axis ，这样就直白多了，代表 reduce 
# 是沿着哪个轴的方向进行的。

vec = np.array([
			  20, 50
			 ])
a = np.array([
			  [20.0, 5.0],
			  [15.0, 10.0]
			 ])
w = np.array([[2.0, 1.0], 
			  [1.0, 4.0]
			 ])

with tf.Session() as sess:
  # reference:https://www.zhihu.com/question/51325408

  # print (tf.multiply(tf.expand_dims(a,-1), w).eval()) # [[[ 40.  20.]  [  5.  20.]][[ 30.  15.][ 10.  40.]]]
  # print((tf.reduce_sum(tf.multiply(tf.expand_dims(a,-1), w), axis=0)).eval()) # [[ 70.  35.][ 15.  60.]]
  # print((tf.reduce_sum(tf.multiply(tf.expand_dims(a,-1), w), axis=1)).eval()) # [[45 40][40 55]]
  # print((tf.reduce_sum(tf.multiply(tf.expand_dims(a,-1), w), axis=2)).eval()) # [[60 25][45 50]]
  # ----------------------------------------------

  # reference:http://www.jianshu.com/p/00ab12bc357c
  tf.transpose(a, perm = None, name = 'transpose')

  # 解释：将a进行转置，并且根据perm参数重新排列输出维度。

  # 输出数据tensor的第i维将根据perm[i]指定。比如，如果perm没有给定，那么默认是perm = [n-1, n-2, ..., 0]，其中rank(a) = n。默认情况下，
  # 对于二维输入数据，其实就是常规的矩阵转置操作。 
  # print(tf.transpose(a).eval()) # [[ 20.  15.][  5.  10.]]
  print(tf.transpose(a,perm=[1, 0]).eval()) # [[ 20.  15.][  5.  10.]]
  input_data = tf.constant([[1,2,3],[4,5,6]])
  # print(sess.run(tf.transpose(input_data)))
  # print(sess.run(input_data))
  # print(sess.run(tf.transpose(input_data, perm=[1,0])))

  # print(tf.transpose(w).eval()) # [[ 2.  1.][ 1.  4.]]
  # print(tf.multiply(a, tf.transpose(w)).eval()) # [[ 40.   5.] [ 15.  40.]]
  # print((tf.reduce_sum(tf.multiply(a, tf.transpose(w)), axis=1)).eval()) # [ 45.  55.]

  # Note tf.multiply is equivalent to "*"
  # print((tf.reduce_sum(tf.expand_dims(a,-1) * w, axis=0)).eval())
  # print((tf.reduce_sum(a * tf.transpose(w), axis=1)).eval())







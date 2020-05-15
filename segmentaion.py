
def segement_liver(img, mask):
#     print(img.dtype)
#     print(mask.dtype)
    return  cv2.bitwise_and(src1, src2)
org =np.uint8(cv2.normalize(image_histogram_equalization(imgs_to_process[70]), None, 0, 255, cv2.NORM_MINMAX))

org =np.uint8(cv2.normalize(image_histogram_equalization(imgs_to_process[70]), None, 0, 255, cv2.NORM_MINMAX))

       
src1 = org 
src2 = make_mask(largest_shape)
segemented = segement_liver(src1,src2)

plt.imshow(segemented, cmap='gray')

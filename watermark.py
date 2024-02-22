import cv2

def add_watermark(original_image_path, watermark_image_path, output_image_path):
    original_image = cv2.imread(r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\hello.png')
    watermark_image = cv2.imread(r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\white.png', cv2.IMREAD_UNCHANGED)
    original_height, original_width = original_image.shape[:2]
    watermark_image = cv2.resize(watermark_image, (original_width, original_height))
    alpha_channel = watermark_image[:, :, 3]
    _, alpha_mask = cv2.threshold(alpha_channel, 128, 255, cv2.THRESH_BINARY)
    
    # Extract the RGB channels of the watermark image
    watermark = watermark_image[:, :, :3]

    # Create an inverted mask for the original image
    inv_alpha_mask = cv2.bitwise_not(alpha_mask)

    # Place the watermark on the original image using the mask
    result = cv2.bitwise_and(original_image, original_image, mask=inv_alpha_mask)
    result += cv2.bitwise_and(watermark, watermark, mask=alpha_mask)

    # Save the result
    cv2.imwrite(output_image_path, result)
    cv2.imshow("watermarked",result)
    cv2.waitkey(0)
    cv2.destroyAllWindows()

# Example usage
add_watermark("original_image.jpg", "watermark.png", "output_image.jpg")




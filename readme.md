Ok 👍 mình gợi ý **các bài tập OpenCV rất đơn giản**, phù hợp cho **người mới bắt đầu** (học từng bước, không cần toán cao siêu). Mỗi bài có **mục tiêu + gợi ý**, bạn có thể tự code rồi nhờ mình check sau.

---

## 🟢 Nhóm 1 – Làm quen với ảnh & OpenCV

### **Bài 1. Đọc và hiển thị ảnh**

**Yêu cầu**

* Đọc ảnh từ file
* Hiển thị ảnh ra màn hình

**Gợi ý**

* `cv2.imread`
* `cv2.imshow`
* `cv2.waitKey`

---

### **Bài 2. Chuyển ảnh sang grayscale**

**Yêu cầu**

* Đọc ảnh màu
* Chuyển sang ảnh xám
* Hiển thị cả ảnh gốc và ảnh xám

**Gợi ý**

* `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`

---

### **Bài 3. Resize ảnh**

**Yêu cầu**

* Resize ảnh về kích thước 300x300
* So sánh ảnh trước và sau

**Gợi ý**

* `cv2.resize`

---

## 🟡 Nhóm 2 – Xử lý ảnh cơ bản

### **Bài 4. Cắt ảnh (crop)**

**Yêu cầu**

* Cắt vùng giữa ảnh (ví dụ: 100×100 pixel)
* Hiển thị vùng đã cắt

**Gợi ý**

* Dùng slicing: `img[y1:y2, x1:x2]`

---

### **Bài 5. Lật ảnh**

**Yêu cầu**

* Lật ảnh:

  * ngang
  * dọc
  * cả hai

**Gợi ý**

* `cv2.flip(img, 0 / 1 / -1)`

---

### **Bài 6. Làm mờ ảnh (blur)**

**Yêu cầu**

* Làm mờ ảnh bằng Gaussian Blur
* Thử nhiều kernel khác nhau

**Gợi ý**

* `cv2.GaussianBlur`

---

## 🟠 Nhóm 3 – Ngưỡng & cạnh

### **Bài 7. Threshold (nhị phân hóa ảnh)**

**Yêu cầu**

* Chuyển ảnh xám sang ảnh trắng đen
* Thử nhiều ngưỡng khác nhau

**Gợi ý**

* `cv2.threshold`

---

### **Bài 8. Adaptive Threshold**

**Yêu cầu**

* Áp dụng adaptive threshold
* So sánh với threshold thường

**Gợi ý**

* `cv2.adaptiveThreshold`

---

### **Bài 9. Phát hiện cạnh**

**Yêu cầu**

* Dùng Canny để phát hiện cạnh

**Gợi ý**

* `cv2.Canny`

---

## 🔵 Nhóm 4 – Vẽ & thao tác hình học

### **Bài 10. Vẽ hình lên ảnh**

**Yêu cầu**

* Vẽ:

  * đường thẳng
  * hình chữ nhật
  * hình tròn
* Viết chữ lên ảnh

**Gợi ý**

* `cv2.line`
* `cv2.rectangle`
* `cv2.circle`
* `cv2.putText`

---

### **Bài 11. Dịch chuyển ảnh**

**Yêu cầu**

* Dịch ảnh sang phải 50px, xuống 30px

**Gợi ý**

* Ma trận affine + `cv2.warpAffine`

---

## 🔴 Nhóm 5 – Webcam (vui và thực tế 😄)

### **Bài 12. Mở webcam**

**Yêu cầu**

* Mở webcam
* Hiển thị video realtime
* Nhấn `q` để thoát

**Gợi ý**

* `cv2.VideoCapture(0)`

---

### **Bài 13. Webcam + grayscale**

**Yêu cầu**

* Webcam nhưng hiển thị ảnh xám

---

### **Bài 14. Webcam + phát hiện cạnh**

**Yêu cầu**

* Áp dụng Canny cho từng frame webcam

---

## ⭐ Bài nâng nhẹ (bonus)

### **Bài 15. Đếm pixel trắng**

**Yêu cầu**

* Với ảnh threshold
* Đếm số pixel trắng và đen

**Gợi ý**

* `np.sum(img == 255)`



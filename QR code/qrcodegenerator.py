import qrcode
import image as im


my_qr = qrcode.QRCode(
    version = 15,
    box_size =10,
    border = 5,
)
data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x"
my_qr.add_data(data)
my_qr.make(fit=True)
img = my_qr.make_image(fill ='red', back_color = 'blue')
img.save('test.png')
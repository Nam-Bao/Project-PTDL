import json
from kafka import KafkaProducer
from pymongo import MongoClient
import time
from bson import ObjectId

# Thiết lập kết nối tới MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')  # Thay thế với URL MongoDB của bạn
db = mongo_client['dbcardata']  # Thay thế 'your_database' với tên cơ sở dữ liệu của bạn
collection = db['cars']  # Thay thế 'your_collection' với tên collection của bạn

# Thiết lập Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],  # Thay thế với địa chỉ Kafka broker của bạn
    value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')  # Sử dụng default=str để chuyển ObjectId thành string
)

# Hàm để gửi dữ liệu từ MongoDB tới Kafka
def send_data_to_kafka():
    # Lấy dữ liệu từ MongoDB (ví dụ: tất cả các document trong collection)
    cursor = collection.find()
    
    for document in cursor:
        # Gửi mỗi document tới Kafka topic
        producer.send('cars', document)  # Thay thế 'your_topic' với tên topic Kafka của bạn
        print(f"Đã gửi dữ liệu: {document}")
        time.sleep(1)  # Giới hạn tốc độ gửi dữ liệu (1 giây)

    # Đảm bảo tất cả dữ liệu đã được gửi trước khi kết thúc
    producer.flush()

# Chạy hàm gửi dữ liệu
if __name__ == '__main__':
    send_data_to_kafka()
    print("Đã gửi toàn bộ dữ liệu từ MongoDB vào Kafka.")
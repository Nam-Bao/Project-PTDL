FROM python:3.13

WORKDIR /usr/src/app

# Sao chép requirements.txt và cài đặt các phụ thuộc
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn
COPY . .

CMD ["python", "xuliapp.py"]
